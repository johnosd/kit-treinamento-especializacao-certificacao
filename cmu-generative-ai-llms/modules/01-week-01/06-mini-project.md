# 06 — Mini-Project — Technical Readiness Audit

## Objetivo

Criar uma auditoria técnica pessoal para decidir se você está pronto para avançar no programa CMU LLMs ou se precisa de remediação em pré-requisitos.

---

## Entregáveis

Crie em `assets/`:

```txt
02-diagnostic-report.md
03-tokenization-report.md
04-remediation-plan.md
05-readiness-audit.md
```

---

## Estrutura de `05-readiness-audit.md`

```md
# Technical Readiness Audit

## Summary

## Scores

| Área | Score | Status |
|---|---:|---|

## Blocking Gaps

## Non-Blocking Gaps

## Environment Status

## Tokenization/Tensorization Evidence

## Remediation Plan

## Go/No-Go Decision for Week 02
```

---

## Critérios de Go/No-Go

Avance para a Semana 02 se:

- ML básico não está abaixo de 70%;
- NLP básico não está abaixo de 60%;
- você consegue explicar softmax/cross-entropy/perplexity;
- o pipeline `texto -> token IDs -> context/target` está claro;
- ambiente Python roda scripts sem erro.

Pare para remediação se:

- você não consegue explicar gradient descent;
- não entende probabilidade condicional;
- não sabe ler shapes de tensors;
- não consegue rodar scripts Python localmente;
- confunde tokenização com embedding.

---

## Rubrica

| Critério | Fraco | Adequado | Forte |
|---|---|---|---|
| Diagnóstico | respostas vagas | gaps classificados | plano mensurável por área |
| Ambiente | não reproduzível | scripts rodam | versões, logs e limitações documentadas |
| Tokenização | só executa | explica IDs/context/target | identifica limitações e custos |
| Matemática | memoriza fórmulas | aplica softmax/CE/PPL | interpreta tradeoffs e falhas |
| Decisão | "vou seguir" | go/no-go justificado | plano de remediação com evidência |
