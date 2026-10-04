# Kit de reunião da Psin Clínica

Abra `site/dist/index.html` para visualizar o website ou `index.html` para acessar o kit completo.

## Website revisado em 04/10/2026

- Hero desde o topo da página, menu transparente sobre a fotografia, parede livre à esquerda e marca/objetos à direita. Composição adaptada com image_gen; original Hero.png preservado.
- Apresentação da clínica em texto, com chamada centralizada para a equipe.
- Quatro perfis individuais, cartões alinhados e links de agendamento pelo WhatsApp.
- Galeria simultânea com três fotografias reais aprimoradas, inteiras e sem legendas.
- Descrição do atendimento em quatro momentos, dúvidas frequentes e avaliações fictícias identificadas.
- Blog com três artigos em texto contínuo sobre alimentação e emoções, férias e cuidado, e conversas após filmes.
- Capas editoriais geradas por IA e botões de Instagram, WhatsApp e Linktree no rodapé.

As páginas abrem diretamente no navegador. Não exigem instalação. O WhatsApp abre uma mensagem preenchida; o visitante decide enviá-la. Não há sistema próprio de reservas.

## Arquivos

- `site/dist/`: website navegável, estilos, interações e imagens.
- `site/dist/images/blog-geracao.json`: prompts das novas imagens do blog.
- `roteiro-reuniao.excalidraw` e `roteiro-visual.svg`: mapa da reunião.
- `roteiro-apresentacao.md`: roteiro escrito.
- `REVISAO-EDITORIAL.md`: informações a confirmar com a clínica antes de publicar.
- `verificacao/`: capturas e relatório técnico da revisão atual.

O site continua local. As avaliações são exemplos fictícios claramente sinalizados. Equipe, registros, contatos e conteúdo clínico aguardam aprovação da clínica. Os retratos da equipe usam iniciais até o recebimento de fotografias autorizadas.

## Manutenção

O conteúdo HTML é gerado por `scripts/site/revisar_apresentacao.py`, executado da raiz do projeto. Estilos e interações ficam em `site/dist/styles.css` e `site/dist/app.js`. O script não altera as fotografias.

## Refinamento visual e interações

Botões cinzas preenchidos e botões rosas com fundo branco e preenchimento rosa na interação, faixa de informações com maior destaque, clínica em duas colunas e profissionais com resumos contínuos. Perfis individuais dão mais espaço ao retrato, ainda representado por iniciais até o recebimento de fotos reais. Atendimento com fundo branco, títulos curtos e elevação dos cartões. FAQ sem caixas, com seta lateral de giro suave, abertura por cursor, toque ou teclado e respostas antecedidas por um ponto rosa. Botão do blog abaixo dos artigos, chamada final sem caixa e encerramento em um único bloco de contato, com ícones de Instagram, WhatsApp, Google e Facebook.

A chamada de avaliações abre uma busca específica da clínica no Google Maps. O link direto para avaliar ainda precisa ser informado pela clínica.

## Últimos ajustes de apresentação

Imagem da hero com saturação reduzida por CSS, composição preservada. Botões de interação rosa ficam brancos com borda neutra em repouso; botões cinzas permanecem preenchidos. Informações abaixo da hero têm acentos verticais no computador e no celular. Clínica com botão centralizado sob o título e linha discreta à esquerda do texto. Perfis com abordagem destacada e biografias ampliadas a partir das fontes fornecidas e dos perfis profissionais. Chamada de avaliação mais compacta e botão final dos artigos cinza. Não há rodapé separado nem repetição do bloco de contato.
