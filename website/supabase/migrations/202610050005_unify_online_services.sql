-- A modalidade já é escolhida separadamente. Mantemos um único serviço de
-- psicoterapia e uma única primeira consulta, disponíveis nas duas modalidades.
insert into public.professional_services(professional_id,service_id,modality,active)
select ps.professional_id,base.id,'online',true
from public.professional_services ps
join public.services legacy on legacy.id=ps.service_id
join public.services base on base.slug=case
  when legacy.slug='teleconsulta' then 'primeira-psicologia'
  when legacy.slug='psicoterapia-online' then 'psicoterapia'
end
where legacy.slug in ('teleconsulta','psicoterapia-online')
on conflict(professional_id,service_id,modality) do update set active=true;

update public.services
set active=false
where slug in ('teleconsulta','psicoterapia-online');

-- Nesta versão, os mesmos serviços são oferecidos nas duas modalidades. A
-- disponibilidade de horários continua sendo definida por cada profissional.
insert into public.professional_services(professional_id,service_id,modality,active)
select professional_id,service_id,'online',true
from public.professional_services
where modality='presencial' and active
on conflict(professional_id,service_id,modality) do update set active=true;
