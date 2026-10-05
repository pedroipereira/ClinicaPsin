-- PSIN CLÍNICA — LIMPEZA OPERACIONAL E CARGA DE DEMONSTRAÇÃO
-- Todos os nomes, telefones e e-mails abaixo são fictícios.
-- Preserva: auth.users, staff_profiles, professionals, services e professional_services.
-- Remove: consultas, eventos, recorrências, horários, disponibilidades e ausências.

begin;

truncate table
  public.appointment_events,
  public.appointments,
  public.recurring_appointments,
  public.appointment_slots,
  public.schedule_exceptions,
  public.availability_rules
restart identity cascade;

-- Agenda semanal. O exemplo da Allice demonstra dois intervalos no mesmo dia.
insert into public.availability_rules(professional_id,weekday,starts_at,ends_at,modality)
select p.id,x.weekday,x.starts_at,x.ends_at,x.modality::public.appointment_modality
from (values
  ('allice',1,'08:00'::time,'12:00'::time,'presencial'),
  ('allice',1,'14:00'::time,'18:00'::time,'presencial'),
  ('allice',2,'09:00'::time,'12:00'::time,'online'),
  ('allice',3,'08:00'::time,'12:00'::time,'presencial'),
  ('allice',3,'14:00'::time,'18:00'::time,'presencial'),
  ('allice',4,'14:00'::time,'18:00'::time,'online'),
  ('sandson',2,'08:00'::time,'12:00'::time,'presencial'),
  ('sandson',2,'14:00'::time,'18:00'::time,'online'),
  ('sandson',4,'08:00'::time,'12:00'::time,'presencial'),
  ('emanuele',1,'13:00'::time,'18:00'::time,'online'),
  ('emanuele',3,'13:00'::time,'18:00'::time,'presencial'),
  ('emanuele',5,'08:00'::time,'12:00'::time,'presencial'),
  ('suely',2,'13:00'::time,'18:00'::time,'presencial'),
  ('suely',4,'13:00'::time,'18:00'::time,'online')
) as x(professional_slug,weekday,starts_at,ends_at,modality)
join public.professionals p on p.slug=x.professional_slug;

-- Acompanhamentos recorrentes ativos.
select public.create_recurring_appointment(
  p.id,s.id,'presencial','Ana Clara Martins','Juliana Martins','61900000001','ana.clara@example.com',
  current_date+1,current_date+92,'15:00',7,s.duration_minutes,null
) from public.professionals p cross join public.services s
where p.slug='allice' and s.slug='psicologia-infantil';

select public.create_recurring_appointment(
  p.id,s.id,'online','Marina Oliveira',null,'61900000002','marina.oliveira@example.com',
  current_date+2,current_date+100,'17:00',14,s.duration_minutes,null
) from public.professionals p cross join public.services s
where p.slug='allice' and s.slug='psicoterapia';

select public.create_recurring_appointment(
  p.id,s.id,'presencial','Rafael Costa',null,'61900000003','rafael.costa@example.com',
  current_date+1,current_date+92,'10:00',7,s.duration_minutes,null
) from public.professionals p cross join public.services s
where p.slug='sandson' and s.slug='psicoterapia';

select public.create_recurring_appointment(
  p.id,s.id,'online','Beatriz Nunes',null,'61900000004','beatriz.nunes@example.com',
  current_date+3,current_date+101,'16:00',14,s.duration_minutes,null
) from public.professionals p cross join public.services s
where p.slug='emanuele' and s.slug='psicoterapia';

select public.create_recurring_appointment(
  p.id,s.id,'presencial','Helena Ribeiro',null,'61900000005','helena.ribeiro@example.com',
  current_date+2,current_date+93,'14:00',7,s.duration_minutes,null
) from public.professionals p cross join public.services s
where p.slug='suely' and s.slug='primeira-psicanalise';

-- Consultas avulsas próximas: duas confirmadas e uma aguardando confirmação.
with demo as (
  select * from (values
    ('allice','primeira-psicologia','presencial',date_trunc('hour',now()+interval '1 hour'),'confirmed'::public.appointment_status,'Lucas Almeida',null,'61900000011','lucas.almeida@example.com'),
    ('sandson','psicoterapia','online',date_trunc('hour',now()+interval '2 hours'),'pending'::public.appointment_status,'Camila Ferreira',null,'61900000012','camila.ferreira@example.com'),
    ('emanuele','primeira-psicologia','presencial',date_trunc('hour',now()+interval '3 hours'),'confirmed'::public.appointment_status,'Gabriel Santos',null,'61900000013','gabriel.santos@example.com')
  ) x(professional_slug,service_slug,modality,starts_at,status,patient_name,responsible_name,phone,email)
), inserted_slots as (
  insert into public.appointment_slots(professional_id,service_id,modality,starts_at,ends_at)
  select p.id,s.id,d.modality::public.appointment_modality,d.starts_at,d.starts_at+make_interval(mins=>s.duration_minutes)
  from demo d join public.professionals p on p.slug=d.professional_slug join public.services s on s.slug=d.service_slug
  returning id,professional_id,service_id,modality,starts_at,ends_at
)
insert into public.appointments(slot_id,professional_id,service_id,modality,starts_at,ends_at,status,patient_name,responsible_name,phone,email,cancellation_token_hash)
select sl.id,sl.professional_id,sl.service_id,sl.modality,sl.starts_at,sl.ends_at,d.status,d.patient_name,d.responsible_name,d.phone,d.email,
       encode(digest(gen_random_uuid()::text,'sha256'),'hex')
from inserted_slots sl join demo d on d.starts_at=sl.starts_at
join public.professionals p on p.id=sl.professional_id and p.slug=d.professional_slug;

-- Exemplo histórico cancelado pela profissional com motivo para a automação.
with data as (
  select p.id professional_id,s.id service_id,s.duration_minutes,
         date_trunc('hour',now()-interval '2 days') starts_at
  from public.professionals p cross join public.services s
  where p.slug='allice' and s.slug='psicoterapia'
), slot as (
  insert into public.appointment_slots(professional_id,service_id,modality,starts_at,ends_at,active)
  select professional_id,service_id,'presencial',starts_at,starts_at+make_interval(mins=>duration_minutes),false from data
  returning *
), appointment as (
  insert into public.appointments(slot_id,professional_id,service_id,modality,starts_at,ends_at,status,patient_name,phone,email,cancellation_token_hash)
  select id,professional_id,service_id,modality,starts_at,ends_at,'cancelled','João Pereira','61900000014','joao.pereira@example.com',encode(digest(gen_random_uuid()::text,'sha256'),'hex') from slot
  returning id
)
insert into public.appointment_events(appointment_id,event_type,metadata)
select id,'cancelled',jsonb_build_object('cancellation_reason','Imprevisto pessoal da profissional','staff_role','professional','demo',true) from appointment;

-- Férias futuras e uma ausência pontual em horário específico.
insert into public.schedule_exceptions(professional_id,starts_at,ends_at,kind,action,internal_note)
select p.id,(current_date+35)::timestamp at time zone 'America/Sao_Paulo',(current_date+43)::timestamp at time zone 'America/Sao_Paulo','vacation','reschedule','Férias programadas — demonstração'
from public.professionals p where p.slug='allice';

insert into public.schedule_exceptions(professional_id,starts_at,ends_at,kind,action,internal_note)
select p.id,((current_date+8)+time '14:00') at time zone 'America/Sao_Paulo',((current_date+8)+time '16:00') at time zone 'America/Sao_Paulo','course','block_only','Curso de atualização — demonstração'
from public.professionals p where p.slug='emanuele';

-- Gera horários livres para os próximos 45 dias a partir das regras semanais.
do $$
declare item record;
begin
  for item in
    select distinct s.slug service_slug,ps.modality,p.slug professional_slug
    from public.professional_services ps
    join public.professionals p on p.id=ps.professional_id and p.active
    join public.services s on s.id=ps.service_id and s.active
    where ps.active
  loop
    perform public.generate_appointment_slots(item.service_slug,item.modality,item.professional_slug,45);
  end loop;
end $$;

-- Eventos de criação tornam o histórico da demonstração mais realista.
insert into public.appointment_events(appointment_id,event_type,metadata)
select a.id,'created',jsonb_build_object('source','demo_seed')
from public.appointments a
where not exists(select 1 from public.appointment_events e where e.appointment_id=a.id);

commit;

-- Conferência rápida após a execução.
select 'profissionais' item,count(*) total from public.professionals where active
union all select 'acompanhamentos ativos',count(*) from public.recurring_appointments where active
union all select 'consultas futuras',count(*) from public.appointments where starts_at>=now() and status in ('pending','confirmed')
union all select 'horários disponíveis',count(*) from public.available_slots
union all select 'ausências futuras',count(*) from public.schedule_exceptions where ends_at>=now();
