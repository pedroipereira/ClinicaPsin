import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: { default: "Psin Clínica", template: "%s | Psin Clínica" },
  description: "Psicologia e psicanálise para crianças, adolescentes e adultos em Taguatinga Sul.",
};

export default function RootLayout({ children }: LayoutProps<"/">) {
  return <html lang="pt-BR"><body>{children}</body></html>;
}
