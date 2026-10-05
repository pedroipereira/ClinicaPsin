-- O Supabase instala pgcrypto no schema extensions. A migração 003 já pode
-- ter sido executada, portanto ajustamos a função existente sem recriá-la.
alter function public.create_recurring_appointment(
  uuid, uuid, public.appointment_modality,
  text, text, text, text,
  date, date, time,
  integer, integer, uuid
) set search_path = public, extensions;
