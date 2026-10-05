# MVP do agendamento próprio

## Objetivo

Substituir gradualmente o agendamento da Doctoralia por um fluxo próprio dentro do website da Psin Clínica, mantendo o site anterior como referência visual durante a migração.

## Stack escolhida

- Next.js com App Router e Server Components.
- TypeScript em toda a aplicação.
- React para as etapas interativas.
- Tailwind CSS com tokens da identidade da Psin.
- Supabase: PostgreSQL, autenticação da equipe e Row Level Security.
- Route Handlers ou Server Actions para operações de agendamento.
- Vercel como primeira opção de hospedagem.

## Escopo do MVP

### Paciente

1. Escolher atendimento presencial ou online.
2. Escolher o serviço.
3. Escolher o profissional ou a primeira disponibilidade.
4. Escolher data e horário.
5. Informar nome, telefone, e-mail e, quando aplicável, nome do responsável.
6. Aceitar os termos de privacidade.
7. Receber confirmação e código/link para cancelamento ou remarcação.

O formulário não deve perguntar motivo da consulta, diagnóstico ou relato clínico.

### Recepção

1. Entrar em uma área protegida.
2. Cadastrar profissionais e serviços.
3. Definir disponibilidade recorrente e bloqueios.
4. Visualizar a agenda por dia e profissional.
5. Confirmar, cancelar ou remarcar um atendimento.
6. Consultar os dados mínimos de contato necessários para a operação.

### Regras essenciais

- Impedir dois agendamentos para o mesmo profissional no mesmo horário no próprio banco de dados.
- Reservar o horário de forma atômica, sem depender apenas da interface.
- Armazenar datas em UTC e exibir no fuso `America/Sao_Paulo`.
- Registrar criação, alteração e cancelamento.
- Não expor a chave de serviço do banco no navegador.
- Aplicar RLS em todas as tabelas expostas.

## Fora do primeiro MVP

- Prontuário psicológico e anotações clínicas. Tema mantido como pendência para uma etapa futura, com análise própria de segurança, acesso e tratamento de dados sensíveis.
- Registro do motivo da consulta ou documentos clínicos.
- Pagamento online ou presencial. A direção escolhida é permitir futuramente pagamento opcional: antecipado ou na clínica, mas a implementação permanece pendente.
- Faturamento de convênio.
- Integração bidirecional com a Doctoralia.
- Aplicativo móvel.
- Automação completa de WhatsApp.

## Entidades previstas

- `professionals`
- `services`
- `professional_services`
- `appointment_slots`
- `appointments`
- `appointment_events`
- `staff_profiles`

## Fases

1. Fluxo visual tipado com dados de demonstração.
2. Banco, migrações e prevenção de conflito de horário.
3. Identificação mínima e confirmação do paciente.
4. Login e agenda da recepção.
5. Notificações, cancelamento e remarcação.
6. Migração das páginas institucionais para o novo projeto.

## Decisões para a evolução da agenda

- Cada serviço terá duração padrão e poderá prever intervalo entre sessões.
- Acompanhamentos poderão ser semanais, a cada 14, 21 ou 28 dias, ou usar uma periodicidade personalizada.
- Um profissional poderá ter vários intervalos de trabalho no mesmo dia.
- A disponibilidade será calculada pela combinação da agenda semanal, sessões recorrentes, consultas avulsas, férias, feriados e bloqueios.
- Férias e ausências serão informadas pelo profissional, com identificação prévia das sessões afetadas.
- Feriados serão importados pelo sistema e seguirão uma política configurável, permitindo tratar de forma diferente atendimentos presenciais e online.
- A automação consultará o estado atual da sessão antes de enviar confirmação, cancelamento ou proposta de remarcação.
- Haverá um painel próprio para cada profissional e uma visão geral para a administração.

## Pendências deliberadas

### Prontuário

O sistema atual armazenará somente informações administrativas de agenda, contato, presença e, futuramente, pagamento. Conteúdo clínico ficará fora do agendamento até que seja projetado como módulo próprio.

### Pagamento

A política desejada é opcional: o paciente poderá escolher pagar antecipadamente ou na clínica. A integração, os meios aceitos, os prazos de reserva e as regras de cancelamento serão definidos antes da implementação.

## Estado atual

As fases 1 a 3 já possuem uma primeira implementação:

- `/agendamento` consulta a API e usa horários demonstrativos quando o banco ainda não está configurado;
- a migração em `supabase/migrations/202610050001_initial_scheduling.sql` cria o catálogo, os horários, os agendamentos e o histórico;
- `book_appointment` bloqueia o horário dentro de uma transação e o índice parcial impede duplicidade;
- `/api/availability` retorna a disponibilidade e `/api/appointments` valida e registra a reserva;
- a identificação coleta apenas nome, responsável quando aplicável, WhatsApp, e-mail e consentimento.

Para ativar o modo real, crie o projeto no Supabase, execute a migração, copie `.env.example` para `.env.local` e preencha as três variáveis. A chave `SUPABASE_SERVICE_ROLE_KEY` deve existir apenas no servidor.

A fase 4 também possui uma primeira implementação em `/recepcao`:

- login com Supabase Auth;
- segunda verificação de autorização na tabela `staff_profiles`;
- agenda diária com dados do paciente e do atendimento;
- criação de novas disponibilidades;
- confirmação e cancelamento com registro no histórico;
- APIs administrativas protegidas por token e perfil ativo da equipe.

Após executar a segunda migração, crie a primeira conta em `Authentication > Users` e vincule o UUID na tabela `staff_profiles`, conforme o exemplo comentado na migração. O próximo incremento é permitir editar/remover horários, remarcar atendimentos e enviar as confirmações automaticamente.

## Painel profissional e agenda recorrente

A migração `202610050003_professional_scheduling.sql` e a rota `/profissional` implementam a base da etapa seguinte:

- vários turnos de trabalho no mesmo dia;
- modalidade por turno;
- duração do serviço e intervalo entre sessões;
- geração automática dos horários públicos a partir da agenda semanal;
- férias, feriados e bloqueios com contagem dos atendimentos afetados;
- acompanhamentos recorrentes semanais, a cada 14, 21 ou 28 dias;
- recorrências personalizadas pela API;
- painel utilizável pelo profissional e visão administrativa;
- prevenção de sobreposição de qualquer atendimento do mesmo profissional no banco.

O envio automático de mensagens de cancelamento e remarcação permanece como próximo incremento. As exceções e suas ações já são registradas para alimentar essa automação.

## Lapidação da experiência

- As etapas do agendamento podem ser usadas para voltar a uma escolha anterior.
- A seleção de horário mostra um dia por vez e permite navegar entre os dias disponíveis.
- O formulário confirma o número de WhatsApp antes de reservar.
- As mensagens de validação identificam o campo ou problema específico.
- `Teleconsulta` e `Psicoterapia online` foram consolidadas: o serviço é escolhido separadamente da modalidade presencial ou online.
- O pagamento opcional permanece sinalizado como pendência e nenhuma cobrança é feita no fluxo atual.
- O painel profissional possui Visão geral, Calendário, Clientes, Disponibilidade e Acompanhamentos.
- Os formulários do painel não usam autopreenchimento e são limpos depois de uma operação concluída.

A consolidação dos serviços online depende da migração `202610050005_unify_online_services.sql`.
