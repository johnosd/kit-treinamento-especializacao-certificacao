# Coverage Report — Semana 01

> **Data da revisão:** 2026-05-15
> **Estado final:** ✓ aprovado

---

## Sumário executivo

A Semana 01 cobre os três tópicos oficiais do 11-667 W01 (transformer architecture, pre-training objectives, building blocks) com profundidade equivalente ou superior ao syllabus. O material teórico deriva a mecânica de atenção com profundidade de paper graduate-level (incluindo análise de variância do dot product, Pre-LN vs Post-LN, comparação de objetivos CLM vs MLM). O lab valida implementação NumPy contra PyTorch — padrão de research engineering, não tutorial. O assessment tem 5 questões com rubrica completa e model answers; o total de pesos = 100. As leituras cobrem os papers primários obrigatórios e incluem publicação de professor CMU (Neubig 2017), em conformidade com a Professor Extraction Rule. Não há `✗ ausente` nem `⚠ raso` sem gap action.

---

## Auditoria por tópico

### Tópico: Transformer architecture

- **Previsto no original:** sim (11-667 W01 explicita)
- **Coberto no kit:** ✓
- **Profundidade comparada:** equivalente/acima
- **Evidência:**
  - `01-theory.md` §Fundamentos formais — derivação completa de scaled dot-product attention, MHA, FFN, PE, LN
  - `01-theory.md` §Arquitetura e componentes — diagrama Mermaid encoder vs decoder, tabela GPT-2 Small
  - `01-theory.md` §Scaling e custo — fórmula de FLOPs, regra de bolso Kaplan 2020
  - `03-lab-guided.md` — implementação NumPy + validação PyTorch (5 passos)
  - `07-assessment.md` Q1 (scaling), Q2 (design), Q3 (MHA vs single-head), Q5 (paper critique)
- **Gap action:** nenhuma

---

### Tópico: Pre-training objectives (CLM, MLM)

- **Previsto no original:** sim (11-667 W01 menciona "pre-training objectives")
- **Coberto no kit:** ✓
- **Profundidade comparada:** equivalente
- **Evidência:**
  - `01-theory.md` §Objetivos de pré-treinamento — fórmulas CLM e MLM com detalhes sobre masking strategy do BERT (80/10/10)
  - `02-readings.md` — Brown et al. 2020 (CLM em escala) e Devlin et al. 2019 (MLM) como leituras obrigatórias
  - `07-assessment.md` Q2 — design question que distingue quando usar encoder vs decoder
  - `08-flashcards.md` F2 (CLM loss) e F3 (MLM com percentuais)
- **Gap action:** nenhuma

---

### Tópico: Building blocks (attention, positional encoding, FFN, residual, layer norm)

- **Previsto no original:** sim (11-667 W01 usa o termo "building blocks")
- **Coberto no kit:** ✓
- **Profundidade comparada:** acima (inclui Pre-LN vs Post-LN com justificativa de estabilidade de gradiente, análise de d_ff=4×d_model)
- **Evidência:**
  - `01-theory.md` §Fundamentos formais — todos os 5 componentes cobertos com fórmulas
  - `05-exercises.md` E3 — comparação explícita Post-LN vs Pre-LN
  - `08-flashcards.md` A1 (fluxo decoder), A3 (d_ff), C2 (Pre-LN vs Post-LN)
- **Gap action:** nenhuma

---

## Auditoria de leituras

- **Leituras obrigatórias no original:** não especificado publicamente para W01 (lista de papers geral não separada por semana)
- **Leituras obrigatórias no kit:** 4 (Vaswani 2017, Devlin 2019, Brown 2020, Neubig 2017)
- **Leitura do professor real presente:** ✓ — Neubig 2017 (Graham Neubig, CMU LTI, co-faculty do certificado)
- **Leitura do material oficial presente:** ✓ — 2025.cmu-llms.org/schedule/ listado em leituras complementares
- **Referências suspeitas:** nenhuma — todas as 4 obrigatórias são arXiv verificáveis com IDs confirmados (1706.03762, 1810.04805, 2005.14165, 1703.01619); Harvard NLP Annotated Transformer é URL confirmada

---

## Auditoria de assessment

- **Questões com rubrica + model answer:** 5 de 5 ✓
- **Mix de tipos:**
  - open-ended / derivação: ✓ (Q1)
  - design: ✓ (Q2)
  - tradeoff analysis: ✓ (Q3)
  - debugging: ✓ (Q4)
  - paper critique: ✓ (Q5)
- **Total de pesos:** 20 + 20 + 20 + 15 + 25 = **100** ✓
- **Múltipla escolha trivial:** nenhuma ✓
- **Observações:** mix de tipos conforme requisito da Banca (≥1 de cada categoria obrigatória). Todas as model answers têm 200–500 palavras com derivação, pitfalls e referências.

---

## Auditoria de suplementação

**Não aplicável** — Semana 01 é `core` (1:1 com 11-667 W01). Sem suplementação de curso-irmão. A leitura Neubig 2017 é do professor real identificado (Professor Extraction Rule §4.2), não é suplementação por gap.

---

## Auditoria de filosofia

**Consistente.** O programa é engineering-heavy (filosofia extraída: 60% lab/engenharia, 40% teoria+readings). Esta semana:
- Lab é o coração: 5 passos com verificações quantitativas (max_diff < 1e-5), profiling de tempo, comparação contra framework.
- Teoria tem implementação de referência em 50 linhas de código real (não pseudocódigo).
- Assessment privilegia derivação + design + debugging — não reconhecimento passivo.
- Nenhuma seção de "motivação genérica" — começa direto com o problema técnico.

A voz de Neubig (professor real) aparece nas escolhas de referência (tutorial seq2seq como contexto histórico do Transformer).

---

## Gap actions

Nenhuma. Semana aprovada sem gaps catastróficos ou rasos.

---

## Decisão final

**✓ aprovado** — Semana 01 fechada. Todos os tópicos cobertos com profundidade ≥ ao original. Assessment completo com mix de tipos e total de pesos = 100. Leituras incluem publicação do professor real. Lab valida implementação NumPy contra PyTorch com critério quantitativo.

Atualizar `coverage-matrix.md` linha W01: `⏳ pendente` → `✓ coberto`.
