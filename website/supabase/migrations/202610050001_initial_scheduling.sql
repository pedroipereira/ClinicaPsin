create extension if not exists pgcrypto;

create type public.appointment_modality as enum ('presencial', 'online');
create type public.appointment_status as enum ('pending', 'confirmed', 'cancelled');

create table public.professionals (
  id uuid primary key default gen_random_uuid(),
  slug text not null unique,
  name text not null,
  role text not null,
  active boolean not null default true,
  created_at timestamptz not null default now()
);

create table public.services (
  id uuid primary key default gen_random_uuid(),
  slug text not null unique,
  name text not null,
  duration_minutes integer not null check (duration_minutes between 20 and 240),
  active boolean not null default true,
  created_at timestamptz not null default now()
);

create table public.professional_services (
  professional_id uuid not null references public.professionals on delete cascade,
  service_id uuid not null references public.services on delete cascade,
  modality public.appointment_modality not null,
  active boolean not null default true,
  primary key (professional_id, service_id, modality)
);

create table public.appointment_slots (
  id uuid primary key default gen_random_uuid(),
  professional_id uuid not null references public.professionals on delete cascade,
  service_id uuid not null references public.services on delete cascade,
  modality public.appointment_modality not null,
  starts_at timestamptz not null,
  ends_at timestamptz not null,
  active boolean not null default true,
  created_at timestamptz not null default now(),
  constraint slot_valid_interval check (ends_at > starts_at),
  constraint slot_professional_start_unique unique (professional_id, starts_at)
);

create table public.appointments (
  id uuid primary key default gen_random_uuid(),
  slot_id uuid not null references public.appointment_slots,
  professional_id uuid not null references public.professionals,
  service_id uuid not null references public.services,
  modality public.appointment_modality not null,
  starts_at timestamptz not null,
  ends_at timestamptz not null,
  status public.appointment_status not null default 'confirmed',
  patient_name text not null,
  responsible_name text,
  phone text not null,
  email text not null,
  privacy_accepted_at timestamptz not null default now(),
  cancellation_token_hash text not null unique,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create unique index one_active_appointment_per_slot
  on public.appointments (slot_id)
  where status in ('pending', 'confirmed');

create table public.appointment_events (
  id bigint generated always as identity primary key,
  appointment_id uuid not null references public.appointments on delete cascade,
  event_type text not null,
  metadata jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now()
);

create view public.available_slots with (security_invoker = true) as
select s.id, s.starts_at, s.ends_at, s.modality,
       p.slug as professional_slug, p.name as professional_name,
       sv.slug as service_slug, sv.name as service_name
from public.appointment_slots s
join public.professionals p on p.id = s.professional_id and p.active
join public.services sv on sv.id = s.service_id and sv.active
where s.active
  and not exists (
    select 1 from public.appointments a
    where a.slot_id = s.id and a.status in ('pending', 'confirmed')
  );

create or replace function public.book_appointment(
  p_slot_id uuid,
  p_patient_name text,
  p_responsible_name text,
  p_phone text,
  p_email text,
  p_cancellation_token_hash text
) returns uuid
language plpgsql
security definer
set search_path = public
as $$
declare
  chosen_slot public.appointment_slots%rowtype;
  new_id uuid;
begin
  select * into chosen_slot from public.appointment_slots
  where id = p_slot_id and active and starts_at > now()
  for update;

  if not found or exists (
    select 1 from public.appointments
    where slot_id = p_slot_id and status in ('pending', 'confirmed')
  ) then
    raise exception 'slot_unavailable';
  end if;

  insert into public.appointments (
    slot_id, professional_id, service_id, modality, starts_at, ends_at,
    patient_name, responsible_name, phone, email, cancellation_token_hash
  ) values (
    chosen_slot.id, chosen_slot.professional_id, chosen_slot.service_id,
    chosen_slot.modality, chosen_slot.starts_at, chosen_slot.ends_at,
    trim(p_patient_name), nullif(trim(p_responsible_name), ''), trim(p_phone),
    lower(trim(p_email)), p_cancellation_token_hash
  ) returning id into new_id;

  insert into public.appointment_events (appointment_id, event_type)
  values (new_id, 'created');
  return new_id;
end;
$$;

alter table public.professionals enable row level security;
alter table public.services enable row level security;
alter table public.professional_services enable row level security;
alter table public.appointment_slots enable row level security;
alter table public.appointments enable row level security;
alter table public.appointment_events enable row level security;

revoke all on public.appointments, public.appointment_events from anon, authenticated;
revoke all on function public.book_appointment(uuid,text,text,text,text,text) from public, anon, authenticated;
grant execute on function public.book_appointment(uuid,text,text,text,text,text) to service_role;

insert into public.professionals (slug, name, role) values
  ('allice', 'Allice Gracyelli de Melo', 'Psicóloga'),
  ('sandson', 'Sandson Barbosa Azevedo Junior', 'Psicólogo'),
  ('emanuele', 'Emanuele Martins Carlos de Souza', 'Psicóloga'),
  ('suely', 'Suely P. de Melo', 'Psicanalista clínica');

insert into public.services (slug, name, duration_minutes) values
  ('primeira-psicologia', 'Primeira consulta de psicologia', 50),
  ('primeira-psicanalise', 'Primeira consulta de psicanálise', 50),
  ('psicoterapia', 'Psicoterapia', 50),
  ('psicologia-infantil', 'Psicologia infantil', 50),
  ('teleconsulta', 'Teleconsulta', 50),
  ('psicoterapia-online', 'Psicoterapia online', 50);

-- Serviços, duração e vínculos são uma carga inicial e devem ser confirmados pela clínica.
insert into public.professional_services (professional_id, service_id, modality)
select p.id, s.id, x.modality::public.appointment_modality
from (values
  ('allice','primeira-psicologia','presencial'), ('allice','psicoterapia','presencial'),
  ('allice','psicologia-infantil','presencial'), ('allice','teleconsulta','online'),
  ('allice','psicoterapia-online','online'), ('sandson','primeira-psicologia','presencial'),
  ('sandson','psicoterapia','presencial'), ('sandson','teleconsulta','online'),
  ('sandson','psicoterapia-online','online'), ('emanuele','primeira-psicologia','presencial'),
  ('emanuele','psicoterapia','presencial'), ('emanuele','teleconsulta','online'),
  ('emanuele','psicoterapia-online','online'), ('suely','primeira-psicanalise','presencial'),
  ('suely','teleconsulta','online')
) as x(professional_slug, service_slug, modality)
join public.professionals p on p.slug = x.professional_slug
join public.services s on s.slug = x.service_slug;
