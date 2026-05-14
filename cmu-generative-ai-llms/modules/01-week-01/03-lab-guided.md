# 03 — Lab Guided — Setup, Diagnóstico e Tokenização Mínima

## Objetivo

Este lab valida seu ambiente e executa um pipeline mínimo:

```txt
texto -> tokens -> token IDs -> tensor-like batches -> next-token targets -> cross-entropy/perplexity demo
```

O lab funciona sem dependências externas. Se PyTorch e Hugging Face estiverem instalados, os scripts também registram essa disponibilidade.

---

## Estrutura

```txt
01-week-01/
├── code/
│   ├── 01_environment_check.py
│   ├── 02_prereq_diagnostic.py
│   ├── 03_tokenize_tensorize.py
│   ├── diagnostic_questions.json
│   ├── sample_corpus.txt
│   └── requirements.txt
└── assets/
    └── 01-diagnostic-template.md
```

---

## Passo 1 — Verificar Ambiente

No diretório `cmu-generative-ai-llms/modules/01-week-01/code`, execute:

```powershell
python 01_environment_check.py
```

Resultado esperado:

```txt
Python: ...
Platform: ...
Optional packages:
  torch: installed/missing
  transformers: installed/missing
  tokenizers: installed/missing
CUDA available: yes/no/unknown
```

Por quê:

- PyTorch/HF são centrais no curso;
- GPU não é obrigatória na Semana 01, mas precisa ser detectada cedo;
- versões e disponibilidade devem ser registradas antes de debugging.

---

## Passo 2 — Rodar Diagnóstico de Pré-Requisitos

```powershell
python 02_prereq_diagnostic.py diagnostic_questions.json --out ..\assets\02-diagnostic-report.md
```

O script gera um relatório com áreas fortes/fracas:

- ML;
- NLP;
- PyTorch;
- probabilidade/otimização;
- sistemas.

Por quê:

- o certificado CMU assume base forte;
- gaps em pré-requisitos não devem ser descobertos durante Transformers;
- o plano de remediação precisa ser explícito.

---

## Passo 3 — Rodar Pipeline de Tokenização

```powershell
python 03_tokenize_tensorize.py sample_corpus.txt --out ..\assets\03-tokenization-report.md
```

O script faz:

1. normalização simples;
2. tokenização whitespace/pontuação;
3. construção de vocabulário;
4. mapeamento token -> ID;
5. criação de janelas de contexto;
6. geração de targets next-token;
7. demonstração de softmax, cross-entropy e perplexity com logits artificiais.

Por quê:

- você precisa entender o pipeline antes de usar tokenizers prontos;
- language modeling é essencialmente previsão de próximo token;
- perplexity não deve ser uma palavra decorativa.

---

## Passo 4 — Revisar Relatórios

Abra:

```txt
assets/02-diagnostic-report.md
assets/03-tokenization-report.md
```

Perguntas obrigatórias:

1. Quais gaps impedem progresso em LLMs?
2. O vocabulário gerado tem tokens especiais?
3. Como os exemplos foram transformados em `(context, target)`?
4. A perplexity calculada mede o quê?
5. Que partes mudariam com Hugging Face Tokenizers?

---

## Passo 5 — Plano de Remediação

Preencha:

```txt
assets/04-remediation-plan.md
```

Inclua:

- tópico fraco;
- evidência do gap;
- recurso oficial/paper;
- tarefa prática;
- prazo;
- critério de conclusão.

---

## Troubleshooting

| Sintoma | Causa provável | Correção |
|---|---|---|
| `python` não encontrado | Python fora do PATH | tente `py` no Windows ou ajuste instalação |
| relatório não criado | caminho de saída inválido | confirme `..\assets\...` |
| `torch: missing` | PyTorch não instalado | não bloqueia a semana; instale depois se necessário |
| `CUDA available: no` | sem GPU local ou PyTorch CPU-only | use CPU nesta semana e cloud GPU no futuro |
| tokenização parece simples demais | esperado | esta semana mostra mecânica mínima antes de BPE/WordPiece |

---

## Critério de Conclusão

O lab está completo quando:

- ambiente foi registrado;
- diagnóstico gerou relatório;
- tokenização gerou vocabulário, IDs, janelas e targets;
- você explicou cross-entropy e perplexity com os valores do relatório;
- plano de remediação foi escrito.
