import { z } from "zod";

export const appointmentSchema = z.object({
  slotId: z.string().uuid("O horário selecionado não é válido."),
  patientName: z.string().trim().min(3,"Informe o nome completo do paciente.").max(120,"O nome informado é muito longo."),
  responsibleName: z.string().trim().min(3,"Informe o nome completo do responsável.").max(120,"O nome do responsável é muito longo.").optional().or(z.literal("")),
  phone: z.string().trim().regex(/^\+?[0-9 ()-]{10,20}$/,"Informe um WhatsApp válido, incluindo o DDD."),
  phoneConfirmation: z.string().trim().min(10,"Repita o número de WhatsApp."),
  email: z.string().trim().email("Informe um endereço de e-mail válido.").max(180,"O e-mail informado é muito longo."),
  privacyAccepted: z.literal(true,"É necessário autorizar o uso dos dados para concluir."),
}).refine((data) => data.phone.replace(/\D/g, "") === data.phoneConfirmation.replace(/\D/g, ""), { path:["phoneConfirmation"], message:"Os números de WhatsApp não coincidem." });

export type AppointmentInput = z.infer<typeof appointmentSchema>;
