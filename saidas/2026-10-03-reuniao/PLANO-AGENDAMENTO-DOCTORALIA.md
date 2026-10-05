# Plano de agendamento — Psin Clínica e Doctoralia

Data da análise: 05/10/2026.

## Estado atual

O website apresenta o atendimento e os profissionais, mas todos os botões de agendamento abrem uma mensagem preenchida no WhatsApp. A FAQ também informa que o visitante deve falar com a recepção para consultar profissionais e horários.

Na operação real descrita em `Sistema de Agendamento — Psin Clínica (Doctoralia).md`, o agendamento acontece integralmente na Doctoralia. O perfil da clínica possui agenda atualizada em tempo real, modalidades presencial e online, seleção de serviço, convênio, profissional e horário.

Portanto, o website e a operação estão desalinhados: o site sugere solicitação manual; a Doctoralia já oferece confirmação online imediata.

## Fluxo real entendido

### Atendimento presencial

1. Escolher psicologia ou psicanálise.
2. Confirmar a unidade de Taguatinga Sul.
3. Escolher o serviço.
4. Informar convênio ou atendimento sem plano.
5. Escolher um profissional ou a primeira data disponível.
6. Escolher data e horário.
7. Continuar no ambiente da Doctoralia para identificação e confirmação.

### Atendimento online

1. Escolher o serviço online.
2. Informar convênio ou atendimento sem plano.
3. Escolher um profissional ou a primeira data disponível.
4. Escolher data e horário.
5. Continuar no ambiente da Doctoralia para identificação e confirmação.

Os horários, profissionais, serviços, convênios e valores podem variar. Eles não devem ser copiados como dados fixos para o website.

## Integração recomendada

Usar o widget oficial da Doctoralia para Centro Médico como fonte única da agenda. A própria Doctoralia informa que oferece quatro formatos: Standard, Lista de Especialistas, Certificado e Botão. O código é gerado na área “Widget para site” e colado no website.

Para a Psin, a melhor composição é:

- Uma página própria `agendamento.html`, coerente com a identidade do site.
- No topo, escolha clara entre atendimento presencial e online, se o widget fornecido permitir preservar essa navegação.
- Widget “Lista de Especialistas” como conteúdo principal, caso todos os profissionais ativos estejam corretamente vinculados e com agenda publicada.
- Widget “Botão” como alternativa mais simples e estável caso a lista não represente corretamente a equipe.
- Link direto para o perfil da clínica como alternativa caso o script do widget seja bloqueado ou não carregue.
- WhatsApp mantido como canal de ajuda para dúvidas, sem competir com a ação principal de agendamento.

O visitante deve concluir o agendamento na infraestrutura da Doctoralia. O site da Psin não precisa receber nome, telefone, dados clínicos, convênio ou informações do paciente.

## Alterações previstas no website

1. Trocar os botões “Agendar pelo WhatsApp” por “Ver horários” ou “Agendar consulta”.
2. Direcionar os botões gerais para `agendamento.html`.
3. Nos perfis individuais, usar o link/widget específico do profissional quando houver um código oficial confiável; caso contrário, abrir a agenda da clínica e deixar a escolha dentro da Doctoralia.
4. Atualizar a FAQ para explicar que horários e disponibilidade são vistos em tempo real na Doctoralia.
5. Atualizar a seção “Como funciona o atendimento”: o primeiro passo passa a ser a escolha de modalidade, serviço, profissional e horário na agenda online.
6. Inserir na página de links um botão principal “Agendar consulta”.
7. Manter “Fale com a recepção” e o botão flutuante de WhatsApp como suporte.

## Conteúdo sugerido para a página

**Título:** Agende seu atendimento

**Introdução:** Consulte os horários disponíveis e escolha a modalidade, o serviço e o profissional pela agenda online da Psin Clínica.

**Avisos curtos:**

- Atendimento presencial em Taguatinga Sul e opções de atendimento online.
- A disponibilidade varia conforme o serviço e o profissional.
- A cobertura do convênio deve ser conferida durante o agendamento.
- Os valores exibidos na Doctoralia podem variar conforme o serviço ou o profissional.

**Canal de apoio:** Ficou com alguma dúvida antes de escolher? Fale com a recepção.

## Dados que não devem ser fixados no site

- Horários vistos no levantamento de 05/10/2026.
- Quantidade de profissionais por serviço.
- Relação completa de convênios.
- Valor único de R$ 179 para todos os atendimentos.
- Duração clínica da sessão com base apenas no intervalo de 40 minutos da grade.

Esses dados podem mudar e devem continuar sob responsabilidade da agenda da Doctoralia.

## Dependência para implementar

É necessário obter, na conta da Psin na Doctoralia, o código oficial do widget escolhido:

1. Acessar o perfil ou área da clínica na Doctoralia.
2. Abrir “Widget para site”.
3. Buscar ou confirmar o perfil da Psin Clínica.
4. Escolher “Lista de Especialistas” ou “Botão”.
5. Gerar e copiar o código completo.

O perfil público confirma que a agenda da clínica está ativa e atualizada em tempo real, mas a página pública não fornece o código de integração específico.

Também existe uma divergência a validar: o site atual apresenta quatro profissionais, enquanto o levantamento do perfil da Doctoralia lista cinco e inclui Kadimiel Kadesh Ferreira de Assunção. Antes de usar o widget “Lista de Especialistas”, a clínica deve confirmar a equipe ativa e quais perfis devem aparecer no site.

## Critérios de validação

- O agendamento abre no celular e no computador.
- A pessoa consegue chegar à seleção de horário sem passar pelo WhatsApp.
- O widget mostra apenas profissionais e serviços ativos.
- O site não armazena dados do paciente.
- Há alternativa visível para abrir a Doctoralia diretamente.
- Há um canal separado para dúvidas com a recepção.
- Navegação por teclado, foco visível e texto acessível nos botões.

## Fontes

- Levantamento interno: `Sistema de Agendamento — Psin Clínica (Doctoralia).md`.
- Perfil público da Psin: https://www.doctoralia.com.br/clinicas/psin-clinica-consultorio-de-psicologia-especializado
- Instruções oficiais do widget para centros médicos: https://pro.doctoralia.com.br/facilities/instalar-widget-no-site
- Apresentação oficial da agenda online: https://pro.doctoralia.com.br/produtos/agenda-online-para-especialistas/ativar-agendamento/form
