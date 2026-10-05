# Psin Clínica — 8 carrosséis (versão 2)

Produzidos em 05/10/2026 com a skill `/carrossel`. Substituem os seis carrosséis anteriores (estreia + conversas com as famílias), que continuam no histórico do git (commit `37565ae`).

**Status:** textos e artes para revisão do usuário. Todo o conteúdo é **para validar com a responsável técnica** antes da publicação (normas do CFP). Nenhum post foi publicado.

| # | Carrossel | Slides | Imagens a inserir |
|---|-----------|--------|-------------------|
| 01 | Conheça a Psin | 6 | — |
| 02 | Como começa o atendimento | 7 | — |
| 03 | Conheça a equipe | 6 | 4 retratos autorizados |
| 04 | O filme acabou. A conversa pode continuar. | 7 | — |
| 05 | Quando a brincadeira precisa acabar | 8 | capa |
| 06 | “Como foi o dia?” “Normal.” | 7 | 1 (slide 03) |
| 07 | Telas em casa, sem virar briga | 8 | capa + slide 05 |
| 08 | “Hoje eu não quero ir pra escola.” | 8 | capa |

Slides com **Imagem a inserir** mostram uma área tracejada com a descrição da foto desejada. A geração por IA não estava disponível (plano gratuito do Higgsfield). Para incluir a foto: salve-a em `assets/`, troque `imagem_a_inserir=...` por `foto='arquivo.png'` em `scripts/site/carrosseis_conteudo.py` e gere de novo.

## Arquivos

- `index.html`: galeria com todos os slides e legendas. `visao-geral.png`: prancha geral.
- Cada pasta tem `instagram/slide-NN.png` (1080 × 1350), `legenda.md`, `texto.md` (texto, capas alternativas e fontes), `texto-alternativo.md`, `carrossel.html` e `verificacao.json`.
- `textos-para-revisao.md`: todos os textos e fontes em um só documento.
- `carrosseis-psin.zip`: PNGs, legendas e textos alternativos.

## Regenerar

Na raiz do projeto:

```sh
python3 scripts/site/gerar_carrosseis.py
NODE_PATH=$(npm root -g) node marketing/posts/2026-10-05-carrosseis/render-all.js
```

Conteúdo: `scripts/site/carrosseis_conteudo.py`. Visual: CSS em `scripts/site/gerar_carrosseis.py`. Fontes Fraunces (títulos) e Inter (texto), licença OFL, em `identidade/fontes/`.

## Sistema visual

Branco, azul claro `#E5EFF8`, rosa claro `#FBE4EC`, azul profundo `#24435C` e rosa da marca `#E0628F` no encerramento. Layouts variados: capa com foto, capa de cor, número grande, citação, foto dividida, lista e perfil. Não há dois fundos iguais em sequência. Títulos de 88 px e texto de 40 px, para leitura no celular.
