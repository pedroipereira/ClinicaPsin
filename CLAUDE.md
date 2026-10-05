# MazyOS — Sistema operacional do negócio

Sua empresa roda em cima desse arquivo. Aqui ficam as regras de operação
do MazyOS — como o Claude lê o contexto, aprende com correções, mantém
tudo atualizado e cria skills novas conforme a operação evolui.

Esse arquivo é editável. O `/instalar` complementou o
final dessa página com as regras específicas da Psin Clínica.

---

## Contexto do negócio

No início de toda conversa, ler os seguintes arquivos (quando existirem
e estiverem preenchidos):

1. `_memoria/empresa.md` — quem é o usuário, o que faz, como funciona o negócio
2. `_memoria/preferencias.md` — tom de voz, estilo de escrita, o que evitar
3. `_memoria/estrategia.md` — foco atual, prioridades, prazos

Usar essas informações como base pra qualquer resposta ou decisão. Ao
sugerir prioridades, formatos ou abordagens, considerar o foco atual
descrito em `estrategia.md`.

Pra qualquer tarefa visual (carrossel, post, landing page), consultar
`identidade/design-guide.md` como referência de estilo.

Não é necessário listar o que foi lido nem confirmar a leitura. Apenas
usar o contexto naturalmente.

---

## Fluxo de trabalho

Antes de executar qualquer tarefa, verificar se existe skill relevante
em `.claude/skills/`. Se encontrar, seguir as instruções da skill. Se
não encontrar, executar a tarefa normalmente.

Ao concluir uma tarefa que não tinha skill mas parece repetível (o
usuário provavelmente vai pedir de novo no futuro), perguntar:

> "Isso pode virar uma skill pra próxima vez. Quer que eu crie?"

Não perguntar pra tarefas pontuais ou perguntas simples. Só quando o
padrão de repetição for claro.

---

## Aprender com correções

Quando o usuário corrigir algo, melhorar uma resposta ou dar uma
instrução que parece permanente (frases como "na verdade é assim", "não
faça mais isso", "prefiro assim", "sempre que...", "evita...", "da
próxima vez..."), perguntar:

> "Quer que eu salve isso pra não precisar repetir?"

Se sim, identificar onde faz mais sentido salvar:

- **Sobre o negócio** (clientes, serviços, mercado) → `_memoria/empresa.md`
- **Sobre preferências e estilo** (tom de voz, formato, o que evitar) → `_memoria/preferencias.md`
- **Sobre prioridades e foco** (projetos, metas, prazos) → `_memoria/estrategia.md`
- **Regra de comportamento nessa pasta** → próprio `CLAUDE.md`

Salvar com uma linha nova clara, sem reformatar o arquivo inteiro.
Confirmar mostrando a linha adicionada.

Não perguntar se a correção for óbvia de contexto imediato (ex: "na
verdade o arquivo se chama X"). Só perguntar quando a informação tiver
valor duradouro.

---

## Manter contexto atualizado

Ao terminar uma tarefa que mudou algo relevante (cliente novo, skill
nova, mudança de foco, processo novo, ferramenta instalada, estrutura
alterada), perguntar:

> "Isso mudou algo no teu contexto. Quer que eu atualize a memória?"

Se sim, identificar o que atualizar:

- **Cliente, serviço, ferramenta, equipe** → `_memoria/empresa.md`
- **Mudança de prioridade ou foco** → `_memoria/estrategia.md`
- **Tom ou estilo** → `_memoria/preferencias.md`
- **Pasta, regra de organização, skill criada** → `CLAUDE.md`
- **Visual (cores, fontes, logo)** → `identidade/design-guide.md`

Mostrar o que vai mudar antes de salvar. Não reformatar o arquivo
inteiro, só adicionar ou editar a linha relevante.

**Quando NÃO perguntar:**
- Tarefas pontuais sem impacto no contexto (escrever um email avulso, criar um post)
- Perguntas simples ou conversas sem ação
- Mudanças já salvas pelo bloco "Aprender com correções"

**Dica:** rode `/atualizar` pra uma varredura completa quando houver dúvida.

---

## Criação de skills

Quando o usuário pedir skill nova:

1. Verificar se existe template relevante em `templates/skills/`. Se
   existir, usar como base e adaptar pro contexto
2. Perguntar se é específica desse projeto ou útil em qualquer:
   - Específica → `.claude/skills/nome-da-skill/SKILL.md` (local)
   - Universal → `~/.claude/skills/nome-da-skill/SKILL.md` (global)
3. Ler `_memoria/empresa.md` e `_memoria/preferencias.md` pra calibrar
   o conteúdo da skill ao contexto do negócio
4. Se a skill precisar de arquivos de apoio (templates, exemplos),
   criar dentro da pasta da skill
5. Seguir o fluxo da skill-creator nativa do Claude Code

---

# Psin Clínica — MazyOS

## O que é esse workspace

Operação digital da Psin Clínica, uma clínica de psicologia em Taguatinga Sul (DF).
O foco atual é revisar e preparar para publicação a presença digital já implementada localmente: website, página de links e conteúdo para Instagram.

**Estrutura de pastas:**
- `_memoria/` — quem é a clínica, como falamos, foco atual
- `identidade/` — marca aplicada em tudo que o sistema gera
- `marketing/` — posts, carrosséis, calendário de conteúdo, campanhas
- `saidas/` — entregas pontuais; `2026-10-03-reuniao/` reúne website, página de links, roteiros e verificações
- `scripts/site/` — geradores do website e dos carrosséis
- `backups/` — snapshots locais com manifesto de integridade
- `dados/` — arquivos a analisar e referências de conteúdo/estrutura
- `../*.docx` — pesquisas de identidade e plano de implementação (3/out/2026)

## Sobre a empresa

A Psin Clínica é uma clínica de psicologia e psicanálise. Atende crianças,
adolescentes e adultos, presencial e online. Público prioritário, equipe
ativa e frase de oferta estão **pendentes** (ver `_memoria/empresa.md`).

## Setores e responsáveis

- **Marketing / conteúdo:** *a definir*. Prioridade atual: montagem de posts
- **Clínico:** responsável técnica Allice Gracyelli de Melo (CRP 01/15635). Valida conteúdo clínico e publicidade
- **Recepção / atendimento:** *a definir*

## O que mais fazemos aqui

- Posts e carrosséis para o Instagram
- Padronização dos canais (bio, Google, Doctoralia, Linktree)
- Textos para o site institucional

## Tom de voz

Claro e direto com o cliente final, com base acolhedora. Detalhes em `_memoria/preferencias.md`.

Evitar: prometer resultado, "método exclusivo da Psin", atribuir técnicas ou
títulos sem aprovação do profissional, expor relato clínico.

## Regras do sistema

- Posts e carrosséis ficam em `marketing/posts/AAAA-MM-DD-tema/`
- Todo conteúdo com tema clínico sai marcado como "para validar com a responsável técnica" (normas do CFP)
- Abordagem terapêutica é apresentada por profissional, nunca como método da clínica
- Enquanto as pendências de `_memoria/` não forem resolvidas, não inventar público, serviço ou equipe. Perguntar.

## Ferramentas conectadas

- [ ] Instagram / Meta
- [ ] Google Perfil da Empresa
- [ ] Canva
- [ ] Google Calendar
- [ ] WhatsApp

*(Marcar conforme for instalando os MCPs)*

## Manutenção das entregas locais

- Website: `saidas/2026-10-03-reuniao/site/dist/`. O gerador do conteúdo é `scripts/site/revisar_apresentacao.py`; estilos e interações também possuem arquivos próprios no `dist`. Verificar o gerador antes de editar somente um HTML gerado, para evitar perda de mudanças na próxima execução.
- Carrosséis: `scripts/site/gerar_carrosseis_estreia.py` e `scripts/site/gerar_carrosseis_educativos.py`; cada entrega contém HTML, PNGs, legendas, textos alternativos, galeria e scripts de renderização.
- Registrar separadamente aprovação dos textos, aprovação das artes, validação clínica e publicação. A existência de arquivos ou links para redes sociais não comprova publicação ou integração com essas plataformas.
