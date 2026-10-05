# Primeiros carrosséis — Psin Clínica

Produzidos em 05/10/2026 a partir dos textos aprovados pelo usuário nesta data.

Abra `index.html` para revisar as 18 artes e ler as legendas. `visao-geral.png` reúne todos os slides em uma prancha. Para o Instagram, use os arquivos de cada pasta `instagram/`, em ordem de `slide-01.png` a `slide-06.png`, e a respectiva `legenda.md`.

## Entrega

- 01-conheca-a-psin: apresentação, públicos e localização.
- 02-como-comeca-o-atendimento: recepção, encontros e acompanhamento.
- 03-conheca-a-equipe: apresentações tipográficas dos quatro profissionais.
- 18 PNGs de 1080 × 1350 pixels (4:5), três legendas e textos alternativos.
- HTMLs editáveis com CSS incorporado, dados em JSON e scripts de renderização.

## Direção visual

Branco, azul e rosa claros; títulos editoriais e textos de apoio legíveis. Logotipo preservado, limitado a 100 px. Fotos da recepção e sala já fornecidas e aprimoradas no projeto, reutilizadas sem novas edições de imagem. Os recortes são feitos apenas na composição HTML. Não foram gerados retratos nem representados pacientes. As iniciais na equipe são elementos tipográficos.

## Manutenção

O gerador do projeto é `scripts/site/gerar_carrosseis_estreia.py`. Ele lê o documento aprovado em `marketing/posts/2026-10-04-estreia-do-perfil/textos-para-revisao.md` e monta os HTMLs e legendas. Para exportar, execute `render-all.js` com Node e Playwright disponíveis. Cada pasta também tem seu próprio `render.js`. A variável `CHROME_PATH` permite informar o executável do navegador.

No ambiente atual, a partir da raiz do projeto:

```sh
python3 scripts/site/gerar_carrosseis_estreia.py
NODE_PATH=/private/tmp/psin-preview-tools/node_modules node marketing/posts/2026-10-05-carrosseis-estreia/render-all.js
```

## Verificação

Todas as artes foram inspecionadas visualmente. Formato dos 18 PNGs conferido; textos aprovados comparados com o conteúdo renderizado; galeria verificada em 1440, 390 e 320 pixels. Relatórios por carrossel em `verificacao.json` e relatório da galeria em `verificacao-galeria.json`.

## Estado de entrega

Textos e artes dos três carrosséis aprovados pelo usuário em 05/10/2026. Conteúdo institucional e informações dos profissionais para validar com a responsável técnica antes da publicação, conforme o briefing. O website e a página de links continuam locais: confirmar o destino público da bio antes de publicar as chamadas. Nenhum post foi publicado.
