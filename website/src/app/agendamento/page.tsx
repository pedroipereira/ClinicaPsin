import type { Metadata } from "next";
import Image from "next/image";
import Link from "next/link";
import { SchedulingWizard } from "@/components/scheduling/scheduling-wizard";

export const metadata:Metadata = { title:"Agendamento", description:"Escolha a modalidade, o atendimento, o profissional e o horário na Psin Clínica." };

export default function SchedulingPage() {
  return <main className="min-h-screen bg-[var(--surface)]">
    <header className="mx-auto flex max-w-6xl items-center justify-between px-6 py-6 lg:px-10">
      <Link href="/" className="flex items-center gap-3" aria-label="Voltar ao início da Psin Clínica"><Image src="/logo.jpg" alt="" width={52} height={52} className="rounded-full" priority /><span className="font-serif text-xl text-[var(--ink)]">Psin Clínica</span></Link>
      <Link className="text-sm font-semibold text-[var(--muted)]" href="/">Voltar ao site</Link>
    </header>
    <div className="mx-auto max-w-6xl px-6 pb-20 pt-10 lg:px-10">
      <div className="mb-10 max-w-3xl"><p className="eyebrow">AGENDE SEU ATENDIMENTO</p><h1 className="mt-5 font-serif text-5xl leading-[1.05] tracking-[-0.03em] text-[var(--ink)] sm:text-6xl">Encontre uma opção que faça sentido para você.</h1><p className="mt-5 text-lg leading-8 text-[var(--muted)]">Escolha como deseja ser atendido e consulte as opções disponíveis.</p></div>
      <SchedulingWizard />
    </div>
  </main>;
}
