import { NextResponse } from "next/server";
import { z } from "zod";
import { requireStaff } from "@/lib/auth/require-staff";

const schema=z.object({professionalId:z.string().uuid(),serviceId:z.string().uuid(),modality:z.enum(["presencial","online"]),startsAt:z.iso.datetime()});
export async function POST(request:Request){
 const auth=await requireStaff(request);if("error" in auth)return NextResponse.json({error:auth.error},{status:auth.status});
 if(!["admin","professional"].includes(auth.staff.role))return NextResponse.json({error:"A abertura de horários pertence à profissional responsável."},{status:403});
 const parsed=schema.safeParse(await request.json().catch(()=>null));if(!parsed.success)return NextResponse.json({error:"Revise os dados do horário."},{status:400});
 if(auth.staff.role==="professional"&&parsed.data.professionalId!==auth.staff.professional_id)return NextResponse.json({error:"Você só pode abrir horários na própria agenda."},{status:403});
 const {data:service}=await auth.supabase.from("services").select("duration_minutes").eq("id",parsed.data.serviceId).single();
 if(!service)return NextResponse.json({error:"Serviço não encontrado."},{status:404});
 const startsAt=new Date(parsed.data.startsAt);const endsAt=new Date(startsAt.getTime()+service.duration_minutes*60000);
 const {data,error}=await auth.supabase.from("appointment_slots").insert({professional_id:parsed.data.professionalId,service_id:parsed.data.serviceId,modality:parsed.data.modality,starts_at:startsAt.toISOString(),ends_at:endsAt.toISOString()}).select("id").single();
 if(error)return NextResponse.json({error:error.code==="23505"?"Já existe um horário para esse profissional nesse momento.":"Não foi possível criar o horário."},{status:error.code==="23505"?409:500});
 return NextResponse.json(data,{status:201});
}
