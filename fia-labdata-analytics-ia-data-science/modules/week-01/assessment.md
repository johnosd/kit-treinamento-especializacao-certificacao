# Week 01 — Assessment

Responda sem consultar suas notas. Depois revise e registre erros no mistake log.

---

## Parte A — Perguntas Abertas

1. Diferencie Analytics, Data Science, Machine Learning, Deep Learning e GenAI usando um mesmo problema de negócio como exemplo.
2. Explique por que "usar IA para reduzir churn" não é uma formulação técnica suficiente.
3. Defina unidade de predição, target e horizonte temporal para um modelo de churn.
4. Por que baseline é obrigatório antes de um modelo complexo?
5. Dê um exemplo em que acurácia alta não gera valor de negócio.
6. Explique a diferença entre correlação e causalidade em um projeto preditivo.
7. O que é data leakage? Dê dois exemplos.
8. Por que notebooks são úteis na exploração, mas perigosos como único artefato de produção?
9. Que decisões precisam ser tomadas antes da coleta de dados?
10. Quando GenAI é uma escolha desproporcional?

---

## Parte B — Design Questions

### 1. Sistema de Churn

Desenhe uma solução para priorizar clientes com risco de churn.

Inclua:

- entidade;
- janela de observação;
- target;
- baseline;
- métricas técnicas;
- métricas de negócio;
- split;
- riscos de leakage;
- ação de negócio;
- monitoramento inicial.

### 2. RAG Corporativo

Uma empresa quer "um chatbot com todos os documentos internos".

Transforme essa demanda em problem spec:

- usuários;
- tarefas;
- documentos incluídos/excluídos;
- métrica de factualidade;
- métrica de cobertura;
- fallback;
- riscos de segurança;
- custo por pergunta;
- baseline sem LLM.

### 3. Classificação de Tickets

O time de suporte quer classificar tickets automaticamente.

Compare:

- regras manuais;
- modelo supervisionado;
- LLM zero-shot;
- LLM com fine-tuning.

Critérios: custo, latência, dados necessários, explicabilidade, manutenção e qualidade esperada.

---

## Parte C — Debugging Conceitual

Para cada cenário, identifique o erro principal.

1. O time treinou um modelo com dados aleatórios de todos os meses e avaliou em holdout aleatório, mas em produção a previsão é mensal.
2. A equipe escolheu acurácia para fraude com 0,5% de positivos.
3. O dataset de churn inclui `cancellation_reason`.
4. O projeto não tem baseline porque "o modelo será XGBoost".
5. A solução usa LLM para responder perguntas que poderiam ser resolvidas com filtro SQL e template.
6. O time afirma que desconto causa churn porque o coeficiente da regressão é positivo.

---

## Parte D — Tradeoff Analysis

Escreva uma análise curta para cada tradeoff:

1. Modelo simples interpretável versus modelo complexo mais preciso.
2. Métrica offline melhor versus maior custo operacional.
3. RAG versus fine-tuning para conhecimento interno.
4. Acurácia global versus desempenho por subgrupo.
5. Notebook rápido versus pipeline reproduzível.

---

## Parte E — Critério de Aprovação

Você passa na semana se:

- consegue responder 80% das perguntas sem consultar;
- seu problem spec tem decisão, métrica, baseline e riscos;
- você identificou pelo menos 5 failure modes;
- consegue explicar por que acurácia, correlação e causalidade não são equivalentes;
- seu relatório é claro o suficiente para revisão por alguém técnico.
