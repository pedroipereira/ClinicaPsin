import type { Metadata } from "next";
import Image from "next/image";
import Link from "next/link";
import { notFound } from "next/navigation";
import { SiteFooter,SiteHeader } from "@/components/institutional/site-chrome";
import { articles } from "@/lib/institutional-content";
import "../../institutional.css";
export function generateStaticParams(){return articles.map(({slug})=>({slug}))}
export async function generateMetadata({params}:{params:Promise<{slug:string}>}):Promise<Metadata>{const {slug}=await params;const article=articles.find(item=>item.slug===slug);return article?{title:article.title,description:article.intro}:{title:"Artigo"}}
export default async function ArticlePage({params}:{params:Promise<{slug:string}>}){const {slug}=await params;const article=articles.find(item=>item.slug===slug);if(!article)notFound();return <div className="inner-page"><SiteHeader/><main id="conteudo"><div className="wrap"><article className="article-page"><Link className="back-link" href="/blog">Voltar ao blog</Link><header className="article-heading"><span className="eyebrow">{article.category}</span><h1>{article.title}</h1><p>{article.intro}</p></header><figure className="article-cover"><Image src={article.image} alt={article.alt} width={1200} height={800} priority/><figcaption>Imagem ilustrativa gerada por IA.</figcaption></figure><div className="article-body">{article.paragraphs.map(paragraph=><p key={paragraph}>{paragraph}</p>)}<p className="article-disclaimer">Conteúdo educativo. Uma orientação individual depende da avaliação de um profissional.</p><div className="article-cta"><h2>Quer conversar sobre atendimento?</h2><Link className="btn" href="/agendamento">Ver horários disponíveis</Link></div></div></article></div></main><SiteFooter/></div>}
