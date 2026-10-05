import { NextResponse } from "next/server";
import { requireStaff } from "@/lib/auth/require-staff";
import { formatBrazilianPhone } from "@/lib/phone";

export async function GET(request:Request){
  const auth=await requireStaff(request);
  if("error" in auth)return NextResponse.json({error:auth.error},{status:auth.status});
  if(!["admin","reception"].includes(auth.staff.role))return NextResponse.json({error:"Acesso restrito à recepção."},{status:403});

  const url=new URL(request.url);
  const requestedDate=url.searchParams.get("date");
  const date=requestedDate&&/^\d{4}-\d{2}-\d{2}$/.test(requestedDate)?requestedDate:new Date().toISOString().slice(0,10);
  const start=new Date(`${date}T00:00:00-03:00`).toISOString();
  const end=new Date(`${date}T23:59:59-03:00`).toISOString();

  const upcomingStart=new Date().toISOString();
  const [appointments,upcoming,slots,recurrences,professionals,services]=await Promise.all([
    auth.supabase.from("appointments").select("id, starts_at, ends_at, status, patient_name, responsible_name, phone, email, recurring_appointment_id, professionals(name), services(name)").gte("starts_at",start).lte("starts_at",end).order("starts_at"),
    auth.supabase.from("appointments").select("id, starts_at, ends_at, status, patient_name, responsible_name, phone, email, recurring_appointment_id, professionals(name), services(name)").gte("starts_at",upcomingStart).in("status",["pending","confirmed"]).order("starts_at").limit(12),
    auth.supabase.from("appointment_slots").select("id, starts_at, ends_at, active, professionals(name), services(name)").gte("starts_at",start).lte("starts_at",end).order("starts_at"),
    auth.supabase.from("recurring_appointments").select("id, patient_name, starts_on, ends_on, local_start_time, interval_days, modality, professionals(name), services(name)").eq("active",true).gte("ends_on",date).order("patient_name"),
    auth.supabase.from("professionals").select("id, name").eq("active",true).order("name"),
    auth.supabase.from("services").select("id, name, duration_minutes").eq("active",true).order("name"),
  ]);
  const failure=[appointments,upcoming,slots,recurrences,professionals,services].find(result=>result.error);
  if(failure?.error)return NextResponse.json({error:"Não foi possível carregar a agenda."},{status:500});
  const withFormattedPhone=<T extends {phone:string}>(items:T[]|null)=>items?.map(item=>({...item,phone:formatBrazilianPhone(item.phone)}))??[];
  const legacyOnline=new Set(["teleconsulta","psicoterapia online"]);
  return NextResponse.json({staff:auth.staff,appointments:withFormattedPhone(appointments.data),upcoming:withFormattedPhone(upcoming.data),slots:slots.data,recurrences:recurrences.data,professionals:professionals.data,services:services.data?.filter(service=>!legacyOnline.has(service.name.toLocaleLowerCase("pt-BR"))),updatedAt:new Date().toISOString()});
}
