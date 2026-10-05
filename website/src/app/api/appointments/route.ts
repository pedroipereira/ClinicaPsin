import { createHash, randomBytes } from "node:crypto";
import { NextResponse } from "next/server";
import { createAdminClient } from "@/lib/supabase/admin";
import { appointmentSchema } from "@/lib/validation/appointment";
import { normalizeBrazilianPhone } from "@/lib/phone";

export async function POST(request: Request) {
  const supabase = createAdminClient();
  if (!supabase) return NextResponse.json({ error: "O agendamento real ainda não foi configurado." }, { status: 503 });

  const parsed = appointmentSchema.safeParse(await request.json().catch(() => null));
  if (!parsed.success) return NextResponse.json({ error: "Revise os dados informados.", fields: parsed.error.flatten().fieldErrors }, { status: 400 });

  const cancellationToken = randomBytes(32).toString("base64url");
  const cancellationTokenHash = createHash("sha256").update(cancellationToken).digest("hex");
  const input = parsed.data;
  const { data, error } = await supabase.rpc("book_appointment", {
    p_slot_id: input.slotId,
    p_patient_name: input.patientName,
    p_responsible_name: input.responsibleName || null,
    p_phone: normalizeBrazilianPhone(input.phone),
    p_email: input.email,
    p_cancellation_token_hash: cancellationTokenHash,
  });

  if (error) {
    const unavailable = error.code === "P0001" || error.code === "23505" || error.code === "23P01";
    return NextResponse.json({ error: unavailable ? "Este horário acabou de ser reservado. Escolha outro." : "Não foi possível concluir o agendamento." }, { status: unavailable ? 409 : 500 });
  }

  return NextResponse.json({ appointmentId: data, cancellationToken }, { status: 201 });
}
