# Kit de reunião da Psin Clínica

Abra `site/dist/index.html` para visualizar o website ou `index.html` para acessar o kit completo.

## Website revisado em 04/10/2026

- Hero desde o topo da página, menu transparente sobre a fotografia, parede livre à esquerda e marca/objetos à direita. Composição adaptada com image_gen; original Hero.png preservado.
- Apresentação da clínica em texto, com chamada centralizada para a equipe.
- Quatro perfis individuais, cartões alinhados e links de agendamento pelo WhatsApp.
- Galeria simultânea com três fotografias reais aprimoradas, inteiras e sem legendas.
- Descrição do atendimento em quatro momentos, dúvidas frequentes e avaliações fictícias identificadas.
- Blog com três artigos em texto contínuo sobre alimentação e emoções, férias e cuidado, e conversas após filmes.
- Capas editoriais geradas por IA e ícones de Instagram, WhatsApp, Google e Facebook no bloco de contato.

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

Imagem da hero com saturação reduzida por CSS, composição preservada. Botões de interação rosa ficam brancos com borda neutra em repouso; botões cinzas permanecem preenchidos. Informações abaixo da hero têm acentos verticais no computador e no celular. Clínica com botão levemente deslocado à esquerda sob o título e linha vertical mais aparente junto ao texto. Perfis com abordagem destacada e biografias ampliadas a partir das fontes fornecidas e dos perfis profissionais. Chamada de avaliação mais compacta e botão final dos artigos cinza. Não há rodapé separado nem repetição do bloco de contato.

## Salvamento antes dos ajustes finais

A versão aprovada anterior está no commit local `41e9d09` e em `backups/website-antes-ajustes-finais-2026-10-04-132411/website.zip`, com manifesto SHA-256. A cópia contém 30 arquivos verificados e foi concluída antes de qualquer ajuste desta rodada.

Após o snapshot: rosa de interação reforçado, barras discretamente mais visíveis, alinhamento do botão da clínica, retratos sem posição fixa na rolagem, chamada de avaliação centralizada, ícones mais nítidos, mapa e navegação no bloco de contato, e botão flutuante de WhatsApp em todas as páginas.

A criação/envio ao novo repositório privado `pedroipereira/psin-clinica` está pendente de autorização específica exigida pela revisão automática. Nenhum arquivo foi enviado ao GitHub. O remoto do projeto-base MazyOS não foi alterado.

## Organização do encerramento

Faixa da hero com os rótulos “Modalidades de atendimento” e “De quem cuidamos”. Bloco final em três colunas: chamada com a seção Contatos abaixo; endereço completo com CEP junto ao mapa; navegação. Conteúdo centralizado em cada coluna; títulos de seção com tipografia uniforme e textos de apoio no mesmo tamanho. Botão de recepção acima de Contatos. Telefone em uma linha discreta com ícone. Endereço em três linhas: lote/sala, bairro/cidade e CEP. No celular, os blocos ficam empilhados e a navegação usa duas colunas. Ícones vetoriais de marca do Font Awesome 6.7.2, em cinza, inclusive no WhatsApp flutuante. Arquivos e licença em `site/dist/images/social/`. Layout conferido em seis larguras, de 320 a 1440 pixels.

## Página de links para a bio

Abra `site/dist/links.html` ou use o botão “Abrir página de links” no kit. Página independente com identidade da Psin, agendamento pelo WhatsApp, website, profissionais, blog, localização e redes sociais. Conteúdo gerado pelo mesmo script do website; estilos em `site/dist/links.css`. Layout conferido em 320, 390, 768 e 1440 pixels, com navegação para equipe e blog verificada. A página está local e ainda não tem uma URL pública para a bio; não foi criada conta no serviço Linktree.

### Refinamento da página de links

Botões em uma única coluna, compactos e arredondados, com ícones discretos, bordas delicadas e estados suaves de foco/toque. Agendamento como ação principal, com o mesmo tamanho dos demais botões. Chamada “Avalie a Psin no Google” abre a busca da clínica no Maps; link direto de avaliação continua pendente. A ação “Copiar endereço”, em `site/dist/links.js`, confirma a cópia ou seleciona o endereço e orienta a cópia manual quando a área de transferência está indisponível. Layout e navegação conferidos em quatro larguras, com testes dos dois caminhos da cópia.
