# 02 — Week 01 Readings

## Leituras Obrigatórias

### 1. CMU LLMs 2025 — Syllabus

- **Fonte:** <https://2025.cmu-llms.org/syllabus/>
- **Tipo:** syllabus público.
- **Foco:** pré-requisitos, escopo, avaliações, assignments e expectativas.
- **Tarefa:** extraia os pré-requisitos e marque cada um como `forte`, `médio` ou `fraco`.

### 2. PyTorch — Learn the Basics

- **Fonte:** <https://docs.pytorch.org/tutorials/beginner/basics/intro.html>
- **Tipo:** documentação oficial.
- **Foco:** tensors, datasets, transforms, autograd, optimization e save/load.
- **Tarefa:** leia com atenção especial a `Tensors` e `Automatic Differentiation`.

### 3. Hugging Face Transformers — Quicktour

- **Fonte:** <https://huggingface.co/docs/transformers/quicktour>
- **Tipo:** documentação oficial.
- **Foco:** pipeline, AutoTokenizer, AutoModel, inference e uso básico.
- **Tarefa:** identifique a diferença entre tokenizer, model e pipeline.

### 4. Hugging Face Tokenizers — Quicktour

- **Fonte:** <https://huggingface.co/docs/tokenizers/quicktour>
- **Tipo:** documentação oficial.
- **Foco:** tokenização, vocabulário, encode/decode e treinamento de tokenizer.
- **Tarefa:** registre 5 decisões que um tokenizer impõe sobre custo e representação.

---

## Leituras Técnicas Complementares

### 1. Jurafsky & Martin — Speech and Language Processing

- **Fonte:** <https://web.stanford.edu/~jurafsky/slp3/>
- **Tipo:** livro técnico aberto.
- **Foco:** language modeling, probabilidade de sequências, perplexity.
- **Tarefa:** escreva a fórmula de perplexity e uma limitação da métrica.

### 2. The Illustrated Transformer

- **Fonte:** <https://jalammar.github.io/illustrated-transformer/>
- **Tipo:** artigo técnico visual, citado no schedule público CMU.
- **Foco:** visão estrutural de Transformer.
- **Tarefa:** use apenas como apoio visual; a leitura formal começa na Semana 05 com o paper original.

### 3. Attention Is All You Need

- **Fonte:** <https://arxiv.org/abs/1706.03762>
- **Tipo:** paper seminal.
- **Foco nesta semana:** leia abstract, introdução e visão geral; não tente dominar todos os detalhes ainda.
- **Tarefa:** anote quais pré-requisitos matemáticos ainda precisam ser revisados.

---

## Perguntas de Leitura

1. Quais pré-requisitos do syllabus CMU são mais frágeis para você?
2. O que PyTorch chama de tensor e por que isso é mais que um array?
3. Qual é a diferença entre tokenizar texto e gerar embeddings?
4. Por que perplexity depende do tokenizador?
5. O que significa prever o próximo token?
6. Quais partes do ambiente local impediriam treino ou inferência realista?
7. Que parte da stack só será necessária em semanas avançadas?

---

## Saída Esperada

Crie em `assets/`:

```txt
01-reading-notes.md
```

Com seções:

- syllabus CMU;
- PyTorch;
- Hugging Face Transformers;
- Hugging Face Tokenizers;
- gaps técnicos;
- perguntas abertas.
