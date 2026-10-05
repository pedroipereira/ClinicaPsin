import type { Metadata } from "next";
import Image from "next/image";
import Link from "next/link";
import { SiteFooter,SiteHeader } from "@/components/institutional/site-chrome";
import { articles } from "@/lib/institutional-content";
import "../institutional.css";
export const metadata:Metadata={title:"Blog",description:"Conteúdos educativos da Psin Clínica para pessoas e famílias."};
export default function Blog(){return <div className="inner-page"><SiteHeader/><main id="conteudo"><div className="wrap"><section className="section"><span className="pill">CONVERSAS COM A FAMÍLIA</span><h1>Blog da Psin.</h1><p className="lead">Informação para abrir conversas sobre cuidado, infância, emoções e família.</p><div className="blog-list">{articles.map(article=><article className="blog-card" key={article.slug}><Link className="blog-photo" href={`/blog/${article.slug}`}><Image src={article.image} alt={article.alt} width={1200} height={800}/></Link><div className="blog-card-body"><span className="eyebrow">{article.category}</span><h3><Link href={`/blog/${article.slug}`}>{article.title}</Link></h3><p>{article.intro}</p><Link className="read-link" href={`/blog/${article.slug}`}>Ler artigo</Link></div></article>)}</div></section></div></main><SiteFooter/></div>}
