const reducedMotion=window.matchMedia('(prefers-reduced-motion: reduce)');
if(!reducedMotion.matches && 'IntersectionObserver' in window){
 const observer=new IntersectionObserver(entries=>{entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('is-visible');observer.unobserve(entry.target)}})},{threshold:.08});
 document.querySelectorAll('.clinic-intro,.professional,.environment-grid,.center-heading,.faq-grid,.review,.blog-card,.contact').forEach(el=>{el.classList.add('reveal-ready');observer.observe(el)});
 reducedMotion.addEventListener('change',event=>{if(event.matches){observer.disconnect();document.querySelectorAll('.reveal-ready').forEach(el=>el.classList.add('is-visible'))}});
}
const progress=document.createElement('div');progress.className='scroll-progress';progress.setAttribute('aria-hidden','true');document.body.append(progress);
let queued=false;
function updateProgress(){const total=document.documentElement.scrollHeight-innerHeight;progress.style.transform=`scaleX(${total>0?Math.min(1,Math.max(0,scrollY/total)):0})`;queued=false}
addEventListener('scroll',()=>{if(!queued){queued=true;requestAnimationFrame(updateProgress)}},{passive:true});addEventListener('resize',updateProgress);updateProgress();

// Hover previews answers with a mouse; click/tap and keyboard keep native details behavior.
const hoverQuestions=window.matchMedia('(hover: hover) and (pointer: fine)');
document.querySelectorAll('.faq-items details').forEach(item=>{
 const summary=item.querySelector('summary');
 let openedByHover=false;
 let hoverTimer;
 item.addEventListener('pointerenter',event=>{
  if(event.pointerType==='mouse' && hoverQuestions.matches && !item.open){
   clearTimeout(hoverTimer);
   hoverTimer=setTimeout(()=>{if(!item.open){item.open=true;openedByHover=true;}},180);
  }
 });
 item.addEventListener('pointerleave',()=>{
  clearTimeout(hoverTimer);
  if(openedByHover && !item.contains(document.activeElement)){item.open=false;openedByHover=false;}
 });
 summary.addEventListener('click',event=>{
  clearTimeout(hoverTimer);
  if(openedByHover && event.detail>0){event.preventDefault();openedByHover=false;}
  else openedByHover=false;
 });
 item.addEventListener('keydown',event=>{
  if(event.key==='Escape'){clearTimeout(hoverTimer);item.open=false;openedByHover=false;summary.focus();}
 });
});
