"""Gera as artes a partir dos textos aprovados, preservando a redação."""
from pathlib import Path
import ast
import html
import json
import re
import shutil

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'marketing/posts/2026-10-05-conversas-com-as-familias'
SOURCE = OUT / 'textos-para-revisao.md'
PREVIOUS = ROOT / 'marketing/posts/2026-10-05-carrosseis-estreia'
e = html.escape

# Reutiliza a base tipográfica aprovada sem executar o gerador anterior.
tree = ast.parse((ROOT / 'scripts/site/gerar_carrosseis_estreia.py').read_text())
css = next(ast.literal_eval(node.value) for node in tree.body
           if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'css' for t in node.targets))
css += '''
.content{gap:38px}.content h2{font-size:84px;max-width:850px}.copy p{font-size:38px;line-height:1.5}.copy{display:flex;flex-direction:column;gap:25px}.long-title h2{font-size:77px}.cover .content{padding-top:112px;gap:39px}.cover h1{font-size:106px;max-width:880px}.cover .copy p{font-size:35px;max-width:780px}.cover .bottom-note{font:400 19px/1.6 Arial,sans-serif;letter-spacing:3px;text-transform:uppercase;bottom:30px;color:#746c71}.cover .arch{bottom:80px;right:-170px;width:560px;height:380px;opacity:.7}.quote .content{padding-top:50px;gap:42px}.quote h2{border-left:4px solid #c89ab0;padding-left:34px}.quote .copy{padding-left:38px;max-width:850px}.quote .quote-mark{font:180px/.5 Georgia,serif;color:#c79aad;display:block;height:90px;margin-bottom:8px}.editorial .content{justify-content:flex-start;padding-top:120px}.editorial .copy{border-left:3px solid #a9bfce;padding-left:33px;max-width:840px;margin-top:12px}.reflection .content{gap:42px}.reflection h2{max-width:850px}.reflection .motif{display:flex;gap:14px;margin-top:30px}.reflection .motif i{display:block;width:52px;height:52px;border:1px solid #acbfcd;border-radius:50%}.reflection .motif i:nth-child(2){background:#ffffff70;border-color:#cea8ba}.reflection .motif i:nth-child(3){width:100px;border-radius:35px}.cta .content{padding-top:35px;gap:35px}.cta h2{font-size:90px}.cta .copy p{font-size:36px}.cta .save-copy{font-size:28px!important;margin-top:18px;padding:24px 12px 0;border-top:1px solid #c9aab9;max-width:770px}.cta .cta-logo{margin-bottom:10px}.cta .kicker{font-size:17px}.slide-footer .series{font-size:14px}.white .arch:after{background:#eaf2f860}
'''

def paragraphs(text):
    return ''.join(f'<p>{e(p)}</p>' for p in text.split('\n\n'))

slugs = ['04-filmes-e-conversas', '05-frustracao-na-infancia', '06-dialogo-com-adolescentes']
labels = ['FILMES E EMOÇÕES', 'FRUSTRAÇÃO NA INFÂNCIA', 'DIÁLOGO NA ADOLESCÊNCIA']
kickers = [
    ['', 'UMA CENA DO COTIDIANO', 'EMOÇÕES EM CENA', 'O OLHAR DA CRIANÇA', 'NO TEMPO DA CONVERSA', 'UM MOMENTO EM FAMÍLIA'],
    ['', 'O FIM DA BRINCADEIRA', 'DAR NOME AO SENTIMENTO', 'ACOLHIMENTO E LIMITES', 'TEMPO PARA SE ACALMAR', 'QUEM CUIDA TAMBÉM PRECISA'],
    ['', 'UM COMEÇO POSSÍVEL', 'ESPAÇO PARA CONVERSAR', 'ESCUTAR COM ATENÇÃO', 'DIFERENTES PERSPECTIVAS', 'PRESENÇA E DISPONIBILIDADE'],
]
(OUT / 'assets').mkdir(exist_ok=True)
shutil.copy2(ROOT / 'identidade/logo.jpg', OUT / 'assets/logo.jpg')
parts = re.split(r'\n## Post \d+ — ', SOURCE.read_text())[1:]
posts = []
for pi, part in enumerate(parts):
    title = part.split('\n', 1)[0]
    folder = OUT / slugs[pi]
    folder.mkdir(exist_ok=True)
    block = part.split('### Texto completo dos slides\n\n')[1].split('\n### Legenda')[0].strip()
    matches = re.findall(r'\*\*(\d+) — (.+?)\*\*\n+(.*?)(?=\n\*\*\d+ — |\Z)', block, re.S)
    assert len(matches) == 7
    caption = part.split('### Legenda\n\n')[1].split('\n### Base editorial')[0].strip()
    sources = part.split('### Base editorial e fontes\n\n')[1].split('\n## Direção')[0].strip()
    (folder / 'legenda.md').write_text(caption + '\n')
    (folder / 'texto.md').write_text(f'# {title}\n\nTextos aprovados pelo usuário em 05/10/2026. Conteúdo educativo para validar com a responsável técnica antes da publicação.\n\n{block}\n\n## Legenda\n\n{caption}\n\n## Fontes editoriais\n\n{sources}\n')
    slides, data, alt = [], [], []
    colors = [ ['white','blue','white','pink','white','blue','pink'],
               ['blue','white','pink','white','blue','white','pink'],
               ['pink','white','blue','white','pink','white','blue'] ][pi]
    for number, headline, body in matches:
        n = int(number)
        body = body.strip()
        data.append(dict(number=n, headline=headline, body=body))
        header = f'<header class="slide-header"><div class="brand"><img src="../assets/logo.jpg" alt="Logo Psin Clínica"><span>Psin Clínica</span></div><span class="count">{n:02d} / 07</span></header>'
        footer = f'<footer class="slide-footer"><span>@psinclinicapsicologia</span><span class="series">{"CONVERSAS COM AS FAMÍLIAS" if n == 7 else "CONTINUE A LEITURA"}</span></footer>'
        klass = colors[n-1]
        if n == 1:
            klass += ' cover'
            content = f'<div class="content"><p class="kicker">{labels[pi]}</p><h1>{e(headline)}</h1><div class="rule"></div><div class="copy">{paragraphs(body)}</div><span class="bottom-note">Conversas com as famílias · {pi+4:02d}</span></div><div class="arch" aria-hidden="true"></div>'
        elif n == 7:
            klass += ' cta'
            text, call = body.rsplit('\n\n', 1)
            content = f'<div class="content"><img class="cta-logo" src="../assets/logo.jpg" alt=""><p class="kicker">CONVERSAS COM AS FAMÍLIAS</p><h2>{e(headline)}</h2><div class="rule"></div><div class="copy">{paragraphs(text)}<p class="save-copy">{e(call)}</p></div></div>'
        else:
            layout = ['quote','editorial','reflection','editorial','reflection'][n-2]
            klass += ' ' + layout + (' long-title' if len(headline)>43 else '')
            marker = '<span class="quote-mark" aria-hidden="true">“</span>' if layout == 'quote' else ''
            motif = '<div class="motif" aria-hidden="true"><i></i><i></i><i></i></div>' if layout == 'reflection' else ''
            content = f'<div class="content"><p class="kicker">{kickers[pi][n-1]}</p>{marker}<h2>{e(headline)}</h2><div class="rule"></div><div class="copy">{paragraphs(body)}</div>{motif}</div>'
        slides.append(f'<article class="slide {klass}" id="slide-{n:02d}" aria-label="Slide {n}: {e(headline)}">{header}{content}{footer}</article>')
        alt.append(f'## Slide {n:02d}\n\nArte da Psin Clínica com fundo {dict(white="branco",blue="azul claro",pink="rosa claro")[colors[n-1]]}. {headline} {body.replace(chr(10), " ")}\n')
    (folder / 'carrossel.html').write_text(f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(title)} — Psin Clínica</title><style>{css}</style></head><body>{"".join(slides)}</body></html>')
    (folder / 'conteudo.json').write_text(json.dumps(data, ensure_ascii=False, indent=2))
    (folder / 'texto-alternativo.md').write_text('# Texto alternativo para as imagens\n\n' + '\n'.join(alt))
    shutil.copy2(PREVIOUS / '01-conheca-a-psin/render.js', folder / 'render.js')
    posts.append(dict(slug=slugs[pi], title=title, caption=caption, slides=data))
(OUT / 'posts.json').write_text(json.dumps(posts, ensure_ascii=False, indent=2))
shutil.copy2(PREVIOUS / 'render-all.js', OUT / 'render-all.js')

gallery_css = re.search(r'<style>(.*?)</style>', (PREVIOUS/'index.html').read_text(), re.S)[1]
gallery_css += '.grid{grid-template-columns:repeat(4,minmax(0,1fr))}@media(max-width:1000px){.grid{grid-template-columns:repeat(2,minmax(0,1fr))}}@media(max-width:560px){.grid{grid-template-columns:1fr}}'
sections = []
for post in posts:
    cards = ''.join(f'<a class="slide-preview" href="{post["slug"]}/instagram/slide-{s["number"]:02d}.png" target="_blank"><img src="{post["slug"]}/instagram/slide-{s["number"]:02d}.png" alt="{e(s["headline"]+" "+s["body"])}" width="1080" height="1350"><span>{s["number"]:02d} · {e(s["headline"])}</span></a>' for s in post['slides'])
    sections.append(f'<section id="{post["slug"]}"><div class="section-heading"><div><p class="eyebrow">CARROSSEL {post["slug"][:2]} · 7 SLIDES</p><h2>{e(post["title"])}</h2></div><a class="download" href="{post["slug"]}/legenda.md" download>Baixar legenda</a></div><div class="grid">{cards}</div><details><summary>Ler a legenda</summary><div class="caption">{e(post["caption"])}</div></details></section>')
nav = ''.join(f'<a href="#{p["slug"]}">{label}</a>' for p,label in zip(posts,['Filmes e emoções','Frustração na infância','Diálogo com adolescentes']))
(OUT / 'index.html').write_text(f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Conversas com as famílias — Psin Clínica</title><style>{gallery_css}</style></head><body><div class="wrap"><header><p class="eyebrow">PSIN CLÍNICA · INSTAGRAM</p><h1>Pequenas situações.<br>Conversas que aproximam.</h1><p>Três carrosséis educativos com os textos aprovados. Abra uma arte para ver em tamanho original e encontre a legenda ao final de cada sequência.</p><nav>{nav}<a href="carrosseis-educativos-psin.zip" download>Baixar o pacote completo</a></nav></header>{"".join(sections)}<footer>Textos aprovados pelo usuário em 05/10/2026. Artes para revisão. Conteúdo educativo para validar com a responsável técnica antes da publicação. Publicação não realizada.</footer></div></body></html>')
contact_rows = ''.join('<section><h2>'+e(p['title'])+'</h2><div>'+''.join(f'<img src="{p["slug"]}/instagram/slide-{s["number"]:02d}.png" alt="Slide {s["number"]}">' for s in p['slides'])+'</div></section>' for p in posts)
(OUT / 'contato-visual.html').write_text(f'<!doctype html><html lang="pt-BR"><meta charset="utf-8"><title>Visão geral</title><style>body{{margin:0;padding:35px;background:#f6f4f5;color:#4f4d4e}}h2{{font:28px Georgia}}section{{margin-bottom:35px}}section>div{{display:grid;grid-template-columns:repeat(7,1fr);gap:16px}}img{{width:100%;display:block}}</style>{contact_rows}</html>')
(OUT / 'README.md').write_text('''# Psin Clínica — carrosséis educativos

Textos aprovados pelo usuário em 05/10/2026. Artes para revisão. Conteúdo educativo para validar com a responsável técnica antes da publicação.

- Abra `index.html` para revisar os três carrosséis e as legendas.
- Cada pasta contém sete PNGs em `instagram/`, em ordem de publicação, a legenda, texto alternativo, conteúdo e HTML editável.
- `carrosseis-educativos-psin.zip` reúne os arquivos desta entrega.
- Nenhum conteúdo foi publicado. Os carrosséis institucionais anteriores permanecem na própria pasta.

## Regenerar

Na raiz do projeto, execute `python3 scripts/site/gerar_carrosseis_educativos.py` e depois `NODE_PATH=/private/tmp/psin-preview-tools/node_modules node marketing/posts/2026-10-05-conversas-com-as-familias/render-all.js`. Requer Node, Playwright e Google Chrome. `CHROME_PATH` permite indicar outro executável.

As fontes editoriais e a redação aprovada estão em `textos-para-revisao.md`.
''')
print('3 carrosséis gerados: 21 slides, legendas, textos alternativos e galeria.')
