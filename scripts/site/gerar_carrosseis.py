"""Gera os oito carrosséis da Psin Clínica (versão 2).

Lê o conteúdo de `carrosseis_conteudo.py` e monta, para cada carrossel,
`carrossel.html`, `texto.md`, `legenda.md` e `texto-alternativo.md`.
Também gera `textos-para-revisao.md` e a galeria `index.html`.
Depois, renderizar os PNGs com `render-all.js` (Node + Playwright).
"""
from pathlib import Path
import html
import json
import shutil
import sys

sys.path.insert(0, str(Path(__file__).parent))
from carrosseis_conteudo import CARROSSEIS, HANDLE  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'marketing/posts/2026-10-05-carrosseis'
IMAGES = ROOT / 'saidas/2026-10-03-reuniao/site/dist/images'
e = html.escape

CSS = r'''
:root{
  --ink:#3A3638; --muted:#6E6669; --rose:#E0628F; --rose-text:#C2477A; --rose-soft:#FBE4EC;
  --blue:#94C0E6; --blue-text:#3E6F96; --blue-soft:#E5EFF8; --deep:#24435C; --cream:#FBF8F5;
}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#d9d4d6;font-family:Inter,Arial,sans-serif;color:var(--ink);display:flex;flex-direction:column;align-items:center;gap:40px;padding:40px 0}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;display:flex;flex-direction:column;padding:72px 90px 64px;background:#fff}
.slide.branco{background:#fff}
.slide.azul{background:var(--blue-soft)}
.slide.rosa{background:var(--rose-soft)}
.slide.creme{background:var(--cream)}
.slide.profundo{background:var(--deep);color:#fff}
.slide.destaque{background:var(--rose);color:#fff}

/* topo e rodapé */
.top{display:flex;justify-content:space-between;align-items:center;position:relative;z-index:3}
.brand{display:flex;align-items:center;gap:16px;font:600 22px/1 Inter,sans-serif;letter-spacing:.01em}
.brand .chip{width:64px;height:64px;border-radius:18px;background:#fff;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 10px rgba(36,67,92,.10)}
.brand img{width:52px;height:52px;object-fit:contain}
.count{font:600 20px/1 Inter,sans-serif;letter-spacing:.18em;color:var(--muted)}
.profundo .count,.destaque .count,.photo-cover .count{color:rgba(255,255,255,.75)}
.bottom{margin-top:auto;display:flex;justify-content:space-between;align-items:center;padding-top:26px;border-top:1.5px solid rgba(58,54,56,.14);font:600 20px/1 Inter,sans-serif;color:var(--muted);position:relative;z-index:3}
.profundo .bottom,.destaque .bottom,.photo-cover .bottom{border-color:rgba(255,255,255,.28);color:rgba(255,255,255,.85)}
.bottom .swipe{letter-spacing:.16em;text-transform:uppercase;font-size:17px}

/* tipografia */
.kicker{font:700 20px/1.2 Inter,sans-serif;letter-spacing:.22em;text-transform:uppercase;color:var(--rose-text)}
.azul .kicker{color:var(--blue-text)}
.profundo .kicker,.destaque .kicker,.photo-cover .kicker{color:#F6B9CF}
.rule{width:84px;height:5px;border-radius:3px;background:var(--rose)}
.azul .rule{background:var(--blue-text)}
h1,h2{font-family:Fraunces,Georgia,serif;font-weight:500;letter-spacing:-.012em;font-variation-settings:"opsz" 60,"SOFT" 50}
h1{letter-spacing:-.008em;font-variation-settings:"opsz" 96,"SOFT" 50}
h1{font-size:116px;line-height:1.0}
h2{font-size:88px;line-height:1.04}
p.body{font:400 40px/1.45 Inter,sans-serif;color:#4C4749;max-width:880px}
.profundo p.body,.destaque p.body{color:rgba(255,255,255,.9)}
em.hl{font-style:normal;color:var(--rose-text)}

.main{flex:1;display:flex;flex-direction:column;justify-content:center;gap:34px;position:relative;z-index:2}

/* tags */
.tags{display:flex;flex-wrap:wrap;gap:16px}
.tags span{font:600 26px/1 Inter,sans-serif;padding:18px 30px;border-radius:999px;background:var(--rose-soft);color:var(--rose-text)}
.rosa .tags span{background:#fff}

/* capa com foto */
.photo-cover{color:#fff}
.photo-cover .bg{position:absolute;inset:0;background-size:cover;z-index:0}
.photo-cover:after{content:"";position:absolute;inset:0;z-index:1;background:linear-gradient(180deg,rgba(28,38,48,.30) 0%,rgba(28,38,48,.08) 30%,rgba(28,38,48,.55) 58%,rgba(24,34,44,.92) 100%)}
.photo-cover .main{justify-content:flex-end;padding-bottom:20px}
.photo-cover h1{font-size:104px;text-shadow:0 2px 24px rgba(0,0,0,.25)}
.photo-cover p.body{color:rgba(255,255,255,.92);font-size:36px}

/* espaço para imagem a inserir */
.placeholder{position:relative;border:4px dashed #B9A9B1;border-radius:28px;background:repeating-linear-gradient(-45deg,#F3ECEF 0 22px,#ECE3E8 22px 44px);display:flex;flex-direction:column;justify-content:center;gap:16px;padding:40px 48px;color:#5B5357}
.placeholder b{font:800 22px/1.2 Inter,sans-serif;letter-spacing:.2em;text-transform:uppercase;color:var(--rose-text)}
.placeholder span{font:500 25px/1.42 Inter,sans-serif}
.photo-cover .placeholder.full{position:absolute;inset:0;border-radius:0;border:none;justify-content:flex-start;padding:200px 90px 0;background:repeating-linear-gradient(-45deg,#9DB7CC 0 26px,#93AFC6 26px 52px)}
.photo-cover .placeholder.full .ph-box{border:4px dashed rgba(255,255,255,.85);border-radius:28px;padding:34px 40px;background:rgba(36,67,92,.55);display:flex;flex-direction:column;gap:14px;color:#fff}
.photo-cover .placeholder.full b{color:#FFD3E2}
.photo-cover .placeholder.full span{font-size:25px;color:#fff}

/* capa de cor */
.cover-color h1{font-size:118px}
.cover-color .main{justify-content:center}
.cover-color .deco{position:absolute;right:-180px;bottom:-200px;width:680px;height:680px;border-radius:50%;z-index:1}
.profundo .deco{background:radial-gradient(circle at 35% 35%,rgba(148,192,230,.35),rgba(148,192,230,0) 70%)}
.rosa .deco{background:radial-gradient(circle at 35% 35%,rgba(224,98,143,.22),rgba(224,98,143,0) 70%)}
.azul .deco{background:radial-gradient(circle at 35% 35%,rgba(62,111,150,.20),rgba(62,111,150,0) 70%)}

/* número */
.num{font-family:Fraunces,Georgia,serif;font-weight:400;font-size:260px;line-height:.82;letter-spacing:-.04em;color:var(--rose)}
.azul .num{color:var(--blue-text)}
.profundo .num{color:#F6B9CF;font-size:230px}
.num-row{display:flex;align-items:flex-end;gap:28px}
.num-row .kicker{padding-bottom:22px}

/* citação */
.quote-mark{font-family:Fraunces,Georgia,serif;font-size:300px;line-height:.6;height:110px;margin-top:70px;color:var(--rose);opacity:.85}
.azul .quote-mark{color:var(--blue-text)}
.profundo .quote-mark{color:#F6B9CF}
.citacao h2{font-size:92px;font-style:italic;font-weight:400}
.citacao .main{gap:30px}

/* foto dividida */
.split{padding:0}
.split .ph{height:600px;flex-shrink:0;position:relative;background-size:cover}
.split .ph .placeholder{position:absolute;inset:0;border-radius:0;border:none;border-bottom:4px dashed #B9A9B1;padding:150px 90px 40px}
.split .top{position:absolute;left:90px;right:90px;top:72px}
.split .ph .count{color:#fff;text-shadow:0 1px 6px rgba(0,0,0,.4)}
.split .ph.empty .count{color:var(--muted);text-shadow:none}
.split .text{flex:1;display:flex;flex-direction:column;padding:56px 90px 64px}
.split .main{justify-content:flex-start;gap:26px}
.split h2{font-size:76px}
.split p.body{font-size:36px}
.split .numtag{font-family:Fraunces,Georgia,serif;font-size:96px;line-height:.8;color:var(--rose)}

/* lista */
.list{display:flex;flex-direction:column;gap:22px;margin-top:10px}
.list div{display:flex;align-items:center;gap:30px;background:var(--rose-soft);border-radius:28px;padding:30px 36px;font:500 36px/1.3 Inter,sans-serif}
.list div:nth-child(2){background:var(--blue-soft)}
.list i{font-style:normal;font-family:Fraunces,Georgia,serif;font-size:64px;line-height:1;color:var(--rose);min-width:52px}
.list div:nth-child(2) i{color:var(--blue-text)}

/* perfil */
.perfil .main{justify-content:center;gap:28px}
.portrait{width:300px;height:300px;border-radius:50%;position:relative;overflow:hidden;flex-shrink:0}
.portrait .placeholder{position:absolute;inset:0;border-radius:50%;padding:40px 46px;text-align:center;align-items:center;gap:8px}
.portrait .placeholder b{font-size:17px}
.portrait .placeholder span{font-size:19px;line-height:1.3}
.portrait .initials{position:absolute;right:-6px;bottom:-6px}
.perfil h2{font-size:80px}
.credential{font:600 26px/1.3 Inter,sans-serif;color:var(--rose-text);letter-spacing:.02em}
.azul .credential{color:var(--blue-text)}
.perfil .ghost{position:absolute;right:70px;bottom:120px;font-family:Fraunces,Georgia,serif;font-size:260px;line-height:1;color:rgba(58,54,56,.05);z-index:1}

/* CTA */
.cta{background:var(--rose);color:#fff;text-align:center}
.cta .main{align-items:center;justify-content:center;gap:34px}
.cta .logo-big{width:150px;height:150px;border-radius:40px;background:#fff;display:flex;align-items:center;justify-content:center;box-shadow:0 10px 30px rgba(120,30,70,.18)}
.cta .logo-big img{width:120px;height:120px;object-fit:contain}
.cta h2{font-size:92px;max-width:880px}
.cta p.body{color:#fff;max-width:840px;font-size:38px}
.cta .button{font:700 26px/1 Inter,sans-serif;letter-spacing:.14em;text-transform:uppercase;background:#fff;color:var(--rose-text);padding:26px 46px;border-radius:999px}
.cta .note{font:500 26px/1.4 Inter,sans-serif;color:#fff;border-top:2px solid rgba(255,255,255,.45);padding-top:24px;max-width:700px}
.cta .bottom{border-color:rgba(255,255,255,.4);color:rgba(255,255,255,.9)}
.cta .count{color:rgba(255,255,255,.8)}
'''


def slide_html(s, i, total, assets_rel):
    n = f'{i:02d} / {total:02d}'
    layout = s['layout']
    fundo = s.get('fundo', 'branco')
    logo = f'<img src="{assets_rel}/logo.jpg" alt="">'
    top = f'<div class="top"><div class="brand"><span class="chip">{logo}</span>Psin Clínica</div><span class="count">{n}</span></div>'
    last = i == total
    bottom = f'<div class="bottom"><span>{HANDLE}</span><span class="swipe">{"" if last else "Arraste →"}</span></div>'
    kicker = f'<div class="kicker">{e(s["kicker"])}</div>' if s.get('kicker') else ''
    titulo = s['titulo']  # pode conter <br>
    body = f'<p class="body">{e(s["texto"])}</p>' if s.get('texto') else ''
    tags = ''.join(f'<span>{e(t)}</span>' for t in s.get('tags', []))
    tags = f'<div class="tags">{tags}</div>' if tags else ''

    def placeholder(desc, extra=''):
        return f'<div class="placeholder {extra}"><b>Imagem a inserir</b><span>{e(desc)}</span></div>'

    if layout == 'capa_foto':
        if s.get('foto'):
            bg = f'<div class="bg" style="background-image:url({assets_rel}/{s["foto"]});background-position:{s.get("foco", "center")}"></div>'
        else:
            bg = f'<div class="placeholder full"><div class="ph-box"><b>Imagem a inserir · foto de capa</b><span>{e(s["imagem_a_inserir"])}</span></div></div>'
        return f'''<section class="slide photo-cover">{bg}{top}<div class="main">{kicker}<h1>{titulo}</h1><div class="rule"></div>{body}</div>{bottom}</section>'''
    if layout == 'capa_cor':
        return f'''<section class="slide cover-color {fundo}"><div class="deco"></div>{top}<div class="main">{kicker}<h1>{titulo}</h1><div class="rule"></div>{body}{tags}</div>{bottom}</section>'''
    if layout == 'texto':
        return f'''<section class="slide {fundo}">{top}<div class="main">{kicker}<div class="rule"></div><h2>{titulo}</h2>{body}{tags}</div>{bottom}</section>'''
    if layout == 'numero':
        k = f'<div class="kicker">{e(s["kicker"])}</div>' if s.get('kicker') else ''
        return f'''<section class="slide {fundo}">{top}<div class="main"><div class="num-row"><div class="num">{e(s["numero"])}</div>{k}</div><h2>{titulo}</h2>{body}</div>{bottom}</section>'''
    if layout == 'citacao':
        return f'''<section class="slide citacao {fundo}">{top}<div class="main">{kicker}<div class="quote-mark">“</div><h2>{titulo}</h2><div class="rule"></div>{body}</div>{bottom}</section>'''
    if layout == 'foto':
        if s.get('foto'):
            ph = f'<div class="ph" style="background-image:url({assets_rel}/{s["foto"]});background-position:{s.get("foco", "center")}">'
        else:
            ph = f'<div class="ph empty">{placeholder(s["imagem_a_inserir"])}'
        numtag = f'<div class="numtag">{e(s["numero"])}</div>' if s.get('numero') else kicker
        return f'''<section class="slide split {fundo}">{ph}{top}</div><div class="text"><div class="main">{numtag}<h2>{titulo}</h2>{body}</div>{bottom}</div></section>'''
    if layout == 'lista':
        items = ''.join(f'<div><i>{k}</i>{e(t)}</div>' for k, t in enumerate(s['itens'], 1))
        return f'''<section class="slide {fundo}">{top}<div class="main">{kicker}<div class="rule"></div><h2>{titulo}</h2><div class="list">{items}</div></div>{bottom}</section>'''
    if layout == 'perfil':
        return f'''<section class="slide perfil {fundo}">{top}<div class="ghost">{e(s["iniciais"])}</div><div class="main"><div class="portrait">{placeholder(s["imagem_a_inserir"])}</div><h2>{e(titulo)}</h2><div class="credential">{e(s["registro"])}</div><div class="rule"></div>{body}</div>{bottom}</section>'''
    if layout == 'cta':
        extra = ''
        if s.get('botao'):
            extra += f'<div class="button">{e(s["botao"])}</div>'
        if s.get('nota'):
            extra += f'<div class="note">{e(s["nota"])}</div>'
        return f'''<section class="slide cta">{top}<div class="main"><div class="logo-big"><img src="{assets_rel}/logo.jpg" alt=""></div><h2>{titulo}</h2>{body}{extra}</div>{bottom}</section>'''
    raise ValueError(layout)


def plain(t):
    return t.replace('<br>', ' ')


def alt_text(s):
    parts = [plain(s['titulo'])]
    if s.get('registro'):
        parts.append(s['registro'])
    if s.get('texto'):
        parts.append(s['texto'])
    if s.get('itens'):
        parts += [f'{k}. {t}' for k, t in enumerate(s['itens'], 1)]
    if s.get('foto'):
        parts.append(f'Fotografia de fundo: {s["foto"]}.')
    if s.get('imagem_a_inserir'):
        parts.append(f'[Imagem a inserir: {s["imagem_a_inserir"]}]')
    return ' '.join(parts)


def slide_md(i, s):
    lines = [f'**{i:02d} — {plain(s["titulo"])}** · _{s["layout"]}_']
    if s.get('kicker'):
        lines.append(f'Chamada: {s["kicker"]}')
    if s.get('numero'):
        lines.append(f'Destaque: {s["numero"]}')
    if s.get('registro'):
        lines.append(s['registro'])
    if s.get('texto'):
        lines.append(s['texto'])
    for k, t in enumerate(s.get('itens', []), 1):
        lines.append(f'{k}. {t}')
    if s.get('tags'):
        lines.append(' · '.join(s['tags']))
    if s.get('botao'):
        lines.append(f'Botão: {s["botao"]}')
    if s.get('nota'):
        lines.append(s['nota'])
    if s.get('foto'):
        lines.append(f'Imagem: foto real/existente `{s["foto"]}`')
    if s.get('imagem_a_inserir'):
        lines.append(f'**Imagem a inserir:** {s["imagem_a_inserir"]}')
    return '\n'.join(lines)


def main():
    if OUT.exists():
        for child in OUT.iterdir():
            if child.is_dir() and child.name[:2].isdigit():
                shutil.rmtree(child)
    assets = OUT / 'assets'
    assets.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / 'identidade/logo.jpg', assets / 'logo.jpg')
    shutil.copytree(ROOT / 'identidade/fontes', assets / 'fonts', dirs_exist_ok=True)  # Fraunces e Inter (OFL)
    fotos = {s['foto'] for c in CARROSSEIS for s in c['slides'] if s.get('foto')}
    for f in fotos:
        shutil.copy2(IMAGES / f, assets / f)

    revisao = ['# Psin Clínica — oito carrosséis (versão 2)', '',
               'Gerado em 05/10/2026 por `scripts/site/gerar_carrosseis.py` a partir de `scripts/site/carrosseis_conteudo.py`. '
               'Substitui os seis carrosséis anteriores (estreia e conversas com as famílias). '
               '**Todo o conteúdo é para validar com a responsável técnica antes da publicação (normas do CFP).** Nenhum post foi publicado.', '',
               'Slides marcados com **Imagem a inserir** ainda não têm foto: a geração de imagem não estava disponível. A descrição indica a imagem desejada.', '']
    resumo = []
    for c in CARROSSEIS:
        folder = OUT / c['slug']
        folder.mkdir()
        total = len(c['slides'])
        slides = '\n'.join(slide_html(s, i, total, '../assets') for i, s in enumerate(c['slides'], 1))
        (folder / 'carrossel.html').write_text(
            f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>{e(plain(c["titulo"]))} — Psin Clínica</title>'
            f'<link rel="stylesheet" href="../assets/fonts/fonts.css"><style>{CSS}</style></head><body>\n{slides}\n</body></html>\n')
        md_slides = '\n\n'.join(slide_md(i, s) for i, s in enumerate(c['slides'], 1))
        alts = '\n\n'.join(f'**Slide {i:02d}:** {alt_text(s)}' for i, s in enumerate(c['slides'], 1))
        alternativas = '\n'.join(f'- {a}' for a in c['capas_alternativas'])
        bloco = (f'Série: {c["serie"]}  \nObjetivo: {c["objetivo"]}  \nFormato: {total} slides, 1080 × 1350\n\n'
                 f'### Capas alternativas\n\n{alternativas}\n\n### Slides\n\n{md_slides}\n\n'
                 f'### Legenda\n\n{c["legenda"]}\n\n### Base editorial e fontes\n\n{c["fontes"]}\n')
        (folder / 'texto.md').write_text(f'# {plain(c["titulo"])}\n\nStatus: para revisão do usuário e validação da responsável técnica.\n\n{bloco}')
        (folder / 'legenda.md').write_text(c['legenda'] + '\n')
        (folder / 'texto-alternativo.md').write_text(f'# Texto alternativo — {plain(c["titulo"])}\n\n{alts}\n')
        revisao += [f'## {c["slug"][:2]} — {plain(c["titulo"])}', '', bloco]
        resumo.append(dict(slug=c['slug'], titulo=plain(c['titulo']), serie=c['serie'], slides=total,
                           imagens_a_inserir=sum(1 for s in c['slides'] if s.get('imagem_a_inserir')),
                           legenda=c['legenda']))
    (OUT / 'textos-para-revisao.md').write_text('\n'.join(revisao))
    (OUT / 'posts.json').write_text(json.dumps(resumo, ensure_ascii=False, indent=2))

    cards = []
    for r in resumo:
        imgs = ''.join(f'<img loading="lazy" src="{r["slug"]}/instagram/slide-{k:02d}.png" alt="Slide {k}">' for k in range(1, r['slides'] + 1))
        aviso = f'<span class="warn">{r["imagens_a_inserir"]} imagem(ns) a inserir</span>' if r['imagens_a_inserir'] else ''
        cards.append(f'<section><h2>{e(r["slug"][:2])} · {e(r["titulo"])}</h2><p class="meta">{e(r["serie"])} · {r["slides"]} slides {aviso}</p>'
                     f'<div class="row">{imgs}</div><details><summary>Legenda</summary><pre>{e(r["legenda"])}</pre></details></section>')
    (OUT / 'index.html').write_text(
        '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>Carrosséis Psin</title><style>'
        ':root{--bg:#F6F2F3;--ink:#3A3638;--card:#fff}'
        '@media (prefers-color-scheme:dark){:root{--bg:#1d1b1c;--ink:#eee;--card:#2a2729}}'
        'body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.5 Inter,Arial,sans-serif;padding:24px 16px}'
        'h1{font:500 32px Georgia,serif;margin:0 0 4px}h2{font:500 24px Georgia,serif;margin:0}'
        'section{background:var(--card);border-radius:16px;padding:20px;margin:20px 0}.meta{margin:4px 0 12px;opacity:.75}'
        '.row{display:flex;gap:10px;overflow-x:auto;padding-bottom:8px}.row img{height:340px;border-radius:8px;flex-shrink:0}'
        '.warn{background:#FBE4EC;color:#A63A65;border-radius:99px;padding:2px 10px;font-size:13px;margin-left:6px}'
        'pre{white-space:pre-wrap;font:15px/1.5 Inter,Arial,sans-serif}'
        '</style></head><body><h1>Psin Clínica — 8 carrosséis</h1><p>Versão 2 · 05/10/2026 · para validar com a responsável técnica antes de publicar.</p>'
        + ''.join(cards) + '</body></html>\n')
    print(f'{len(CARROSSEIS)} carrosséis gerados em {OUT.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
