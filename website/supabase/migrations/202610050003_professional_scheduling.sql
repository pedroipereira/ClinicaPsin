alter type public.staff_role add value if not exists 'professional';

alter table public.staff_profiles
  add column if not exists professional_id uuid references public.professionals on delete set null;

alter table public.services
  add column if not exists buffer_minutes integer not null default 10
  check (buffer_minutes between 0 and 120);

alter table public.appointment_slots drop constraint if exists slot_professional_start_unique;
create unique index if not exists slot_service_start_unique
  on public.appointment_slots(professional_id, service_id, modality, starts_at);

create extension if not exists btree_gist;
alter table public.appointments
  add constraint appointments_no_professional_overlap
  exclude using gist (
    professional_id with =,
    tstzrange(starts_at, ends_at, '[)') with &&
  ) where (status in ('pending', 'confirmed'));

create table public.availability_rules (
  id uuid primary key default gen_random_uuid(),
  professional_id uuid not null references public.professionals on delete cascade,
  weekday smallint not null check (weekday between 0 and 6),
  starts_at time not null,
  ends_at time not null,
  modality public.appointment_modality not null,
  active boolean not null default true,
  created_at timestamptz not null default now(),
  check (ends_at > starts_at),
  unique (professional_id, weekday, starts_at, ends_at, modality)
);

create type public.schedule_exception_kind as enum ('vacation', 'holiday', 'personal', 'course', 'other');
create type public.schedule_exception_action as enum ('cancel', 'reschedule', 'block_only');

create table public.schedule_exceptions (
  id uuid primary key default gen_random_uuid(),
  professional_id uuid references public.professionals on delete cascade,
  starts_at timestamptz not null,
  ends_at timestamptz not null,
  kind public.schedule_exception_kind not null,
  action public.schedule_exception_action not null default 'reschedule',
  modality public.appointment_modality,
  internal_note text,
  created_by uuid references auth.users on delete set null,
  created_at timestamptz not null default now(),
  check (ends_at > starts_at)
);

create table public.recurring_appointments (
  id uuid primary key default gen_random_uuid(),
  professional_id uuid not null references public.professionals,
  service_id uuid not null references public.services,
  modality public.appointment_modality not null,
  patient_name text not null,
  responsible_name text,
  phone text not null,
  email text not null,
  starts_on date not null,
  ends_on date not null,
  local_start_time time not null,
  interval_days integer not null check (interval_days between 1 and 365),
  duration_minutes integer not null check (duration_minutes between 20 and 240),
  active boolean not null default true,
  created_by uuid references auth.users on delete set null,
  created_at timestamptz not null default now(),
  check (ends_on >= starts_on),
  check (ends_on <= starts_on + 366)
);

alter table public.appointments
  add column if not exists recurring_appointment_id uuid references public.recurring_appointments on delete set null;

alter table public.availability_rules enable row level security;
alter table public.schedule_exceptions enable row level security;
alter table public.recurring_appointments enable row level security;
revoke all on public.availability_rules, public.schedule_exceptions, public.recurring_appointments from anon, authenticated;

create or replace function public.generate_appointment_slots(
  p_service_slug text,
  p_modality public.appointment_modality,
  p_professional_slug text default null,
  p_days integer default 60
) returns integer
language plpgsql security definer set search_path=public,extensions as $$
declare
  created_count integer := 0;
begin
  insert into public.appointment_slots(professional_id, service_id, modality, starts_at, ends_at)
  select p.id, s.id, p_modality,
    (slot_local at time zone 'America/Sao_Paulo'),
    ((slot_local + make_interval(mins => s.duration_minutes)) at time zone 'America/Sao_Paulo')
  from public.services s
  join public.professional_services ps on ps.service_id=s.id and ps.modality=p_modality and ps.active
  join public.professionals p on p.id=ps.professional_id and p.active
  join public.availability_rules r on r.professional_id=p.id and r.modality=p_modality and r.active
  cross join generate_series(current_date, current_date + least(p_days,120), interval '1 day') d
  cross join lateral generate_series(
    d::date + r.starts_at,
    d::date + r.ends_at - make_interval(mins => s.duration_minutes),
    make_interval(mins => s.duration_minutes + s.buffer_minutes)
  ) slot_local
  where s.slug=p_service_slug
    and (p_professional_slug is null or p_professional_slug='first-available' or p.slug=p_professional_slug)
    and extract(dow from d)::smallint=r.weekday
    and not exists (
      select 1 from public.schedule_exceptions e
      where (e.professional_id is null or e.professional_id=p.id)
        and (e.modality is null or e.modality=p_modality)
        and tstzrange(e.starts_at,e.ends_at,'[)') && tstzrange(
          (slot_local at time zone 'America/Sao_Paulo'),
          ((slot_local+make_interval(mins=>s.duration_minutes)) at time zone 'America/Sao_Paulo'),'[)')
    )
  on conflict (professional_id,service_id,modality,starts_at) do nothing;
  get diagnostics created_count = row_count;
  return created_count;
end $$;

drop view if exists public.available_slots;
create view public.available_slots with (security_invoker=true) as
select sl.id, sl.starts_at, sl.ends_at, sl.modality,
       p.slug professional_slug, p.name professional_name,
       sv.slug service_slug, sv.name service_name
from public.appointment_slots sl
join public.professionals p on p.id=sl.professional_id and p.active
join public.services sv on sv.id=sl.service_id and sv.active
where sl.active and sl.starts_at>now()
  and not exists (
    select 1 from public.appointments a
    where a.professional_id=sl.professional_id
      and a.status in ('pending','confirmed')
      and tstzrange(a.starts_at,a.ends_at,'[)') && tstzrange(sl.starts_at,sl.ends_at,'[)')
  );

revoke all on function public.generate_appointment_slots(text,public.appointment_modality,text,integer) from public,anon,authenticated;
grant execute on function public.generate_appointment_slots(text,public.appointment_modality,text,integer) to service_role;

create or replace function public.create_recurring_appointment(
  p_professional_id uuid, p_service_id uuid, p_modality public.appointment_modality,
  p_patient_name text, p_responsible_name text, p_phone text, p_email text,
  p_starts_on date, p_ends_on date, p_local_start_time time,
  p_interval_days integer, p_duration_minutes integer, p_created_by uuid
) returns uuid
language plpgsql security definer set search_path=public,extensions as $$
declare
  series_id uuid;
  occurrence_date date;
  occurrence_start timestamptz;
  occurrence_end timestamptz;
  generated_slot_id uuid;
begin
  if p_ends_on < p_starts_on or p_ends_on > p_starts_on + 366 or p_interval_days < 1 then
    raise exception 'invalid_recurrence';
  end if;

  insert into public.recurring_appointments(
    professional_id,service_id,modality,patient_name,responsible_name,phone,email,
    starts_on,ends_on,local_start_time,interval_days,duration_minutes,created_by
  ) values (
    p_professional_id,p_service_id,p_modality,trim(p_patient_name),nullif(trim(p_responsible_name),''),
    trim(p_phone),lower(trim(p_email)),p_starts_on,p_ends_on,p_local_start_time,
    p_interval_days,p_duration_minutes,p_created_by
  ) returning id into series_id;

  occurrence_date := p_starts_on;
  while occurrence_date <= p_ends_on loop
    occurrence_start := ((occurrence_date + p_local_start_time) at time zone 'America/Sao_Paulo');
    occurrence_end := occurrence_start + make_interval(mins=>p_duration_minutes);
    if exists(select 1 from public.schedule_exceptions e where (e.professional_id is null or e.professional_id=p_professional_id) and (e.modality is null or e.modality=p_modality) and tstzrange(e.starts_at,e.ends_at,'[)') && tstzrange(occurrence_start,occurrence_end,'[)'))
      or exists(select 1 from public.appointments a where a.professional_id=p_professional_id and a.status in ('pending','confirmed') and tstzrange(a.starts_at,a.ends_at,'[)') && tstzrange(occurrence_start,occurrence_end,'[)')) then
      raise exception 'recurrence_conflict_on_%', occurrence_date;
    end if;

    insert into public.appointment_slots(professional_id,service_id,modality,starts_at,ends_at)
    values(p_professional_id,p_service_id,p_modality,occurrence_start,occurrence_end)
    on conflict (professional_id,service_id,modality,starts_at)
    do update set active=true,ends_at=excluded.ends_at returning id into generated_slot_id;

    insert into public.appointments(
      slot_id,professional_id,service_id,modality,starts_at,ends_at,status,
      patient_name,responsible_name,phone,email,cancellation_token_hash,recurring_appointment_id
    ) values (
      generated_slot_id,p_professional_id,p_service_id,p_modality,occurrence_start,occurrence_end,'confirmed',
      trim(p_patient_name),nullif(trim(p_responsible_name),''),trim(p_phone),lower(trim(p_email)),
      encode(digest(gen_random_uuid()::text,'sha256'),'hex'),series_id
    );
    occurrence_date := occurrence_date + p_interval_days;
  end loop;
  return series_id;
end $$;

revoke all on function public.create_recurring_appointment(uuid,uuid,public.appointment_modality,text,text,text,text,date,date,time,integer,integer,uuid) from public,anon,authenticated;
grant execute on function public.create_recurring_appointment(uuid,uuid,public.appointment_modality,text,text,text,text,date,date,time,integer,integer,uuid) to service_role;
