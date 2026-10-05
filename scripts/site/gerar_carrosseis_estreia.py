from pathlib import Path
import re, html, json
ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/'marketing/posts/2026-10-04-estreia-do-perfil/textos-para-revisao.md'
OUT=ROOT/'marketing/posts/2026-10-05-carrosseis-estreia'
parts=re.split(r'\n## Post \d+ — ',SOURCE.read_text())[1:]
slugs=['01-conheca-a-psin','02-como-comeca-o-atendimento','03-conheca-a-equipe']
e=html.escape
css='''
*{box-sizing:border-box}body{margin:0;background:#ddd;color:#4f4d4e;font-family:Arial,Helvetica,sans-serif}.slide{width:1080px;height:1350px;position:relative;overflow:hidden;background:#fff;margin:0 auto 30px;padding:70px 84px;isolation:isolate}.blue{background:#eaf2f8}.pink{background:#f8e7ef}.slide-header{height:84px;display:flex;align-items:center;justify-content:space-between;position:relative;z-index:2}.brand{display:flex;align-items:center;gap:15px}.brand img{width:76px;height:76px;border-radius:50%;background:white;object-fit:contain}.brand span{font:400 25px Georgia,serif;letter-spacing:-.5px}.count{font-size:19px;letter-spacing:3px;color:#736a70}.content{height:980px;padding:62px 0 28px;display:flex;flex-direction:column;justify-content:center;gap:30px;position:relative;z-index:1}.kicker{font-size:18px;font-weight:600;letter-spacing:3.4px;line-height:1.5;text-transform:uppercase;color:#886579;margin:0}.rule{width:76px;height:3px;background:#c889a6;flex-shrink:0}h1,h2{font-family:Georgia,serif;font-weight:400;letter-spacing:-2.6px;line-height:1.07;margin:0;text-wrap:balance}h1{font-size:104px}h2{font-size:82px}p{font-size:38px;line-height:1.48;margin:0;text-wrap:pretty}.copy{max-width:860px}.slide-footer{position:absolute;left:84px;right:84px;bottom:68px;display:flex;justify-content:space-between;align-items:center;border-top:1px solid #c9bec65c;padding-top:23px;font-size:19px;letter-spacing:.3px;z-index:2}.slide-footer .series{font-size:15px;letter-spacing:1.8px;text-transform:uppercase}.cover .content{justify-content:flex-start;padding-top:115px;gap:35px}.cover h1{max-width:840px}.cover p{max-width:715px;font-size:34px}.cover .rule{margin-top:12px}.arch{position:absolute;z-index:0;width:600px;height:570px;right:-105px;bottom:-30px;border:1px solid #caa7b947;border-radius:330px 330px 0 0;transform:rotate(-18deg)}.arch:before{content:'';position:absolute;inset:45px;border:1px solid #caa7b94d;border-radius:inherit}.arch:after{content:'';position:absolute;inset:90px;background:#eaf2f875;border-radius:inherit}.blue .arch{border-color:#9cb6ca50}.blue .arch:after{background:#ffffff65}.pink .arch:after{background:#ffffff60}.cover .bottom-note{position:absolute;left:0;bottom:90px;font:italic 46px/1.25 Georgia,serif;color:#9b7084;max-width:630px}.cover.team-cover .bottom-note{font:400 27px/1.9 Arial,sans-serif;color:#6f636a;max-width:650px}.cover.process-cover h1{font-size:102px;max-width:780px}.cover.team-cover h1{max-width:780px}.audience .content{justify-content:flex-start;padding-top:100px;gap:35px}.audience h2{max-width:800px}.audience .copy{max-width:800px}.audiences{display:flex;flex-wrap:wrap;gap:13px;margin-top:40px}.audiences span{font:400 28px Georgia,serif;border:1px solid #adc4d5;border-radius:50px;padding:17px 27px}.photo-layout .content{gap:25px;padding-top:45px}.photo-layout h2{font-size:74px}.photo-layout .photo{width:100%;height:370px;border-radius:120px 12px 12px 12px;object-fit:cover;object-position:center;display:block}.photo-layout p{font-size:32px;line-height:1.45}.photo-layout .address{font-size:30px;line-height:1.4}.photo-layout .copy{display:flex;flex-direction:column;gap:14px}.family .content{gap:40px}.family h2{font-size:91px;max-width:800px}.family .copy{border-left:3px solid #d4a1b7;padding-left:33px}.family .corner{position:absolute;right:100px;top:175px;width:95px;height:95px;border-radius:50%;border:1px solid #d9c2cc}.profession .content{gap:42px}.profession h2{max-width:850px}.profession .copy{max-width:785px}.photo-split .content{display:grid;grid-template-columns:1fr .8fr;gap:40px;align-content:center;align-items:center}.photo-split .text{display:flex;flex-direction:column;gap:28px}.photo-split h2{font-size:74px}.photo-split p{font-size:32px;line-height:1.45}.photo-split .content img{width:100%;height:650px;object-fit:cover;object-position:center;border-radius:190px 190px 12px 12px}.step .content{gap:33px;padding-top:50px}.step h2{font-size:84px;max-width:800px}.step .step-marker{font:400 135px/1 Georgia,serif;color:#92afc3;margin-bottom:15px;letter-spacing:-6px}.step.pink .step-marker{color:#c295aa}.step .copy{max-width:850px}.profile .content{justify-content:flex-start;padding-top:82px;gap:0}.profile .kicker{margin-bottom:44px}.profile h2{font-size:78px;line-height:1.08;min-height:252px;max-width:855px;display:flex;align-items:flex-start}.profile .credential{font-size:27px;line-height:1.5;min-height:48px;margin:15px 0 35px;color:#716871}.profile .rule{margin-bottom:35px}.profile .copy{font-size:36px;line-height:1.52;max-width:850px}.monogram{font:400 150px/1 Georgia,serif;color:#8ea7b820;position:absolute;bottom:16px;right:0;letter-spacing:-9px}.profile.pink .monogram{color:#be8ea42b}.cta .content{text-align:center;align-items:center;gap:33px;padding-top:46px}.cta .cta-logo{width:100px;height:100px;border-radius:50%;background:#fff;object-fit:contain}.cta h2{font-size:94px;max-width:870px}.cta p{max-width:810px;font-size:35px;line-height:1.48}.cta .cta-label{margin-top:13px;font-size:22px;letter-spacing:2px;padding:20px 37px;border-radius:45px;border:1px solid #bfa5b2}.cta.long h2{font-size:86px}.cta.long p{font-size:34px}.cta .rule{background:#b7849c}.cover .kicker,.photo-layout .kicker,.photo-split .kicker{font-size:18px;line-height:1.5}.readable{overflow:visible}@media print{body{background:none}.slide{margin:0;break-after:page}@page{size:1080px 1350px;margin:0}}
'''
def header(n):return f'<header class="slide-header"><div class="brand"><img src="../assets/logo.jpg" alt="Logo Psin Clínica"><span>Psin Clínica</span></div><span class="count">{n:02d} / 06</span></header>'
def footer(series,n):return f'<footer class="slide-footer"><span>@psinclinicapsicologia</span><span class="series">{series if n==6 else "CONTINUE A LEITURA"}</span></footer>'
def paragraphs(text):return ''.join(f'<p>{e(x)}</p>' for x in text.split('\n') if x)
posts=[]
for pi,part in enumerate(parts):
 title=part.split('\n',1)[0]; folder=OUT/slugs[pi]; folder.mkdir(parents=True,exist_ok=True)
 block=part.split('### Texto completo dos slides\n\n')[1].split('\n### Legenda')[0]
 matches=re.findall(r'\*\*(\d+) — (.+?)\*\*\n(.*?)(?=\n\*\*\d+ — |\Z)',block,re.S)
 assert len(matches)==6
 caption=part.split('### Legenda\n\n')[1].split('\n### Direção visual')[0].strip()
 (folder/'legenda.md').write_text(caption+'\n')
 (folder/'texto.md').write_text('# '+title+'\n\nTexto aprovado em 05/10/2026.\n\n'+block+'\n\n## Legenda\n\n'+caption+'\n')
 slides=[]; data=[]
 for number,headline,body in matches:
  n=int(number); body=body.strip(); data.append({'number':n,'headline':headline,'body':body})
  bg=['white','blue','white','pink','white','pink'][n-1]
  klass=bg; content=''
  series=['CONHEÇA A PSIN','O ATENDIMENTO','NOSSA EQUIPE'][pi]
  if n==1:
   klass=['white cover','blue cover process-cover','pink cover team-cover'][pi]
   note=['Psicologia e psicanálise.','Um encontro de cada vez.','Allice · Sandson<br>Emanuele · Suely'][pi]
   content=f'<div class="content"><p class="kicker">{series}</p><h1>{e(headline)}</h1><div class="rule"></div><div class="copy">{paragraphs(body)}</div><span class="bottom-note">{note}</span></div><div class="arch" aria-hidden="true"></div>'
  elif n==6:
   klass='pink cta'+(' long' if pi else '')
   content=f'<div class="content"><img class="cta-logo" src="../assets/logo.jpg" alt=""><h2>{e(headline)}</h2><div class="rule"></div><div class="copy">{paragraphs(body)}</div><span class="cta-label">ACESSE O LINK DA BIO</span></div>'
  elif pi==2:
   klass=('blue' if n%2==0 else 'white')+' profile'
   if n==5:klass='white profile'
   credential,desc=body.split('\n',1)
   mono=['AG','SB','EM','SM'][n-2]
   content=f'<div class="content"><p class="kicker">NOSSA EQUIPE</p><h2>{e(headline)}</h2><p class="credential">{e(credential)}</p><div class="rule"></div><div class="copy">{e(desc)}</div><span class="monogram" aria-hidden="true">{mono}</span></div>'
  elif pi==0 and n==2:
   klass='blue audience';content=f'<div class="content"><p class="kicker">DE QUEM CUIDAMOS</p><h2>{e(headline)}</h2><div class="rule"></div><div class="copy">{paragraphs(body)}</div><div class="audiences"><span>Infância</span><span>Adolescência</span><span>Vida adulta</span></div></div>'
  elif pi==0 and n==3:
   klass='white family';content=f'<div class="content"><p class="kicker">CRIANÇAS E FAMÍLIAS</p><h2>{e(headline)}</h2><div class="copy">{paragraphs(body)}</div></div><span class="corner" aria-hidden="true"></span>'
  elif pi==0 and n==4:
   klass='pink profession';content=f'<div class="content"><p class="kicker">FORMAÇÕES E ABORDAGENS</p><h2>{e(headline)}</h2><div class="rule"></div><div class="copy">{paragraphs(body)}</div></div>'
  elif pi==0 and n==5:
   klass='white photo-layout';lines=body.split('\n');content=f'<div class="content"><p class="kicker">NOSSO ESPAÇO</p><h2>{e(headline)}</h2><img class="photo" src="../assets/recepcao.png" alt="Recepção da Psin Clínica"><div class="copy"><p class="address">{e(lines[0])}<br>{e(lines[1])}</p>{paragraphs(chr(10).join(lines[2:]))}</div></div>'
  elif pi==1 and n==3:
   klass='white photo-split';content=f'<div class="content"><div class="text"><p class="kicker">PRIMEIROS ENCONTROS</p><h2>{e(headline)}</h2><div class="rule"></div>{paragraphs(body)}</div><img src="../assets/sala.png" alt="Sala de atendimento da Psin Clínica"></div>'
  else:
   klass=('pink' if n in (2,4) else 'blue')+' step'
   content=f'<div class="content"><span class="step-marker">{n-1:02d}</span><h2>{e(headline)}</h2><div class="rule"></div><div class="copy">{paragraphs(body)}</div></div>'
  slides.append(f'<article class="slide {klass}" id="slide-{n:02d}" aria-label="Slide {n}: {e(headline)}">{header(n)}{content}{footer(series,n)}</article>')
 page=f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(title)} — Psin Clínica</title><style>{css}</style></head><body>{"".join(slides)}</body></html>'
 (folder/'carrossel.html').write_text(page)
 (folder/'conteudo.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 posts.append({'slug':slugs[pi],'title':title,'caption':caption,'slides':data})
(OUT/'posts.json').write_text(json.dumps(posts,ensure_ascii=False,indent=2))
print(f'{len(posts)} carrosséis, 18 slides, legendas e fontes HTML preparados.')
