export function formatBrazilianPhone(value:string){
  const digits=value.replace(/\D/g,"").slice(0,11);
  if(!digits)return "";
  if(digits.length<=2)return `(${digits}`;
  if(digits.length<=7)return `(${digits.slice(0,2)})${digits.slice(2)}`;
  return `(${digits.slice(0,2)})${digits.slice(2,7)}-${digits.slice(7)}`;
}

export function normalizeBrazilianPhone(value:string){
  return formatBrazilianPhone(value);
}
