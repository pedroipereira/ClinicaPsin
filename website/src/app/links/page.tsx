import type { Metadata } from "next";
import Image from "next/image";
import Link from "next/link";
import { CopyAddress } from "./copy-address";
import styles from "./links.module.css";

export const metadata: Metadata = {
  title: "Nossos links",
  description:
    "Agende seu atendimento, conheça a Psin Clínica e encontre nossos contatos, profissionais e conteúdos.",
};

const maps =
  "https://www.google.com/maps/search/?api=1&query=Psin+Cl%C3%ADnica+CSE+01+Lote+06+Sala+102+Taguatinga+Sul";
const whatsapp =
  "https://wa.me/5561996225522?text=Ol%C3%A1%21%20Gostaria%20de%20informa%C3%A7%C3%B5es%20sobre%20atendimento%20na%20Psin%20Cl%C3%ADnica.";

type IconName = "calendar" | "home" | "people" | "book" | "map" | "google";

function Icon({ name }: { name: IconName }) {
  if (name === "calendar")
    return (
      <svg viewBox="0 0 24 24" aria-hidden="true">
        <path d="M5 4h14a2 2 0 0 1 2 2v14H3V6a2 2 0 0 1 2-2Z" />
        <path d="M8 2v4M16 2v4M3 9h18M8 13h3M13 13h3M8 17h3" />
      </svg>
    );
  if (name === "home")
    return (
      <svg viewBox="0 0 24 24" aria-hidden="true">
        <path d="m3 10 9-7 9 7v11H3Z" />
        <path d="M9 21v-8h6v8" />
      </svg>
    );
  if (name === "people")
    return (
      <svg viewBox="0 0 24 24" aria-hidden="true">
        <circle cx="9" cy="8" r="3" />
        <path d="M3 21v-3a6 6 0 0 1 12 0v3M16 5a3 3 0 0 1 0 6m2 4a5 5 0 0 1 3 5" />
      </svg>
    );
  if (name === "book")
    return (
      <svg viewBox="0 0 24 24" aria-hidden="true">
        <path d="M12 5C8 2 4 3 2 4v16c3-2 6-2 10 0 4-2 7-2 10 0V4c-3-1-6-2-10 1Z" />
        <path d="M12 5v15" />
      </svg>
    );
  if (name === "map")
    return (
      <svg viewBox="0 0 24 24" aria-hidden="true">
        <path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 1 1 16 0Z" />
        <circle cx="12" cy="10" r="2.5" />
      </svg>
    );
  return (
    <svg viewBox="0 0 488 512" aria-hidden="true" className={styles.brandIcon}>
      <path d="M488 261.8C488 403.3 391.1 504 248 504 110.8 504 0 393.2 0 256S110.8 8 248 8c66.8 0 123 24.5 166.3 64.9l-67.5 64.9C258.5 52.6 94.3 116.6 94.3 256c0 86.5 69.1 156.6 153.7 156.6 98.2 0 135-70.4 140.8-106.9H248v-85.3h236.1c2.3 12.7 3.9 24.9 3.9 41.4Z" />
    </svg>
  );
}

function Arrow() {
  return (
    <svg className={styles.arrow} viewBox="0 0 24 24" aria-hidden="true">
      <path d="m9 5 7 7-7 7" />
    </svg>
  );
}

function LinkCard({
  href,
  icon,
  title,
  description,
  primary = false,
  external = false,
}: {
  href: string;
  icon: IconName;
  title: string;
  description: string;
  primary?: boolean;
  external?: boolean;
}) {
  const className = `${styles.card} ${primary ? styles.primary : ""}`;
  const content = (
    <>
      <span className={styles.icon}>
        <Icon name={icon} />
      </span>
      <span className={styles.copy}>
        <strong>{title}</strong>
        <span>{description}</span>
      </span>
      <Arrow />
    </>
  );

  if (external)
    return (
      <a className={className} href={href} target="_blank" rel="noopener noreferrer">
        {content}
      </a>
    );

  return (
    <Link className={className} href={href}>
      {content}
    </Link>
  );
}

export default function LinksPage() {
  return (
    <main className={styles.page}>
      <header className={styles.profile}>
        <Link className={styles.logo} href="/" aria-label="Conheça o website da Psin Clínica">
          <Image src="/institutional/logo.jpg" alt="Logo da Psin Clínica" width={88} height={88} priority />
        </Link>
        <p className={styles.eyebrow}>PSICOLOGIA E PSICANÁLISE</p>
        <h1>Psin Clínica</h1>
        <p className={styles.intro}>
          Sua história merece
          <br />
          tempo, atenção e escuta.
        </p>
        <p className={styles.modality}>
          <span aria-hidden="true" /> Presencial e online
        </p>
      </header>

      <nav className={styles.list} aria-label="Links da Psin Clínica">
        <LinkCard
          href="/agendamento"
          icon="calendar"
          title="Agende seu atendimento"
          description="Escolha atendimento, profissional e horário"
          primary
        />
        <LinkCard href="/" icon="home" title="Conheça nossa clínica" description="Um espaço para sua história" />
        <LinkCard href="/#equipe" icon="people" title="Nossa equipe" description="Profissionais e abordagens" />
        <LinkCard href="/blog" icon="book" title="Blog da Psin" description="Conversas com as famílias" />
        <LinkCard href={maps} icon="map" title="Como chegar" description="Veja o caminho no Google Maps" external />
        <LinkCard href={maps} icon="google" title="Avalie a Psin no Google" description="Deixe sua avaliação pelo Maps" external />
      </nav>

      <footer className={styles.footer}>
        <div className={styles.socials}>
          <a href="https://www.instagram.com/psinclinicapsicologia/" target="_blank" rel="noreferrer" aria-label="Instagram">
            <Image src="/institutional/images/social/instagram.svg" alt="" width={19} height={19} />
          </a>
          <a href={whatsapp} target="_blank" rel="noreferrer" aria-label="WhatsApp">
            <Image src="/institutional/images/social/whatsapp.svg" alt="" width={19} height={19} />
          </a>
          <a href={maps} target="_blank" rel="noreferrer" aria-label="Google">
            <Image src="/institutional/images/social/google.svg" alt="" width={19} height={19} />
          </a>
          <a href="https://www.facebook.com/psinclinicapsicologia/" target="_blank" rel="noreferrer" aria-label="Facebook">
            <Image src="/institutional/images/social/facebook-f.svg" alt="" width={19} height={19} />
          </a>
        </div>
        <a className={styles.phone} href="tel:+556133514551">
          Ligue para a clínica · (61) 3351-4551
        </a>
        <address>
          CSE 01 · Lote 06 · Sala 102
          <br />
          Taguatinga Sul · Brasília - DF
          <br />
          CEP 72025-015
        </address>
        <CopyAddress />
        <Link className={styles.home} href="/">
          Um espaço para escutar.
        </Link>
      </footer>
    </main>
  );
}
