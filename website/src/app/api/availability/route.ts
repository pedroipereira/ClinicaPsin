import { NextRequest, NextResponse } from "next/server";
import { z } from "zod";
import { createAdminClient } from "@/lib/supabase/admin";

const querySchema = z.object({
  modality: z.enum(["presencial", "online"]),
  service: z.string().min(1).max(80),
  professional: z.string().min(1).max(80).optional(),
});

export async function GET(request: NextRequest) {
  const parsed = querySchema.safeParse(Object.fromEntries(request.nextUrl.searchParams));
  if (!parsed.success) return NextResponse.json({ error: "Filtros inválidos." }, { status: 400 });

  const supabase = createAdminClient();
  if (!supabase) return NextResponse.json({ mode: "demo", slots: [] }, { status: 503 });

  const { modality, service, professional } = parsed.data;
  await supabase.rpc("generate_appointment_slots", {
    p_service_slug: service,
    p_modality: modality,
    p_professional_slug: professional ?? null,
    p_days: 60,
  });
  let query = supabase
    .from("available_slots")
    .select("id, starts_at, ends_at, professional_slug, professional_name, service_slug")
    .eq("modality", modality)
    .eq("service_slug", service)
    .gte("starts_at", new Date().toISOString())
    .order("starts_at")
    .limit(40);

  if (professional && professional !== "first-available") query = query.eq("professional_slug", professional);
  const { data, error } = await query;
  if (error) return NextResponse.json({ error: "Não foi possível consultar os horários." }, { status: 500 });

  return NextResponse.json({ mode: "live", slots: data });
}
