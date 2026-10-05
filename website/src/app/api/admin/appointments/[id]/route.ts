import { NextResponse } from "next/server";
import { z } from "zod";
import { requireStaff } from "@/lib/auth/require-staff";

const schema=z.object({status:z.enum(["confirmed","cancelled"]),cancellationReason:z.string().trim().max(500).optional()}).superRefine((value,context)=>{if(value.status==="cancelled"&&(!value.cancellationReason||value.cancellationReason.length<3))context.addIssue({code:"custom",path:["cancellationReason"],message:"Informe o motivo do cancelamento."})});
export async function PATCH(request:Request,{params}:{params:Promise<{id:string}>}){
 const auth=await requireStaff(request);if("error" in auth)return NextResponse.json({error:auth.error},{status:auth.status});
 if(!["admin","reception","professional"].includes(auth.staff.role))return NextResponse.json({error:"Acesso não autorizado."},{status:403});
 const input=schema.safeParse(await request.json().catch(()=>null));const {id}=await params;
 if(!input.success||!z.string().uuid().safeParse(id).success)return NextResponse.json({error:input.error?.issues[0]?.message??"Solicitação inválida."},{status:400});
 if(auth.staff.role==="reception"&&input.data.status==="cancelled")return NextResponse.json({error:"O cancelamento deve ser realizado pela profissional responsável."},{status:403});
 let update=auth.supabase.from("appointments").update({status:input.data.status,updated_at:new Date().toISOString()}).eq("id",id);
 if(auth.staff.role==="professional")update=update.eq("professional_id",auth.staff.professional_id);
 const {data,error}=await update.select("id").maybeSingle();
 if(error)return NextResponse.json({error:"Não foi possível atualizar o atendimento."},{status:500});
 if(!data)return NextResponse.json({error:"Atendimento não encontrado na sua agenda."},{status:404});
 await auth.supabase.from("appointment_events").insert({appointment_id:id,event_type:input.data.status,metadata:{staff_user_id:auth.user.id,cancellation_reason:input.data.cancellationReason??null,staff_role:auth.staff.role}});
 return NextResponse.json({ok:true});
}
