# Week 01 — Exercises

## 1. Classificação de Problemas

Para cada caso, classifique como descriptive analytics, diagnostic analytics, predictive ML, prescriptive analytics, Deep Learning ou GenAI. Justifique em 3-5 linhas.

1. Identificar por que a receita caiu em determinada região.
2. Prever quais clientes devem receber oferta de retenção.
3. Gerar resposta contextual a partir de documentos internos.
4. Classificar imagens de defeitos em linha de produção.
5. Definir qual desconto maximiza margem esperada.
6. Criar dashboard mensal de inadimplência.

Critério: a justificativa deve mencionar decisão, dados, métrica e por que a técnica escolhida é suficiente.

---

## 2. Métrica Técnica vs Métrica de Negócio

Escolha um problema e preencha:

| Item | Resposta |
|---|---|
| Decisão |  |
| Usuário da saída |  |
| Métrica técnica |  |
| Métrica de negócio |  |
| Erro mais caro |  |
| Como medir impacto real |  |

Depois, explique por que otimizar apenas a métrica técnica pode falhar.

---

## 3. Baseline Honesto

Para cada projeto, proponha um baseline simples:

1. Churn de clientes.
2. Previsão de demanda semanal.
3. Triagem de tickets.
4. RAG para políticas internas.
5. Segmentação de clientes.

Critério: o baseline deve ser executável sem modelo complexo.

---

## 4. Detecção de Leakage

Você recebeu um dataset para prever churn em 30 dias. As colunas incluem:

- `customer_id`
- `signup_date`
- `last_login_date`
- `number_of_support_tickets_last_90_days`
- `plan_type`
- `cancellation_reason`
- `days_since_cancellation`
- `discount_received_last_30_days`
- `target_churn_next_30_days`

Responda:

1. Quais colunas são suspeitas de leakage?
2. Quais dependem do timestamp de extração?
3. Que pergunta você faria ao time de dados antes de modelar?
4. Como desenharia um split temporal?

---

## 5. Causalidade

Um modelo mostra que clientes que recebem desconto têm maior churn. A empresa conclui que desconto causa churn.

Explique:

1. por que a conclusão pode estar errada;
2. qual viés operacional pode existir;
3. que experimento ou análise ajudaria a investigar causalidade;
4. como usar o modelo preditivo sem afirmar causalidade.

---

## 6. Custo Computacional e Operacional

Compare duas soluções para triagem de tickets:

- Solução A: regras + busca lexical.
- Solução B: LLM com RAG e agente que chama ferramentas internas.

Preencha:

| Critério | Solução A | Solução B |
|---|---|---|
| Latência |  |  |
| Custo por requisição |  |  |
| Interpretabilidade |  |  |
| Risco de resposta errada |  |  |
| Observabilidade |  |  |
| Quando escolher |  |  |

---

## 7. Red Team do Seu Spec

Pegue o `problem_spec.json` do lab e escreva 10 críticas técnicas. Pelo menos 3 devem envolver dados, 2 avaliação, 2 operação, 1 ética/privacidade e 1 custo.

Exemplo de crítica fraca:

- "Precisa melhorar os dados."

Exemplo aceitável:

- "A fonte `support_interactions` é atualizada após a resolução do ticket; se usada sem timestamp de corte, pode vazar informação posterior à decisão."
