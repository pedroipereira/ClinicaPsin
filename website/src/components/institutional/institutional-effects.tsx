"use client";

import { useEffect } from "react";

export function InstitutionalEffects(){
  useEffect(()=>{
    const root=document.querySelector<HTMLElement>(".institutional-site");
    if(!root)return;
    const reducedMotion=window.matchMedia("(prefers-reduced-motion: reduce)");
    const targets=root.querySelectorAll<HTMLElement>(".clinic-intro,.professional,.environment-grid,.center-heading,.faq-grid,.review,.blog-card,.contact");
    let observer:IntersectionObserver|undefined;
    if(!reducedMotion.matches&&"IntersectionObserver" in window){
      observer=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add("is-visible");observer?.unobserve(entry.target)}}),{threshold:.08});
      targets.forEach(element=>{element.classList.add("reveal-ready");observer?.observe(element)});
    }else targets.forEach(element=>element.classList.add("is-visible"));

    const progress=document.createElement("div");
    progress.className="scroll-progress";
    progress.setAttribute("aria-hidden","true");
    root.append(progress);
    let queued=false;
    const updateProgress=()=>{const total=document.documentElement.scrollHeight-innerHeight;progress.style.transform=`scaleX(${total>0?Math.min(1,Math.max(0,scrollY/total)):0})`;queued=false};
    const onScroll=()=>{if(!queued){queued=true;requestAnimationFrame(updateProgress)}};
    addEventListener("scroll",onScroll,{passive:true});
    addEventListener("resize",updateProgress);
    updateProgress();

    const cleanups:Array<()=>void>=[];
    const hoverQuestions=window.matchMedia("(hover: hover) and (pointer: fine)");
    root.querySelectorAll<HTMLDetailsElement>(".faq-items details").forEach(item=>{
      const summary=item.querySelector<HTMLElement>("summary");
      if(!summary)return;
      let openedByHover=false;
      let hoverTimer:number|undefined;
      const enter=(event:PointerEvent)=>{if(event.pointerType==="mouse"&&hoverQuestions.matches&&!item.open){clearTimeout(hoverTimer);hoverTimer=window.setTimeout(()=>{if(!item.open){item.open=true;openedByHover=true}},180)}};
      const leave=()=>{clearTimeout(hoverTimer);if(openedByHover&&!item.contains(document.activeElement)){item.open=false;openedByHover=false}};
      const click=(event:MouseEvent)=>{clearTimeout(hoverTimer);if(openedByHover&&event.detail>0){event.preventDefault();openedByHover=false}else openedByHover=false};
      const keydown=(event:KeyboardEvent)=>{if(event.key==="Escape"){clearTimeout(hoverTimer);item.open=false;openedByHover=false;summary.focus()}};
      item.addEventListener("pointerenter",enter);item.addEventListener("pointerleave",leave);summary.addEventListener("click",click);item.addEventListener("keydown",keydown);
      cleanups.push(()=>{item.removeEventListener("pointerenter",enter);item.removeEventListener("pointerleave",leave);summary.removeEventListener("click",click);item.removeEventListener("keydown",keydown)});
    });
    return()=>{observer?.disconnect();removeEventListener("scroll",onScroll);removeEventListener("resize",updateProgress);progress.remove();cleanups.forEach(cleanup=>cleanup())};
  },[]);
  return null;
}
