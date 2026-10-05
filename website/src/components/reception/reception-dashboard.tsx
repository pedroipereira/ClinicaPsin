"use client";

import { FormEvent,useCallback,useEffect,useMemo,useState } from "react";
import type { Session,SupabaseClient } from "@supabase/supabase-js";
import { createPublicClient } from "@/lib/supabase/browser";

type Named={name:string};
type Appointment={id:string;starts_at:string;ends_at:string;status:"pending"|"confirmed"|"cancelled";patient_name:string;responsible_name:string|null;phone:string;email:string;recurring_appointment_id:string|null;professionals:Named|null;services:Named|null};
type Slot={id:string;starts_at:string;ends_at:string;active:boolean;professionals:Named|null;services:Named|null};
type Recurrence={id:string;patient_name:string;starts_on:string;ends_on:string;local_start_time:string;interval_days:number;modality:string;professionals:Named|null;services:Named|null};
type CatalogItem={id:string;name:string;duration_minutes?:number};
type Agenda={staff:{name:string;role:string};appointments:Appointment[];upcoming:Appointment[];slots:Slot[];recurrences:Recurrence[];professionals:CatalogItem[];services:CatalogItem[];updatedAt:string};

export function ReceptionDashboard(){
  const client=useMemo(()=>createPublicClient("reception"),[]);
  const [session,setSession]=useState<Session|null>(null);
  const [loading,setLoading]=useState(Boolean(client));
  useEffect(()=>{if(!client)return;client.auth.getSession().then(({data})=>{setSession(data.session);setLoading(false)});const {data}=client.auth.onAuthStateChange((_event,next)=>setSession(next));return()=>data.subscription.unsubscribe()},[client]);
  if(!client)return <SetupNotice/>;
  if(loading)return <Panel>Carregando acesso…</Panel>;
  if(!session)return <Login client={client}/>;
  return <AgendaView client={client} session={session}/>;
}

function Login({client}:{client:SupabaseClient}){
  const [message,setMessage]=useState("");
  const [sending,setSending]=useState(false);
  async function login(event:FormEvent<HTMLFormElement>){event.preventDefault();const form=new FormData(event.currentTarget);setSending(true);const {error}=await client.auth.signInWithPassword({email:String(form.get("email")),password:String(form.get("password"))});setMessage(error?"E-mail ou senha inválidos.":"");setSending(false)}
  return <div className="mx-auto max-w-md rounded-[2rem] border border-[var(--line)] bg-white p-8 shadow-[0_24px_80px_rgba(79,77,78,.06)]"><p className="eyebrow">ACESSO PROTEGIDO</p><h1 className="mt-4 font-serif text-4xl">Entrar na recepção.</h1><p className="mt-3 leading-7 text-[var(--muted)]">Use a conta cadastrada pela administração da clínica.</p><form className="mt-8 grid gap-5" onSubmit={login}><Field name="email" label="E-mail" type="email" required/><Field name="password" label="Senha" type="password" required/>{message&&<p className="rounded-2xl bg-[var(--pink-soft)] p-4 text-sm">{message}</p>}<button className="button button-neutral" disabled={sending}>{sending?"Entrando…":"Entrar"}</button></form></div>;
}

function AgendaView({client,session}:{client:SupabaseClient;session:Session}){
  const [date,setDate]=useState(new Date().toLocaleDateString("en-CA",{timeZone:"America/Sao_Paulo"}));
  const [agenda,setAgenda]=useState<Agenda|null>(null);
  const [message,setMessage]=useState("");
  const [refreshing,setRefreshing]=useState(false);
  const [showAllRecurrences,setShowAllRecurrences]=useState(false);

  const load=useCallback(async(silent=false)=>{if(!silent)setRefreshing(true);const response=await fetch(`/api/admin/agenda?date=${date}`,{headers:{Authorization:`Bearer ${session.access_token}`}});const payload=await response.json();if(response.ok){setAgenda(payload);if(!silent)setMessage("")}else setMessage(payload.error);setRefreshing(false)},[date,session.access_token]);
  useEffect(()=>{void fetch(`/api/admin/agenda?date=${date}`,{headers:{Authorization:`Bearer ${session.access_token}`}}).then(async response=>({response,payload:await response.json()})).then(({response,payload})=>{if(response.ok){setAgenda(payload);setMessage("")}else setMessage(payload.error)})},[date,session.access_token]);
  useEffect(()=>{const onFocus=()=>void load(true);const timer=window.setInterval(()=>void load(true),10000);window.addEventListener("focus",onFocus);return()=>{window.clearInterval(timer);window.removeEventListener("focus",onFocus)}},[load]);

  async function confirmAppointment(id:string){const response=await fetch(`/api/admin/appointments/${id}`,{method:"PATCH",headers:{Authorization:`Bearer ${session.access_token}`,"Content-Type":"application/json"},body:JSON.stringify({status:"confirmed"})});const payload=await response.json();setMessage(response.ok?"Atendimento confirmado.":payload.error);if(response.ok)await load(true)}
  const busySlotIds=new Set(agenda?.appointments.filter(item=>item.status!=="cancelled").map(item=>`${item.starts_at}|${item.professionals?.name}`));
  const available=agenda?.slots.filter(item=>!busySlotIds.has(`${item.starts_at}|${item.professionals?.name}`))??[];
  const pendingToday=agenda?.appointments.filter(item=>item.status==="pending").length??0;
  const confirmedToday=agenda?.appointments.filter(item=>item.status==="confirmed").length??0;

  return <div>
    <div className="flex flex-col gap-5 sm:flex-row sm:items-end sm:justify-between"><div><p className="eyebrow">AGENDA DA CLÍNICA</p><h1 className="mt-3 font-serif text-5xl">Olá, {agenda?.staff.name??"recepção"}.</h1><p className="mt-3 text-sm text-[var(--muted)]">Atualização automática a cada 10 segundos{agenda?.updatedAt?` · última atualização às ${formatTime(agenda.updatedAt)}`:""}.</p></div><div className="flex flex-wrap items-end gap-3"><label className="grid gap-2 text-sm font-semibold">Dia<input className="rounded-xl border border-[var(--line)] bg-white px-4 py-3" type="date" value={date} onChange={event=>setDate(event.target.value)}/></label><button className="button button-pink" onClick={()=>load()} disabled={refreshing}>{refreshing?"Atualizando…":"Atualizar agenda"}</button><button className="button button-neutral" onClick={()=>client.auth.signOut()}>Sair</button></div></div>
    {message&&<p className="mt-6 rounded-2xl bg-[var(--blue-soft)] p-4 text-sm">{message}</p>}
    <section className="mt-8 rounded-[2rem] border border-[var(--line)] bg-white p-6 sm:p-8"><div className="flex flex-col gap-3 sm:flex-row sm:items-end sm:justify-between"><div><p className="eyebrow">RESUMO OPERACIONAL</p><h2 className="mt-3 font-serif text-3xl">O que precisa de atenção agora.</h2><p className="mt-2 max-w-2xl text-sm leading-6 text-[var(--muted)]">A recepção acompanha toda a clínica, identifica pendências e mantém profissionais e famílias alinhados.</p></div>{pendingToday>0&&<span className="rounded-full bg-[var(--pink-soft)] px-4 py-2 text-sm font-bold">{pendingToday} aguardando confirmação</span>}</div><div className="mt-6 grid gap-4 sm:grid-cols-2 xl:grid-cols-4"><ReceptionMetric value={String(confirmedToday)} label="confirmados no dia"/><ReceptionMetric value={String(pendingToday)} label="confirmações pendentes" attention={pendingToday>0}/><ReceptionMetric value={String(agenda?.upcoming.length??0)} label="próximas consultas visíveis"/><ReceptionMetric value={String(agenda?.recurrences.length??0)} label="acompanhamentos ativos"/></div></section>
    <div className="mt-8 grid gap-7 xl:grid-cols-[minmax(0,1fr)_360px]">
      <div className="grid gap-7">
        <section className="rounded-[2rem] border border-[var(--line)] bg-white p-6 sm:p-8"><div className="flex items-center justify-between"><div><h2 className="font-serif text-3xl">Atendimentos do dia</h2><p className="mt-2 text-sm text-[var(--muted)]">Consultas avulsas e sessões recorrentes.</p></div><span className="text-sm text-[var(--muted)]">{agenda?.appointments.length??0} agendados</span></div><div className="mt-6 grid gap-3">{agenda?.appointments.length?agenda.appointments.map(item=><article key={item.id} className="rounded-2xl border border-[var(--line)] p-5"><div className="flex flex-wrap items-start justify-between gap-3"><div><strong className="text-lg">{formatTime(item.starts_at)} · {item.patient_name}</strong><p className="mt-1 text-sm text-[var(--muted)]">{item.services?.name} com {item.professionals?.name}</p><p className="mt-2 text-sm">{item.phone} · {item.email}</p></div><div className="flex gap-2"><TypeBadge recurring={Boolean(item.recurring_appointment_id)}/><Status status={item.status}/></div></div>{item.status==="pending"&&<ReceptionActions item={item} onConfirm={confirmAppointment}/>}</article>):<Empty>Nenhum atendimento neste dia.</Empty>}</div><details className="schedule-group mt-8"><summary><strong>Horários ainda disponíveis</strong><span>{available.length} horários</span></summary><div className="flex flex-wrap gap-2 p-4 pt-1">{available.length?available.map(item=><span key={item.id} className="rounded-full bg-[var(--blue-soft)] px-4 py-2 text-sm">{formatTime(item.starts_at)} · {item.professionals?.name}</span>):<span className="text-sm text-[var(--muted)]">Nenhum horário aberto.</span>}</div></details></section>
        <details className="reception-collapsible"><summary><div><h2 className="font-serif text-2xl">Próximas consultas</h2><p className="mt-1 text-sm text-[var(--muted)]">Consulte quando precisar antecipar a organização dos próximos dias.</p></div><span>{agenda?.upcoming.length??0} próximas</span></summary><div className="grid max-h-[30rem] gap-3 overflow-auto p-6 pt-1 sm:grid-cols-2">{agenda?.upcoming.length?agenda.upcoming.map(item=><article key={item.id} className="rounded-2xl bg-[var(--surface)] p-5"><div className="flex items-start justify-between gap-3"><div><strong>{item.patient_name}</strong><p className="mt-1 text-sm text-[var(--muted)]">{formatDateTime(item.starts_at)} · {item.professionals?.name}</p></div><Status status={item.status}/></div><p className="mt-3 text-sm">{item.services?.name}</p></article>):<Empty>Nenhuma consulta futura encontrada.</Empty>}</div></details>
        <details className="reception-collapsible"><summary><div><h2 className="font-serif text-2xl">Acompanhamentos ativos</h2><p className="mt-1 text-sm text-[var(--muted)]">Abra somente quando precisar consultar horários fixos.</p></div><span>{agenda?.recurrences.length??0} ativos</span></summary><div className="grid gap-3 p-6 pt-1 sm:grid-cols-2">{agenda?.recurrences.length?agenda.recurrences.slice(0,showAllRecurrences?undefined:4).map(item=><article key={item.id} className="rounded-2xl bg-[var(--surface)] p-5"><strong>{item.patient_name}</strong><p className="mt-2 text-sm text-[var(--muted)]">{item.services?.name} · {item.professionals?.name}</p><p className="mt-2 text-sm">A cada {item.interval_days} dias · {item.local_start_time.slice(0,5)}</p><p className="mt-1 text-sm">{formatCalendarDate(item.starts_on)} a {formatCalendarDate(item.ends_on)}</p></article>):<Empty>Nenhum acompanhamento recorrente ativo.</Empty>}</div>{(agenda?.recurrences.length??0)>4&&<button className="button button-pink mx-6 mb-6" onClick={()=>setShowAllRecurrences(value=>!value)}>{showAllRecurrences?"Mostrar menos":"Ver todos os acompanhamentos"}</button>}</details>
      </div>
      <aside className="h-fit rounded-[2rem] bg-[var(--blue-soft)] p-7 xl:sticky xl:top-6"><p className="eyebrow">PAPEL DA RECEPÇÃO</p><h2 className="mt-3 font-serif text-2xl">Coordenar sem alterar a agenda clínica.</h2><p className="mt-3 text-sm leading-6 text-[var(--muted)]">Acompanhe confirmações, identifique pendências e entre em contato com a família. Cancelamentos, ausências e novos horários ficam sob responsabilidade da profissional.</p><div className="mt-5 rounded-2xl bg-white/70 p-4 text-sm"><strong>{pendingToday}</strong> {pendingToday===1?"confirmação pendente":"confirmações pendentes"} no dia selecionado.</div></aside>
    </div>
  </div>;
}

function SetupNotice(){return <div className="mx-auto max-w-2xl rounded-[2rem] bg-[var(--blue-soft)] p-8"><p className="eyebrow">CONFIGURAÇÃO NECESSÁRIA</p><h1 className="mt-4 font-serif text-4xl">A recepção está pronta para ser conectada.</h1><p className="mt-4 leading-7 text-[var(--muted)]">Configure as variáveis do Supabase no arquivo <code>.env.local</code>, execute as migrações e cadastre a primeira conta da equipe.</p></div>}
function Panel({children}:{children:React.ReactNode}){return <div className="rounded-[2rem] bg-white p-8">{children}</div>}
function Field({name,label,type="text",required=false}:{name:string;label:string;type?:string;required?:boolean}){return <label className="grid gap-2 text-sm font-semibold">{label}<input className="rounded-xl border border-[var(--line)] bg-white px-4 py-3" name={name} type={type} required={required}/></label>}
function Empty({children}:{children:React.ReactNode}){return <p className="rounded-2xl bg-[var(--surface)] p-6 text-[var(--muted)]">{children}</p>}
function Status({status}:{status:Appointment["status"]}){const label={pending:"Pendente",confirmed:"Confirmado",cancelled:"Cancelado"}[status];return <span className="rounded-full bg-[var(--surface)] px-3 py-1 text-xs font-bold uppercase tracking-wider">{label}</span>}
function TypeBadge({recurring}:{recurring:boolean}){return <span className="rounded-full bg-[var(--blue-soft)] px-3 py-1 text-xs font-bold uppercase tracking-wider">{recurring?"Recorrente":"Avulso"}</span>}
function ReceptionActions({item,onConfirm}:{item:Appointment;onConfirm:(id:string)=>void}){return <div className="mt-4"><button className="button button-pink" onClick={()=>onConfirm(item.id)}>Confirmar atendimento</button></div>}
function ReceptionMetric({value,label,attention=false}:{value:string;label:string;attention?:boolean}){return <div className={`rounded-2xl p-5 ${attention?"bg-[var(--pink-soft)]":"bg-[var(--surface)]"}`}><strong className="font-serif text-4xl">{value}</strong><p className="mt-2 text-sm text-[var(--muted)]">{label}</p></div>}
function formatTime(value:string){return new Intl.DateTimeFormat("pt-BR",{hour:"2-digit",minute:"2-digit",timeZone:"America/Sao_Paulo"}).format(new Date(value))}
function formatDateTime(value:string){return new Intl.DateTimeFormat("pt-BR",{day:"2-digit",month:"2-digit",hour:"2-digit",minute:"2-digit",timeZone:"America/Sao_Paulo"}).format(new Date(value))}
function formatCalendarDate(value:string){return new Intl.DateTimeFormat("pt-BR",{timeZone:"America/Sao_Paulo"}).format(new Date(`${value}T12:00:00-03:00`))}
