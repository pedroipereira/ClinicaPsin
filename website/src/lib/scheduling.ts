export type Modality = "presencial" | "online";
export type Service = { id:string; name:string; modalities:Modality[] };
export type Professional = { id:string; name:string; role:string; serviceIds:string[]; modalities:Modality[] };
export type TimeSlot = { id:string; professionalId:string; modality:Modality; serviceId:string; date:string; dayLabel:string; time:string };

export const services:Service[] = [
  { id:"primeira-psicologia", name:"Primeira consulta de psicologia", modalities:["presencial","online"] },
  { id:"primeira-psicanalise", name:"Primeira consulta de psicanálise", modalities:["presencial","online"] },
  { id:"psicoterapia", name:"Psicoterapia", modalities:["presencial","online"] },
  { id:"psicologia-infantil", name:"Psicologia infantil", modalities:["presencial","online"] },
];

export const professionals:Professional[] = [
  { id:"allice", name:"Allice Gracyelli de Melo", role:"Psicóloga", serviceIds:["primeira-psicologia","psicoterapia","psicologia-infantil"], modalities:["presencial","online"] },
  { id:"sandson", name:"Sandson Barbosa Azevedo Junior", role:"Psicólogo", serviceIds:["primeira-psicologia","psicoterapia"], modalities:["presencial","online"] },
  { id:"emanuele", name:"Emanuele Martins Carlos de Souza", role:"Psicóloga", serviceIds:["primeira-psicologia","psicoterapia"], modalities:["presencial","online"] },
  { id:"suely", name:"Suely P. de Melo", role:"Psicanalista clínica", serviceIds:["primeira-psicanalise"], modalities:["presencial","online"] },
];

export const demoSlots:TimeSlot[] = [
  { id:"a-1", professionalId:"allice", modality:"presencial", serviceId:"primeira-psicologia", date:"2026-10-06", dayLabel:"Ter, 06 out", time:"08:00" },
  { id:"a-2", professionalId:"allice", modality:"presencial", serviceId:"primeira-psicologia", date:"2026-10-06", dayLabel:"Ter, 06 out", time:"08:40" },
  { id:"s-1", professionalId:"sandson", modality:"presencial", serviceId:"primeira-psicologia", date:"2026-10-07", dayLabel:"Qua, 07 out", time:"10:00" },
  { id:"e-1", professionalId:"emanuele", modality:"presencial", serviceId:"psicoterapia", date:"2026-10-08", dayLabel:"Qui, 08 out", time:"15:00" },
  { id:"u-1", professionalId:"suely", modality:"presencial", serviceId:"primeira-psicanalise", date:"2026-10-09", dayLabel:"Sex, 09 out", time:"09:20" },
  { id:"a-3", professionalId:"allice", modality:"online", serviceId:"primeira-psicologia", date:"2026-10-06", dayLabel:"Ter, 06 out", time:"09:00" },
  { id:"s-2", professionalId:"sandson", modality:"online", serviceId:"primeira-psicologia", date:"2026-10-06", dayLabel:"Ter, 06 out", time:"09:40" },
  { id:"e-2", professionalId:"emanuele", modality:"online", serviceId:"psicoterapia", date:"2026-10-08", dayLabel:"Qui, 08 out", time:"14:00" },
];
