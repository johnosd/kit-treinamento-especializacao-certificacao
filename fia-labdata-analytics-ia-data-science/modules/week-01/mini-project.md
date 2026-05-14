# Mini-Project — Especificação de Problema de IA Aplicada

## Objetivo

Produzir uma especificação técnica de um problema realista que possa evoluir durante o curso para projeto de dados estruturados, GenAI ou capstone.

O projeto desta semana não exige dataset pronto. Exige clareza suficiente para decidir se vale coletar dados e construir baseline.

---

## Entregáveis

Crie os seguintes artefatos dentro de `modules/week-01/assets/`:

1. `problem_spec.json`
2. `problem-report.md`
3. `risk-register.md`
4. `go-no-go.md`

---

## Requisitos do `problem_spec.json`

Use o exemplo em `code/problem_spec.example.json` e substitua por um problema próprio.

O spec deve conter:

- nome do problema;
- decisão a melhorar;
- stakeholders;
- unidade de predição/análise;
- horizonte temporal;
- definição do target ou saída;
- fontes de dados;
- métricas técnicas;
- métricas de negócio;
- baseline;
- custo de erros;
- riscos;
- critérios go/no-go.

---

## Requisitos do `risk-register.md`

Inclua pelo menos 10 riscos:

| Categoria | Mínimo |
|---|---:|
| Dados | 3 |
| Avaliação | 2 |
| Operação | 2 |
| Ética/privacidade | 1 |
| Custo | 1 |
| Produto/adoção | 1 |

Para cada risco:

```txt
Risco:
Causa:
Impacto:
Sinal de detecção:
Mitigação:
Decisão se ocorrer:
```

---

## Requisitos do `go-no-go.md`

Declare critérios objetivos. Exemplos:

- o projeto só avança se houver dados de pelo menos 12 meses;
- o baseline precisa superar regra atual em recall@20% sem dobrar custo operacional;
- o target precisa ser auditável por fonte independente;
- o custo estimado por decisão precisa ser menor que o valor esperado da intervenção;
- o risco de privacidade precisa ter mitigação antes da coleta.

---

## Rubrica

| Critério | Iniciante | Intermediário | Avançado | Research-ready |
|---|---|---|---|---|
| Problema | Vago | Decisão identificada | Decisão, usuário e ação claros | Formulação operacional auditável |
| Dados | Lista genérica | Fontes prováveis | Entidade, timestamp e granularidade | Plano anti-leakage e documentação |
| Métricas | Uma métrica técnica | Técnica + negócio | Métricas alinhadas ao custo de erro | Métrica, experimento e monitoramento |
| Baseline | Ausente | Regra simples | Baseline competitivo | Baseline com critério de superioridade |
| Riscos | Genéricos | Alguns riscos reais | Registro por categoria | Mitigação e decisão go/no-go |
| Comunicação | Prosa solta | Estrutura clara | Documento defendível | Pronto para design review |

---

## Critério de Aceite

O mini-projeto está aceito se outra pessoa consegue ler os arquivos e responder:

1. o que será decidido;
2. com quais dados;
3. como medir sucesso;
4. contra qual baseline;
5. quais riscos podem invalidar o projeto;
6. por que a solução proposta é proporcional ao problema.
