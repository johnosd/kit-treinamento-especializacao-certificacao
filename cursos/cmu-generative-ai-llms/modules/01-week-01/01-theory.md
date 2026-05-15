# 01 — Week 01 Theory — Diagnóstico Técnico e Setup

## Objetivo da Semana

A primeira semana não é uma introdução leve a IA generativa. Ela é uma auditoria técnica: você valida se tem base suficiente para acompanhar um programa no estilo CMU em LLMs, sistemas e multimodalidade.

Ao final da semana, você deve ter:

- ambiente Python validado;
- diagnóstico honesto de gaps em ML, NLP, PyTorch, probabilidade e sistemas;
- pipeline mínimo de tokenização e tensorização;
- entendimento operacional de `softmax`, `cross-entropy`, `perplexity` e `next-token prediction`;
- plano de remediação para pré-requisitos fracos.

---

## 1. O Que Significa Estar Pronto Para LLMs

LLMs combinam várias camadas técnicas:

| Camada | Exigência |
|---|---|
| Matemática | álgebra linear, probabilidade, otimização, estatística |
| ML | supervised learning, generalização, loss, validação |
| NLP | tokenização, embeddings, sequência, language modeling |
| Deep Learning | backpropagation, autograd, tensors, GPUs |
| Sistemas | memória, paralelismo, throughput, latency, deployment |
| Avaliação | benchmarks, contaminação, análise humana, failure modes |

Se uma dessas camadas é fraca, o sintoma aparece mais tarde como implementação frágil, leitura superficial de papers ou decisões ruins de arquitetura.

---

## 2. Language Modeling Como Problema Probabilístico

Um language model estima uma distribuição sobre sequências. Para tokens `x_1, x_2, ..., x_T`, um modelo autoregressivo usa a fatoração:

```txt
P(x_1, ..., x_T) = Π_t P(x_t | x_1, ..., x_{t-1})
```

Em um decoder-only LM, o objetivo típico é prever o próximo token dado o prefixo. O dataset vira pares:

```txt
input:  [x_1, x_2, ..., x_{t-1}]
target: x_t
```

Esse detalhe importa porque quase tudo no curso depende dele:

- causal masks em Transformers;
- perplexity;
- decoding;
- KV cache;
- exposure bias;
- avaliação de modelos generativos.

---

## 3. Tokens, Vocabulário e Tensorização

Texto bruto não entra diretamente no modelo. O caminho mínimo é:

```mermaid
flowchart LR
    Text[Texto bruto] --> Normalize[Normalização]
    Normalize --> Tokenize[Tokenização]
    Tokenize --> Vocab[Vocabulário]
    Vocab --> IDs[Token IDs]
    IDs --> Tensor[Tensor]
    Tensor --> Model[Modelo]
```

Na prática:

- **tokenização** define unidades discretas;
- **vocabulário** mapeia token para ID inteiro;
- **tensorização** transforma IDs em tensores numéricos;
- **embedding layer** transforma IDs em vetores densos treináveis.

Pitfalls iniciais:

- confundir palavra com token;
- ignorar tokens especiais (`<unk>`, `<pad>`, `<bos>`, `<eos>`);
- comparar custos de modelos sem considerar tokens;
- esquecer que tokenização pode penalizar idiomas ou domínios.

---

## 4. Softmax

Modelos de linguagem produzem logits: números reais não normalizados para cada token do vocabulário.

Softmax transforma logits `z` em probabilidades:

```txt
softmax(z_i) = exp(z_i) / Σ_j exp(z_j)
```

Propriedades importantes:

- probabilidades somam 1;
- diferenças relativas nos logits controlam confiança;
- valores extremos podem causar instabilidade numérica;
- temperatura em decoding altera a concentração da distribuição.

Implementação numericamente estável subtrai o maior logit antes da exponencial.

---

## 5. Cross-Entropy

Para uma classe correta `y`, a cross-entropy é:

```txt
L = -log p(y)
```

Para language modeling, isso é calculado por token e depois agregado. Se o modelo atribui baixa probabilidade ao token correto, a loss aumenta.

Interpretação:

- `p(y)=1.0` implica loss 0;
- `p(y)=0.5` implica loss aproximada 0.693;
- `p(y)=0.01` implica loss aproximada 4.605.

Cross-entropy é sensível à calibração probabilística. Ela pune confiança errada com força.

---

## 6. Perplexity

Perplexity é a exponencial da cross-entropy média:

```txt
PPL = exp(mean_cross_entropy)
```

Intuição técnica: se `PPL = 20`, o modelo está tão incerto quanto escolher entre 20 alternativas efetivas em média. Essa interpretação é aproximada e depende do tokenizador e do corpus.

Pitfalls:

- perplexity não mede factualidade;
- perplexity não mede utilidade em RAG;
- perplexity não mede segurança;
- comparar perplexity entre tokenizadores diferentes pode ser enganoso.

---

## 7. Autograd e Backpropagation

PyTorch constrói um grafo computacional dinâmico. Operações em tensors com `requires_grad=True` permitem calcular gradientes por backpropagation.

Fluxo mínimo:

```txt
forward -> loss -> backward -> optimizer.step -> zero_grad
```

O erro comum é tratar `backward()` como magia. Ele aplica regra da cadeia sobre operações registradas no grafo.

Para LLMs, autograd é a base para:

- treinar embeddings;
- atualizar pesos de attention/MLP;
- fine-tuning;
- PEFT/LoRA;
- gradient checkpointing;
- distributed training.

---

## 8. Setup Técnico Esperado

Ambiente mínimo:

- Python 3.10+;
- ambiente virtual;
- Git;
- PyTorch;
- Hugging Face `transformers`;
- Hugging Face `tokenizers`;
- `numpy`;
- opcional: CUDA/GPU.

Ambiente avançado futuro:

- cloud GPU;
- Hugging Face Hub;
- experiment tracking;
- vLLM;
- PEFT;
- vector database;
- Ray/DeepSpeed.

Na Semana 01, o código roda sem esses pacotes, mas o diagnóstico deve registrar o que falta.

---

## 9. Critério de Prontidão

Você está pronto para seguir para a Semana 02 se consegue:

1. explicar `P(x_t | x_<t)`;
2. calcular softmax manualmente;
3. explicar cross-entropy sem analogia superficial;
4. explicar por que perplexity é útil e insuficiente;
5. transformar texto em IDs;
6. diferenciar token, token ID, embedding e tensor;
7. rodar um script Python reproduzível;
8. listar gaps técnicos com plano de correção.
