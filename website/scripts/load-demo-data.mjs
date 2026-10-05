import { createClient } from "@supabase/supabase-js";
import { createHash, randomUUID } from "node:crypto";

const url=process.env.NEXT_PUBLIC_SUPABASE_URL;
const key=process.env.SUPABASE_SERVICE_ROLE_KEY;
if(!url||!key)throw new Error("Variáveis do Supabase ausentes.");
const db=createClient(url,key,{auth:{persistSession:false,autoRefreshToken:false}});
const check=(result,label)=>{if(result.error)throw new Error(`${label}: ${result.error.message}`);return result.data};
const hash=()=>createHash("sha256").update(randomUUID()).digest("hex");
const localDate=(offset=0)=>{const d=new Date();d.setDate(d.getDate()+offset);return d.toLocaleDateString("en-CA",{timeZone:"America/Sao_Paulo"})};
const localIso=(offset,time)=>new Date(`${localDate(offset)}T${time}:00-03:00`).toISOString();

for(const table of ["appointment_events","appointments","recurring_appointments","appointment_slots","schedule_exceptions","availability_rules"]){
  check(await db.from(table).delete().not("id","is",null),`limpeza de ${table}`);
}

const professionals=check(await db.from("professionals").select("id,slug").eq("active",true),"profissionais");
const services=check(await db.from("services").select("id,slug,duration_minutes").eq("active",true),"serviços");
const professionalServices=check(await db.from("professional_services").select("professional_id,service_id,modality,active").eq("active",true),"vínculos");
const p=Object.fromEntries(professionals.map(item=>[item.slug,item]));
const s=Object.fromEntries(services.map(item=>[item.slug,item]));

const rules=[
 ["allice",1,"08:00","12:00","presencial"],["allice",1,"14:00","18:00","presencial"],["allice",2,"09:00","12:00","online"],["allice",3,"08:00","12:00","presencial"],["allice",3,"14:00","18:00","presencial"],["allice",4,"14:00","18:00","online"],
 ["sandson",2,"08:00","12:00","presencial"],["sandson",2,"14:00","18:00","online"],["sandson",4,"08:00","12:00","presencial"],
 ["emanuele",1,"13:00","18:00","online"],["emanuele",3,"13:00","18:00","presencial"],["emanuele",5,"08:00","12:00","presencial"],
 ["suely",2,"13:00","18:00","presencial"],["suely",4,"13:00","18:00","online"],
].map(([slug,weekday,starts_at,ends_at,modality])=>({professional_id:p[slug].id,weekday,starts_at,ends_at,modality}));
check(await db.from("availability_rules").insert(rules),"agenda semanal");

const recurrences=[
 ["allice","psicologia-infantil","presencial","Ana Clara Martins","Juliana Martins","61900000001","ana.clara@example.com",1,92,"15:00",7],
 ["allice","psicoterapia","online","Marina Oliveira",null,"61900000002","marina.oliveira@example.com",2,100,"17:00",14],
 ["sandson","psicoterapia","presencial","Rafael Costa",null,"61900000003","rafael.costa@example.com",1,92,"10:00",7],
 ["emanuele","psicoterapia","online","Beatriz Nunes",null,"61900000004","beatriz.nunes@example.com",3,101,"16:00",14],
 ["suely","primeira-psicanalise","presencial","Helena Ribeiro",null,"61900000005","helena.ribeiro@example.com",2,93,"14:00",7],
];
for(const [professionalSlug,serviceSlug,modality,patient,responsible,phone,email,startOffset,endOffset,time,interval] of recurrences){
  check(await db.rpc("create_recurring_appointment",{p_professional_id:p[professionalSlug].id,p_service_id:s[serviceSlug].id,p_modality:modality,p_patient_name:patient,p_responsible_name:responsible,p_phone:phone,p_email:email,p_starts_on:localDate(startOffset),p_ends_on:localDate(endOffset),p_local_start_time:time,p_interval_days:interval,p_duration_minutes:s[serviceSlug].duration_minutes,p_created_by:null}),`acompanhamento de ${patient}`);
}

const base=new Date();base.setMinutes(0,0,0);base.setHours(base.getHours()+1);
const oneOff=[
 ["allice","primeira-psicologia","presencial",0,"confirmed","Lucas Almeida",null,"61900000011","lucas.almeida@example.com"],
 ["sandson","psicoterapia","online",1,"pending","Camila Ferreira",null,"61900000012","camila.ferreira@example.com"],
 ["emanuele","primeira-psicologia","presencial",2,"confirmed","Gabriel Santos",null,"61900000013","gabriel.santos@example.com"],
];
for(const [professionalSlug,serviceSlug,modality,hours,status,patient,responsible,phone,email] of oneOff){
  const starts=new Date(base.getTime()+hours*3600000);const ends=new Date(starts.getTime()+s[serviceSlug].duration_minutes*60000);
  const slot=check(await db.from("appointment_slots").insert({professional_id:p[professionalSlug].id,service_id:s[serviceSlug].id,modality,starts_at:starts.toISOString(),ends_at:ends.toISOString()}).select("id").single(),`horário de ${patient}`);
  const appointment=check(await db.from("appointments").insert({slot_id:slot.id,professional_id:p[professionalSlug].id,service_id:s[serviceSlug].id,modality,starts_at:starts.toISOString(),ends_at:ends.toISOString(),status,patient_name:patient,responsible_name:responsible,phone,email,cancellation_token_hash:hash()}).select("id").single(),`consulta de ${patient}`);
  check(await db.from("appointment_events").insert({appointment_id:appointment.id,event_type:"created",metadata:{source:"demo_seed"}}),`evento de ${patient}`);
}

const cancelledStart=new Date(Date.now()-2*86400000);cancelledStart.setMinutes(0,0,0);const cancelledEnd=new Date(cancelledStart.getTime()+s.psicoterapia.duration_minutes*60000);
const cancelledSlot=check(await db.from("appointment_slots").insert({professional_id:p.allice.id,service_id:s.psicoterapia.id,modality:"presencial",starts_at:cancelledStart.toISOString(),ends_at:cancelledEnd.toISOString(),active:false}).select("id").single(),"horário cancelado");
const cancelled=check(await db.from("appointments").insert({slot_id:cancelledSlot.id,professional_id:p.allice.id,service_id:s.psicoterapia.id,modality:"presencial",starts_at:cancelledStart.toISOString(),ends_at:cancelledEnd.toISOString(),status:"cancelled",patient_name:"João Pereira",phone:"61900000014",email:"joao.pereira@example.com",cancellation_token_hash:hash()}).select("id").single(),"consulta cancelada");
check(await db.from("appointment_events").insert({appointment_id:cancelled.id,event_type:"cancelled",metadata:{cancellation_reason:"Imprevisto pessoal da profissional",staff_role:"professional",demo:true}}),"evento cancelado");

check(await db.from("schedule_exceptions").insert([
 {professional_id:p.allice.id,starts_at:localIso(35,"00:00"),ends_at:localIso(43,"00:00"),kind:"vacation",action:"reschedule",internal_note:"Férias programadas — demonstração"},
 {professional_id:p.emanuele.id,starts_at:localIso(8,"14:00"),ends_at:localIso(8,"16:00"),kind:"course",action:"block_only",internal_note:"Curso de atualização — demonstração"},
]),"ausências");

for(const relation of professionalServices){
  const professional=professionals.find(item=>item.id===relation.professional_id);const service=services.find(item=>item.id===relation.service_id);
  if(professional&&service)check(await db.rpc("generate_appointment_slots",{p_service_slug:service.slug,p_modality:relation.modality,p_professional_slug:professional.slug,p_days:45}),`horários ${professional.slug}/${service.slug}`);
}

const counts={};
for(const [label,table,filter] of [["acompanhamentos","recurring_appointments",["active",true]],["consultas","appointments",null],["horários","appointment_slots",["active",true]],["ausências","schedule_exceptions",null]]){
  let query=db.from(table).select("id",{count:"exact",head:true});if(filter)query=query.eq(filter[0],filter[1]);const result=await query;check(result,`contagem de ${label}`);counts[label]=result.count;
}
console.log(JSON.stringify(counts));
