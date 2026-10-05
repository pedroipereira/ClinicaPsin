import "server-only";
import { createAdminClient } from "@/lib/supabase/admin";

export async function requireStaff(request:Request) {
  const supabase=createAdminClient();
  if(!supabase) return { error:"Banco não configurado.",status:503 } as const;
  const token=request.headers.get("authorization")?.replace(/^Bearer\s+/i,"");
  if(!token) return { error:"Acesso não autorizado.",status:401 } as const;
  const {data:{user},error}=await supabase.auth.getUser(token);
  if(error||!user) return { error:"Sessão inválida.",status:401 } as const;
  const {data:staff}=await supabase.from("staff_profiles").select("name, role, active, professional_id").eq("user_id",user.id).eq("active",true).maybeSingle();
  if(!staff) return { error:"Usuário sem acesso à recepção.",status:403 } as const;
  return { supabase,user,staff } as const;
}
