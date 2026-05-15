# Problem Report — Priorizacao de clientes com risco de churn em 30 dias

## Decision

Selecionar semanalmente os clientes ativos que receberao acao de retencao antes de cancelarem.

## Stakeholders

- CRM manager
- Data Science
- Customer Success
- Finance

## Prediction / Analysis Unit

Cliente ativo no fechamento semanal

## Horizon

Probabilidade de churn nos proximos 30 dias apos a data de scoring

## Target Definition

1 se o cliente cancelar ou ficar inativo por criterio contratual dentro de 30 dias; 0 caso contrario

## Data Sources

- Tabela de clientes com cadastro e plano vigente
- Eventos de login agregados ate a data de scoring
- Historico de tickets de suporte disponivel ate a data de scoring
- Historico de pagamentos e faturas ate a data de scoring
- Campanhas de retencao enviadas antes da data de scoring

## Technical Metrics

- recall@20%
- precision@20%
- AUC
- calibration error

## Business Metrics

- receita liquida retida por campanha
- custo por cliente salvo
- margem incremental apos desconto

## Baseline

Regra atual: priorizar clientes sem login por 45 dias ou com mais de 2 tickets criticos nos ultimos 30 dias.

## Error Costs

- **false_positive:** Cliente recebe desconto ou contato sem necessidade, gerando custo e possivel erosao de margem.
- **false_negative:** Cliente com alto risco nao recebe acao e pode cancelar sem intervencao.

## Risks

- Leakage se forem usadas colunas preenchidas apos o cancelamento
- Vies operacional se apenas clientes contatados historicamente tiverem resultado observavel
- Target inconsistente entre cancelamento contratual e inatividade comportamental
- Metrica offline desalinhada com margem preservada
- Campanha de retencao pode causar desconto desnecessario em clientes que ficariam
- Dados sensiveis exigem controle de acesso e minimizacao

## Go/No-Go Criteria

- Target auditavel em fonte independente
- Baseline reproduzido com dados historicos
- Modelo ou regra nova deve melhorar recall@20% sem reduzir precision@20% abaixo do limite operacional
- Custo esperado da intervencao deve ser menor que margem esperada preservada
- Nenhuma feature pode depender de informacao posterior a data de scoring
