"use client";

import { useState } from "react";
import styles from "./links.module.css";

const address = "CSE 01, Lote 06, Sala 102, Taguatinga Sul, Brasília - DF, CEP 72025-015";

export function CopyAddress() {
  const [status, setStatus] = useState("");

  async function copyAddress() {
    try {
      await navigator.clipboard.writeText(address);
      setStatus("Endereço copiado!");
    } catch {
      setStatus("Não foi possível copiar. Toque e segure o endereço acima.");
    }
  }

  return (
    <>
      <button className={styles.copyAddress} type="button" onClick={copyAddress}>
        Copiar endereço
      </button>
      <p className={styles.copyStatus} role="status" aria-live="polite">
        {status}
      </p>
    </>
  );
}
