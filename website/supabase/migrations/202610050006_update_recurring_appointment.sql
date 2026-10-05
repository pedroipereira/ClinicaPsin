create or replace function public.update_recurring_appointment(
  p_recurrence_id uuid, p_service_id uuid, p_modality public.appointment_modality,
  p_starts_on date, p_ends_on date, p_local_start_time time,
  p_interval_days integer, p_duration_minutes integer
) returns uuid
language plpgsql security definer set search_path=public,extensions as $$
declare
  series public.recurring_appointments%rowtype;
  occurrence_date date;
  occurrence_start timestamptz;
  occurrence_end timestamptz;
  generated_slot_id uuid;
begin
  select * into series from public.recurring_appointments where id=p_recurrence_id and active=true for update;
  if not found then raise exception 'recurrence_not_found'; end if;
  if p_ends_on < p_starts_on or p_ends_on > p_starts_on + 366 or p_interval_days < 1 then raise exception 'invalid_recurrence'; end if;

  delete from public.appointments where recurring_appointment_id=p_recurrence_id and starts_at>=now();
  update public.recurring_appointments set service_id=p_service_id,modality=p_modality,starts_on=p_starts_on,ends_on=p_ends_on,
    local_start_time=p_local_start_time,interval_days=p_interval_days,duration_minutes=p_duration_minutes where id=p_recurrence_id;

  occurrence_date:=p_starts_on;
  while occurrence_date<=p_ends_on loop
    if occurrence_date>=current_date then
      occurrence_start:=((occurrence_date+p_local_start_time) at time zone 'America/Sao_Paulo');
      occurrence_end:=occurrence_start+make_interval(mins=>p_duration_minutes);
      if exists(select 1 from public.schedule_exceptions e where (e.professional_id is null or e.professional_id=series.professional_id) and (e.modality is null or e.modality=p_modality) and tstzrange(e.starts_at,e.ends_at,'[)')&&tstzrange(occurrence_start,occurrence_end,'[)'))
        or exists(select 1 from public.appointments a where a.professional_id=series.professional_id and a.status in ('pending','confirmed') and tstzrange(a.starts_at,a.ends_at,'[)')&&tstzrange(occurrence_start,occurrence_end,'[)')) then
        raise exception 'recurrence_conflict_on_%',occurrence_date;
      end if;
      insert into public.appointment_slots(professional_id,service_id,modality,starts_at,ends_at)
      values(series.professional_id,p_service_id,p_modality,occurrence_start,occurrence_end)
      on conflict(professional_id,service_id,modality,starts_at) do update set active=true,ends_at=excluded.ends_at returning id into generated_slot_id;
      insert into public.appointments(slot_id,professional_id,service_id,modality,starts_at,ends_at,status,patient_name,responsible_name,phone,email,cancellation_token_hash,recurring_appointment_id)
      values(generated_slot_id,series.professional_id,p_service_id,p_modality,occurrence_start,occurrence_end,'confirmed',series.patient_name,series.responsible_name,series.phone,series.email,encode(digest(gen_random_uuid()::text,'sha256'),'hex'),p_recurrence_id);
    end if;
    occurrence_date:=occurrence_date+p_interval_days;
  end loop;
  return p_recurrence_id;
end $$;

revoke all on function public.update_recurring_appointment(uuid,uuid,public.appointment_modality,date,date,time,integer,integer) from public,anon,authenticated;
grant execute on function public.update_recurring_appointment(uuid,uuid,public.appointment_modality,date,date,time,integer,integer) to service_role;
