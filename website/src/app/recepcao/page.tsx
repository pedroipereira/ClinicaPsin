import type { Metadata } from "next";
import Image from "next/image";
import Link from "next/link";
import { ReceptionDashboard } from "@/components/reception/reception-dashboard";

export const metadata:Metadata={title:"Recepção",robots:{index:false,follow:false}};
export default function ReceptionPage(){return <main className="min-h-screen bg-[var(--surface)]"><header className="mx-auto flex max-w-7xl items-center justify-between px-6 py-6 lg:px-10"><Link href="/" className="flex items-center gap-3"><Image src="/logo.jpg" alt="" width={48} height={48} className="rounded-full"/><span className="font-serif text-xl">Psin Clínica</span></Link><span className="eyebrow">ÁREA DA RECEPÇÃO</span></header><div className="mx-auto max-w-7xl px-6 pb-20 pt-8 lg:px-10"><ReceptionDashboard/></div></main>}
