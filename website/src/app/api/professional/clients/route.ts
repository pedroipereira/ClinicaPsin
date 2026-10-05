import { NextResponse } from "next/server";
import { z } from "zod";
import { requireStaff } from "@/lib/auth/require-staff";
import { formatBrazilianPhone } from "@/lib/phone";

const schema=z.object({
  professionalId:z.string().uuid().optional(),
  originalName:z.string().trim().min(2).max(120),
  patientName:z.string().trim().min(2).max(120),
  responsibleName:z.string().trim().max(120).optional(),
  phone:z.string().trim().min(10).max(20),
  email:z.string().trim().email(),
});

export async function PATCH(request:Request){
  const auth=await requireStaff(request);
  if("error" in auth)return NextResponse.json({error:auth.error},{status:auth.status});
  const parsed=schema.safeParse(await request.json().catch(()=>null));
  if(!parsed.success)return NextResponse.json({error:"Confira o nome, o WhatsApp e o e-mail do cliente."},{status:400});
  const professionalId=auth.staff.role==="professional"?auth.staff.professional_id:parsed.data.professionalId;
  if(!professionalId)return NextResponse.json({error:"Profissional não identificado."},{status:400});
  const values={patient_name:parsed.data.patientName,responsible_name:parsed.data.responsibleName||null,phone:formatBrazilianPhone(parsed.data.phone),email:parsed.data.email};
  const now=new Date().toISOString();
  const [appointments,recurrences]=await Promise.all([
    auth.supabase.from("appointments").update(values).eq("professional_id",professionalId).eq("patient_name",parsed.data.originalName).gte("starts_at",now),
    auth.supabase.from("recurring_appointments").update(values).eq("professional_id",professionalId).eq("patient_name",parsed.data.originalName).eq("active",true),
  ]);
  if(appointments.error||recurrences.error)return NextResponse.json({error:"Não foi possível atualizar os dados do cliente."},{status:500});
  return NextResponse.json({ok:true});
}
