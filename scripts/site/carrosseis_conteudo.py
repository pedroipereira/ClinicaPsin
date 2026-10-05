"""Conteúdo dos oito carrosséis da Psin Clínica (versão 2, 05/10/2026).

Cada slide tem um layout (capa_foto, capa_cor, texto, numero, citacao, foto,
lista, perfil, cta) e um fundo (branco, azul, rosa, profundo, creme).
Imagens: "foto" aponta para um arquivo real em assets/; "imagem_a_inserir"
descreve a imagem desejada quando ainda não existe foto.
Todo o conteúdo é para validar com a responsável técnica antes da publicação.
"""

HANDLE = '@psinclinicapsicologia'

CARROSSEIS = [
    # ------------------------------------------------------------------ 01
    {
        'slug': '01-conheca-a-psin',
        'titulo': 'Conheça a Psin',
        'serie': 'Apresentação',
        'objetivo': 'Responder quem somos, quem atendemos e onde estamos.',
        'capas_alternativas': ['Prazer, somos a Psin Clínica.', 'Antes da primeira conversa, conheça a Psin.'],
        'slides': [
            dict(layout='capa_foto', foto='psin-clinica.png', foco='center 30%',
                 kicker='Prazer, Psin Clínica',
                 titulo='Sua história tem espaço aqui.',
                 texto='Psicologia e psicanálise em Taguatinga Sul.'),
            dict(layout='texto', fundo='branco', kicker='Quem atendemos',
                 titulo='Cada fase da vida traz suas próprias perguntas.',
                 texto='Atendemos crianças, adolescentes e adultos, com atenção à história e ao momento de cada pessoa.',
                 tags=['Infância', 'Adolescência', 'Vida adulta']),
            dict(layout='citacao', fundo='rosa', kicker='Crianças e famílias',
                 titulo='Na infância, a família também faz parte da conversa.',
                 texto='A participação dos responsáveis é combinada com o profissional ao longo do acompanhamento.'),
            dict(layout='foto', fundo='azul', foto='sala-clinica.png', foco='center 60%',
                 kicker='Nossa equipe',
                 titulo='Diferentes profissionais, cada um com sua abordagem.',
                 texto='Psicologia e psicanálise na mesma equipe. Cada profissional apresenta sua forma de trabalhar.'),
            dict(layout='foto', fundo='branco', foto='recepcao-clinica.png', foco='center 55%',
                 kicker='Onde estamos',
                 titulo='Presencial em Taguatinga Sul. Ou online.',
                 texto='CSE 01 · Lote 06 · Sala 102 · Brasília/DF. O atendimento online depende do profissional e da disponibilidade.'),
            dict(layout='cta', titulo='Vamos conversar?',
                 texto='Para conhecer os profissionais e os horários, fale com a recepção pelo WhatsApp.',
                 botao='Link na bio'),
        ],
        'legenda': '''Prazer, somos a Psin Clínica. 👋

Este perfil começa com um convite: conhecer quem está por aqui e como acontece o nosso trabalho.

Atendemos crianças, adolescentes e adultos em Taguatinga Sul, com opção de atendimento online. Na infância, a conversa também envolve os responsáveis, conforme os combinados com o profissional.

Arraste para conhecer um pouco da Psin. Por aqui, também vamos falar de infância, relações familiares e cuidado emocional, com a linguagem do dia a dia.

📍 CSE 01, Lote 06, Sala 102 — Taguatinga Sul, Brasília/DF
💬 Fale com a recepção pelo WhatsApp no link da bio.

#PsinClinica #Psicologia #Psicanalise #Psicoterapia #TaguatingaSul #Taguatinga #Brasilia #PsicologiaInfantil #PsicologiaDF #Familias #SaudeEmocional #CuidadoEmocional''',
        'fontes': 'Conteúdo institucional. Dados de endereço e modalidades conforme `_memoria/empresa.md`; confirmar com a clínica.',
    },
    # ------------------------------------------------------------------ 02
    {
        'slug': '02-como-comeca-o-atendimento',
        'titulo': 'Como começa o atendimento',
        'serie': 'Apresentação',
        'objetivo': 'Tornar o processo compreensível e reduzir a insegurança do primeiro contato.',
        'capas_alternativas': ['Do primeiro contato aos próximos encontros.', 'O primeiro encontro começa com escuta.'],
        'slides': [
            dict(layout='capa_cor', fundo='profundo', kicker='Primeiro contato',
                 titulo='Como começa o atendimento na Psin?',
                 texto='Quatro passos, do primeiro contato ao acompanhamento.'),
            dict(layout='numero', fundo='branco', numero='01',
                 titulo='Você fala com a recepção.',
                 texto='Pelo WhatsApp ou por telefone, a recepção apresenta os profissionais, as modalidades e os horários disponíveis.'),
            dict(layout='numero', fundo='azul', numero='02',
                 titulo='O horário é confirmado.',
                 texto='O agendamento é concluído depois da confirmação da clínica, com dia, horário e modalidade: presencial ou online.'),
            dict(layout='foto', fundo='rosa', foto='sala-clinica.png', foco='center 65%', numero='03',
                 titulo='Os primeiros encontros são para escutar.',
                 texto='O profissional conhece o que motivou a busca e a história de quem chega. Não é preciso saber explicar tudo de primeira.'),
            dict(layout='numero', fundo='branco', numero='04',
                 titulo='Juntos, vocês fazem os combinados.',
                 texto='Frequência, horários e próximos passos são definidos com o profissional. No atendimento infantil, a participação da família também.'),
            dict(layout='citacao', fundo='azul', kicker='Se bater a dúvida',
                 titulo='“Não sei por onde começar.”',
                 texto='Tudo bem. Você não precisa chegar com as palavras certas. Começar pela dúvida já é um começo.'),
            dict(layout='cta', titulo='Seu primeiro contato pode ser por aqui.',
                 texto='A recepção informa as opções de atendimento pelo WhatsApp.',
                 botao='Link na bio'),
        ],
        'legenda': '''Você já pensou em procurar atendimento, mas não sabe como funciona o começo?

Na Psin, o primeiro contato é com a recepção, que apresenta profissionais, modalidades e horários. Depois, os primeiros encontros com o profissional são o espaço para conhecer sua história e construir os combinados do acompanhamento.

E não precisa chegar sabendo explicar tudo. Começar pela dúvida já é um começo.

Arraste para ver os quatro passos. Para saber as opções disponíveis, fale com a recepção pelo WhatsApp no link da bio.

#PsinClinica #Psicologia #Psicanalise #Psicoterapia #AtendimentoPsicologico #PrimeiraConsulta #TaguatingaSul #Taguatinga #Brasilia #PsicologiaDF #CuidadoEmocional''',
        'fontes': 'Conteúdo institucional sobre o fluxo de agendamento. Confirmar canais (WhatsApp/telefone) e etapas com a recepção.',
    },
    # ------------------------------------------------------------------ 03
    {
        'slug': '03-conheca-a-equipe',
        'titulo': 'Conheça a equipe',
        'serie': 'Apresentação',
        'objetivo': 'Apresentar os profissionais, seus registros e áreas de atuação.',
        'capas_alternativas': ['Conheça os profissionais da Psin.', 'Diferentes trajetórias, espaço para sua história.'],
        'slides': [
            dict(layout='capa_cor', fundo='rosa', kicker='Nossa equipe',
                 titulo='Quem você encontra na Psin.',
                 texto='Psicologia e psicanálise, com trajetórias e abordagens diferentes.',
                 tags=['Allice', 'Sandson', 'Emanuele', 'Suely']),
            dict(layout='perfil', fundo='branco', iniciais='AG',
                 imagem_a_inserir='Retrato autorizado de Allice Gracyelli de Melo, enquadramento do peito para cima, fundo claro da clínica.',
                 titulo='Allice Gracyelli de Melo', registro='Psicóloga · CRP 01/15635 · Responsável técnica',
                 texto='Atua com crianças, famílias e mulheres. Seu trabalho inclui a Análise do Comportamento Aplicada (ABA) e a orientação parental.'),
            dict(layout='perfil', fundo='azul', iniciais='SB',
                 imagem_a_inserir='Retrato autorizado de Sandson Barbosa Azevedo Junior, enquadramento do peito para cima, fundo claro da clínica.',
                 titulo='Sandson Barbosa Azevedo Junior', registro='Psicólogo · CRP 01/27483',
                 texto='Formado em Psicologia pela UDF, trabalha com a Terapia Cognitivo-Comportamental (TCC).'),
            dict(layout='perfil', fundo='branco', iniciais='EM',
                 imagem_a_inserir='Retrato autorizado de Emanuele Martins Carlos de Souza, enquadramento do peito para cima, fundo claro da clínica.',
                 titulo='Emanuele Martins Carlos de Souza', registro='Psicóloga · CRP DF 29508',
                 texto='Atende adolescentes e adultos. Sua prática é orientada pela Gestalt-terapia, com atenção à experiência de cada pessoa.'),
            dict(layout='perfil', fundo='rosa', iniciais='SM',
                 imagem_a_inserir='Retrato autorizado de Suely P. de Melo, enquadramento do peito para cima, fundo claro da clínica.',
                 titulo='Suely P. de Melo', registro='Psicanalista clínica',
                 texto='Com formação em Letras e Psicanálise, tem atuação voltada a mulheres e famílias.'),
            dict(layout='cta', titulo='Conheça cada trajetória.',
                 texto='No site, você encontra a apresentação completa dos profissionais. A recepção informa modalidades e horários.',
                 botao='Link na bio'),
        ],
        'legenda': '''Por trás de cada atendimento, existe uma trajetória profissional.

A equipe da Psin reúne profissionais de psicologia e psicanálise, cada um com sua formação e sua abordagem. Neste carrossel, apresentamos Allice, Sandson, Emanuele e Suely.

Arraste para conhecer a equipe. As apresentações completas estão no site, pelo link da bio, e a recepção informa as modalidades e os horários disponíveis.

#PsinClinica #Psicologia #Psicanalise #Psicoterapia #EquipePsin #Psicologo #TaguatingaSul #Taguatinga #Brasilia #PsicologiaDF #AtendimentoPsicologico''',
        'fontes': 'Dados públicos reunidos em `_memoria/empresa.md`. Confirmar equipe ativa, nomes de divulgação, registros e abordagens com cada profissional antes de publicar. Retratos: só com fotos autorizadas; não gerar pessoas fictícias.',
    },
    # ------------------------------------------------------------------ 04
    {
        'slug': '04-filmes-e-conversas',
        'titulo': 'O filme acabou. A conversa pode continuar.',
        'serie': 'Conversas com as famílias',
        'objetivo': 'Mostrar aos pais como um filme pode abrir conversa sobre sentimentos.',
        'capas_alternativas': ['O que seu filho viu nessa história?', 'Uma história, muitos jeitos de sentir.'],
        'slides': [
            dict(layout='capa_foto', foto='blog-filmes.png', foco='35% center',
                 kicker='Conversas com as famílias',
                 titulo='O filme acabou. A conversa pode continuar.',
                 texto='Como uma história pode abrir espaço para falar do que a criança sente.'),
            dict(layout='citacao', fundo='rosa', kicker='No meio da cena',
                 titulo='“Por que ele ficou tão triste?”',
                 texto='Antes de dar a explicação pronta, devolva a pergunta: “O que você acha que aconteceu com ele?”'),
            dict(layout='texto', fundo='branco', kicker='Por que funciona',
                 titulo='Falar do personagem é mais fácil do que falar de si.',
                 texto='Despedidas, amizades, mudanças. A história coloca os sentimentos em cena, e a criança pode chegar aos dela no próprio tempo.'),
            dict(layout='texto', fundo='azul', kicker='O olhar da criança',
                 titulo='Vocês podem ter visto coisas diferentes.',
                 texto='Você percebeu medo; ela percebeu saudade. Perguntar “qual parte te fez pensar nisso?” mostra como ela leu a história.'),
            dict(layout='lista', fundo='branco', kicker='Para depois dos créditos',
                 titulo='Três perguntas para puxar conversa.',
                 itens=['Qual parte você mais gostou?', 'Como você acha que ele se sentiu?', 'Você já sentiu algo parecido?']),
            dict(layout='texto', fundo='profundo', kicker='Sem pressa',
                 titulo='Nem todo filme precisa virar conversa.',
                 texto='Se a criança só quiser assistir, tudo bem. Às vezes o comentário aparece dias depois, no carro ou na hora do banho. Estar disponível já conta.'),
            dict(layout='cta', titulo='Tem espaço para o olhar de vocês dois.',
                 texto='Na próxima sessão de cinema em casa, escute o que seu filho viu na história.',
                 nota='Salve para lembrar na próxima escolha de filme.'),
        ],
        'legenda': '''O filme termina, e seu filho continua falando de uma cena. Já aconteceu por aí? 🎬

Esse comentário pode ser uma porta de entrada. Às vezes, o que ficou foi uma amizade. Outras vezes, a despedida ou o personagem que precisou pedir ajuda.

Falar do personagem costuma ser mais fácil do que falar de si. E, a partir da história, a criança pode chegar aos próprios sentimentos no tempo dela.

Arraste para ver três perguntas simples para depois dos créditos. Salve para a próxima sessão de cinema em casa.

Por aqui, seguimos conversando sobre as pequenas situações que fazem parte do cuidado. Conheça a Psin pelo link da bio.

#PsinClinica #Psicologia #PsicologiaInfantil #Infancia #EmocoesNaInfancia #Familias #PaisEFilhos #Parentalidade #DesenvolvimentoInfantil #CinemaEmFamilia #Taguatinga #Brasilia''',
        'fontes': 'Adaptação do artigo do blog `saidas/2026-10-03-reuniao/site/dist/blog/filmes-emocoes.html`. American Academy of Pediatrics (AAP), HealthyChildren.org — *Watch Together* e *Why Co-Viewing Is Important* (assistir junto, perguntas abertas, curiosidade pela perspectiva da criança).',
    },
    # ------------------------------------------------------------------ 05
    {
        'slug': '05-quando-a-brincadeira-acaba',
        'titulo': 'Quando a brincadeira precisa acabar',
        'serie': 'Conversas com as famílias',
        'objetivo': 'Orientar os pais a acolher a frustração mantendo o limite.',
        'capas_alternativas': ['Quando a brincadeira precisa acabar.', 'O passeio terminou. A frustração chegou.'],
        'slides': [
            dict(layout='capa_foto',
                 imagem_a_inserir='Mão de uma criança pequena segurando a mão de um adulto, vistas de costas na altura do quadril, saindo de um parquinho no fim da tarde. Sem rostos. Luz dourada, tons de azul claro e rosa suave.',
                 kicker='Conversas com as famílias',
                 titulo='“Só mais um pouquinho!”',
                 texto='Quando a brincadeira precisa acabar e a frustração chega junto.'),
            dict(layout='texto', fundo='branco', kicker='O lado da criança',
                 titulo='Para ela, ainda tinha muita coisa acontecendo.',
                 texto='Mais uma volta no escorregador, um amigo por perto. Encerrar algo bom frustra, e a criança ainda está aprendendo a lidar com esse sentimento.'),
            dict(layout='numero', fundo='azul', numero='01', kicker='Antes de terminar',
                 titulo='Avise que o fim está chegando.',
                 texto='“Mais duas voltas e vamos embora.” Antecipar o fim ajuda a criança a se preparar para a mudança.'),
            dict(layout='numero', fundo='rosa', numero='02', kicker='Na hora',
                 titulo='Coloque o sentimento em palavras.',
                 texto='“Você queria ficar mais. Ficou chateado porque precisamos ir.” Nomear ajuda a criança a reconhecer o que sente.'),
            dict(layout='numero', fundo='branco', numero='03', kicker='O limite',
                 titulo='Acolher não é voltar atrás.',
                 texto='“Hoje precisamos ir. Eu fico aqui com você enquanto a gente se arruma.” Dá para validar o incômodo e manter a decisão.'),
            dict(layout='numero', fundo='azul', numero='04', kicker='Depois do choro',
                 titulo='A explicação pode esperar.',
                 texto='No auge do choro, conversas longas não chegam. Presença calma e poucas palavras ajudam mais. Quando tudo se acalmar, vocês retomam.'),
            dict(layout='citacao', fundo='profundo', kicker='Quem cuida também precisa',
                 titulo='Esse momento também cansa o adulto.',
                 texto='Atraso, cansaço, não saber o que dizer: reconhecer seus limites faz parte do cuidado. Se essas situações têm preocupado a família, conversar com um profissional pode ajudar.'),
            dict(layout='cta', titulo='Esse aprendizado acontece aos poucos.',
                 texto='No dia a dia, com o apoio dos adultos, a criança vai conhecendo seus sentimentos e outras formas de expressá-los.',
                 nota='Salve para retomar com calma.'),
        ],
        'legenda': '''“Só mais um pouquinho!” 🛝

Quem convive com uma criança conhece essa negociação no fim da brincadeira. Você olha o relógio. Ela olha para tudo o que ainda queria fazer.

Nesse encontro entre uma vontade e um limite, aparece a frustração. E acolher o sentimento e manter a decisão não são opostos: fazem parte do mesmo cuidado.

Arraste para ver quatro atitudes que ajudam nessa hora, inclusive a de olhar para o cansaço de quem cuida.

Se situações assim têm preocupado vocês, buscar apoio pode ajudar a compreender o contexto da família. Conheça os profissionais da Psin pelo link da bio.

#PsinClinica #Psicologia #PsicologiaInfantil #Infancia #FrustracaoInfantil #Birra #EmocoesNaInfancia #Limites #PaisEFilhos #Parentalidade #Familias #Taguatinga #Brasilia''',
        'fontes': 'AAP, HealthyChildren.org — *Healthy Mental & Emotional Development in Children* (nomear e manejar emoções, limites com acolhimento) e *Why Kids Act Out* (regulação antes da conversa; necessidades do adulto). Aviso prévio de transição: AAP — *How to Shape & Manage Your Young Child\'s Behavior*. A cena e os diálogos são construções editoriais, não um protocolo universal.',
    },
    # ------------------------------------------------------------------ 06
    {
        'slug': '06-dialogo-com-adolescentes',
        'titulo': '“Como foi o dia?” “Normal.”',
        'serie': 'Conversas com as famílias',
        'objetivo': 'Ajudar os pais a abrir conversa com adolescentes sem transformar o encontro em interrogatório.',
        'capas_alternativas': ['Quando a conversa fica no “normal”.', 'Seu adolescente anda respondendo com poucas palavras?'],
        'slides': [
            dict(layout='capa_cor', fundo='azul', kicker='Conversas com as famílias',
                 titulo='“Como foi o dia?”<br>“Normal.”',
                 texto='Como continuar a conversa quando a resposta vem curta.'),
            dict(layout='texto', fundo='branco', kicker='Um começo possível',
                 titulo='Talvez a pergunta seja ampla demais.',
                 texto='Resumir um dia inteiro é difícil. Puxe por algo concreto, que ele mesmo já contou: “E a apresentação de hoje, como foi?”'),
            dict(layout='foto', fundo='rosa',
                 imagem_a_inserir='Interior de um carro ao entardecer, visto do banco de trás: um adulto dirigindo e um adolescente no banco do passageiro, ambos de costas, sem rostos visíveis. Luzes da cidade desfocadas, tons azulados com um brilho rosado do pôr do sol.',
                 kicker='Lado a lado',
                 titulo='O lugar muda a conversa.',
                 texto='No carro, numa caminhada, cozinhando juntos. Sem o olho no olho, muitos adolescentes falam com mais facilidade.'),
            dict(layout='citacao', fundo='profundo', kicker='Escuta',
                 titulo='Quando ele começar, deixe terminar.',
                 texto='A vontade de aconselhar chega antes do fim da história. Escute primeiro. Depois pergunte: “O que mais te incomodou nisso?”'),
            dict(layout='texto', fundo='azul', kicker='Perspectivas diferentes',
                 titulo='Discordar também faz parte.',
                 texto='Ele pode enxergar a situação de outro jeito. Reconheça o lado dele antes de apresentar o seu. O respeito mantém o diálogo aberto.'),
            dict(layout='texto', fundo='branco', kicker='Sem pressionar',
                 titulo='E se hoje ele não quiser falar?',
                 texto='“Tudo bem, a gente conversa depois.” Estar disponível, sem insistir, mostra que a porta continua aberta.'),
            dict(layout='cta', titulo='A conversa continua no cotidiano.',
                 texto='Uma música, uma série, um jogo de que ele gosta. Interesse genuíno pelo mundo dele também aproxima.',
                 nota='Salve para lembrar: ouvir também é cuidado.'),
        ],
        'legenda': '''Você pergunta como foi o dia. A resposta: “normal”. E o assunto parece acabar ali. 🚗

Dá vontade de emendar várias perguntas para tentar descobrir alguma coisa. Mas vale experimentar outro caminho: um começo mais concreto, um momento lado a lado, uma escuta sem pressa para aconselhar.

Quando a resposta vier, ela pode trazer uma opinião diferente da sua. Escutar com atenção ajuda a conhecer o que ele está vivendo.

Arraste para ver como manter a porta aberta. E guarde espaço, também, para estar junto sem precisar de um assunto importante.

No perfil da Psin, seguimos conversando sobre as relações que fazem parte do cuidado. Conheça a clínica pelo link da bio.

#PsinClinica #Psicologia #Adolescencia #Adolescentes #DialogoEmFamilia #PaisEFilhos #Parentalidade #Escuta #SaudeEmocional #Familias #Taguatinga #Brasilia''',
        'fontes': 'UNICEF Parenting — *3 Ways to Help Get Your Teen to Open Up* (perguntas específicas; conversas lado a lado; tempo junto sem pauta). UNICEF — *11 Tips for Communicating With Your Teen* (escuta, respeito a perspectivas, disponibilidade sem forçar). Diálogos autorais.',
    },
    # ------------------------------------------------------------------ 07
    {
        'slug': '07-telas-e-rotina',
        'titulo': 'Telas em casa, sem virar briga',
        'serie': 'Conversas com as famílias',
        'objetivo': 'Oferecer aos pais combinados práticos sobre telas, sem culpa e sem alarmismo.',
        'capas_alternativas': ['A tela não é a vilã. A rotina é que precisa de espaço.', '“Só mais um vídeo!”'],
        'slides': [
            dict(layout='capa_foto',
                 imagem_a_inserir='Sala de estar à noite: um tablet virado para baixo sobre uma mesa de centro de madeira, ao lado de um livro infantil aberto, lápis de cor e um brinquedo de madeira. Sem pessoas. Luz de abajur, tons de azul claro e rosa suave.',
                 kicker='Conversas com as famílias',
                 titulo='Telas em casa, sem virar briga.',
                 texto='Combinados simples para a rotina da família.'),
            dict(layout='texto', fundo='branco', kicker='Para começar',
                 titulo='Não é só uma questão de tempo.',
                 texto='Importa também o que a criança assiste, com quem e em que momento do dia. A tela pede atenção quando ocupa o lugar do sono, da refeição ou da brincadeira.'),
            dict(layout='texto', fundo='rosa', kicker='Combinados claros',
                 titulo='Combine antes de ligar.',
                 texto='Quanto tempo, o que vai assistir e o que vem depois: “Mais um episódio e depois é banho.” Um aviso alguns minutos antes ajuda na hora de desligar.'),
            dict(layout='numero', fundo='profundo', numero='1–2h', kicker='Sono',
                 titulo='Telas desligadas antes de dormir.',
                 texto='A Sociedade Brasileira de Pediatria recomenda desligar as telas de uma a duas horas antes do sono. O estímulo e a luz podem atrasar o descanso.'),
            dict(layout='foto', fundo='azul',
                 imagem_a_inserir='Mesa de jantar vista de cima em ângulo: pratos simples, copos d\'água e, no canto, uma cestinha com três celulares virados para baixo. Mãos de adultos e de uma criança passando uma travessa, sem rostos. Luz quente, toalha azul clara e guardanapos rosa.',
                 kicker='Zonas livres de tela',
                 titulo='Alguns lugares podem ficar sem tela.',
                 texto='A mesa das refeições e o quarto na hora de dormir são bons começos. Esses momentos viram espaço para conversa.'),
            dict(layout='citacao', fundo='branco', kicker='Exemplo',
                 titulo='As crianças também observam o nosso celular.',
                 texto='Guardar o seu aparelho durante o jantar mostra, na prática, o combinado que você espera dela.'),
            dict(layout='texto', fundo='rosa', kicker='Na hora de desligar',
                 titulo='Reclamar no fim do tempo é esperado.',
                 texto='Desligar algo de que gosta frustra. Você pode acolher o incômodo e manter o combinado, sem precisar de uma grande discussão.'),
            dict(layout='cta', titulo='Cada família encontra seu ritmo.',
                 texto='Se o uso de telas tem gerado conflitos frequentes em casa, conversar com um profissional pode ajudar a entender o contexto.',
                 nota='Salve para montar os combinados da sua casa.'),
        ],
        'legenda': '''“Só mais um vídeo!” Essa frase tem aparecido por aí? 📱

As telas fazem parte da rotina de muitas famílias, e não precisam ser motivo de culpa. A questão é o espaço que elas ocupam: quando tomam o lugar do sono, das refeições ou da brincadeira, vale rever os combinados.

Combinar antes de ligar, avisar antes de desligar e reservar momentos sem tela, para todo mundo da casa, costuma ajudar mais do que proibir de uma vez.

Arraste para ver ideias práticas e salve para conversar com a família.

Se o uso de telas tem gerado conflitos frequentes, a equipe da Psin pode ajudar a entender o contexto. Fale com a recepção pelo link da bio.

#PsinClinica #Psicologia #PsicologiaInfantil #TempoDeTela #Telas #Rotina #RotinaInfantil #Infancia #PaisEFilhos #Parentalidade #Familias #Taguatinga #Brasilia''',
        'fontes': 'Sociedade Brasileira de Pediatria (SBP) — Manual de Orientação *Menos Telas, Mais Saúde* (2019): desconectar 1–2 h antes de dormir, evitar telas nas refeições, supervisão e equilíbrio com outras atividades. AAP — *Family Media Plan* (combinados em família, zonas e horários livres de tela, exemplo dos adultos). Conferir se a recomendação de sono segue atual antes de publicar.',
    },
    # ------------------------------------------------------------------ 08
    {
        'slug': '08-ansiedade-na-escola',
        'titulo': '“Hoje eu não quero ir pra escola.”',
        'serie': 'Conversas com as famílias',
        'objetivo': 'Ajudar os pais a acolher a preocupação com a escola e saber quando buscar apoio.',
        'capas_alternativas': ['Quando a escola vira preocupação.', 'Dor de barriga toda segunda-feira?'],
        'slides': [
            dict(layout='capa_foto',
                 imagem_a_inserir='Porta de casa pela manhã: uma mochila escolar azul clara e um par de tênis infantis no chão; a mão de um adulto pousada sobre a mão pequena da criança que segura a alça da mochila. Recorte sem rostos. Luz suave de janela, paredes claras, tons de azul e rosa.',
                 kicker='Conversas com as famílias',
                 titulo='“Hoje eu não quero ir pra escola.”',
                 texto='O que pode estar por trás dessa frase e como acompanhar seu filho.'),
            dict(layout='texto', fundo='branco', kicker='É comum',
                 titulo='Preocupar-se com a escola faz parte de crescer.',
                 texto='Provas, apresentações, mudança de turma, amizades. Um pouco de nervosismo diante do novo é esperado, em qualquer idade.'),
            dict(layout='citacao', fundo='azul', kicker='O corpo também fala',
                 titulo='Dor de barriga na porta da escola?',
                 texto='Mal-estar, sono agitado na véspera ou choro na despedida podem aparecer em momentos de preocupação. Uma consulta com o pediatra ajuda a descartar outras causas.'),
            dict(layout='numero', fundo='rosa', numero='01', kicker='Escutar',
                 titulo='Pergunte antes de tranquilizar.',
                 texto='“Vai dar tudo certo” nem sempre alivia. Experimente: “O que te preocupa mais na escola?” Saber o que pesa ajuda a pensar junto.'),
            dict(layout='numero', fundo='branco', numero='02', kicker='Manter a rotina',
                 titulo='Ficar em casa alivia hoje, mas pesa amanhã.',
                 texto='Faltar costuma diminuir a angústia na hora, mas tende a tornar a volta mais difícil. Em geral, ajuda manter a ida à escola com apoio.'),
            dict(layout='numero', fundo='azul', numero='03', kicker='Parceria',
                 titulo='A escola pode ser aliada.',
                 texto='Conversar com a professora ou a coordenação ajuda a entender o que acontece em sala e a combinar apoios, como uma chegada mais tranquila.'),
            dict(layout='texto', fundo='profundo', kicker='Quando buscar ajuda',
                 titulo='Quando a preocupação não passa.',
                 texto='Se o medo dura semanas, aumenta ou faz a criança faltar com frequência, vale conversar com um psicólogo. Buscar apoio ajuda a família a entender o que está acontecendo.'),
            dict(layout='cta', titulo='Vocês não precisam passar por isso sozinhos.',
                 texto='A equipe da Psin atende crianças e adolescentes, e a família também faz parte da conversa.',
                 nota='Salve e compartilhe com quem precisa.'),
        ],
        'legenda': '''“Hoje eu não quero ir pra escola.” 🎒

Às vezes vem com dor de barriga, choro na porta ou um silêncio diferente no caminho. Preocupar-se com provas, amizades ou mudanças faz parte de crescer, mas a forma como a família acolhe essa preocupação faz diferença.

Escutar antes de tranquilizar, manter a rotina com apoio e contar com a escola como parceira são caminhos que costumam ajudar.

Arraste para ler e salve para quando precisar.

Se a preocupação dura semanas ou faz seu filho faltar com frequência, conversar com um psicólogo pode ajudar. A equipe da Psin atende crianças e adolescentes, em Taguatinga Sul e online. Link na bio.

#PsinClinica #Psicologia #PsicologiaInfantil #AnsiedadeInfantil #Ansiedade #Escola #VoltaAsAulas #Adolescencia #Infancia #PaisEFilhos #Familias #Taguatinga #Brasilia''',
        'fontes': 'AAP, HealthyChildren.org — *School Avoidance* e *Anxiety and Children* (sintomas físicos; avaliação pediátrica; retorno gradual à escola com apoio; parceria com a escola). Child Mind Institute — *School Refusal: What Parents Can Do* (evitação alivia no curto prazo e reforça o medo; validar e encorajar). Linguagem educativa, sem diagnóstico; o slide 07 orienta busca de ajuda sem lista de sintomas.',
    },
]
