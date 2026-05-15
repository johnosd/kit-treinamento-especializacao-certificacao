# 05 — Exercícios

## 1. Softmax Manual

Dados os logits:

```txt
[2.0, 1.0, 0.1]
```

Calcule:

1. softmax;
2. probabilidade da classe correta se o target for índice 0;
3. cross-entropy;
4. efeito de dividir logits por temperatura 2.0.

Explique por que a distribuição fica mais ou menos concentrada.

---

## 2. Next-Token Prediction

Para a frase:

```txt
large language models require careful evaluation
```

Com contexto de tamanho 3, escreva pares `(context, target)`.

Depois explique como isso muda quando se adiciona `<bos>` e `<eos>`.

---

## 3. Token vs Palavra

Explique por que as frases abaixo podem ter custos de tokenização muito diferentes:

1. texto técnico em inglês comum;
2. nomes químicos longos;
3. código Python;
4. português com acentos;
5. identificadores de logs.

---

## 4. Perplexity

Um modelo tem cross-entropy média de 2.3.

1. Calcule perplexity aproximada.
2. Interprete o resultado.
3. Diga duas coisas que essa métrica não mede.
4. Explique por que comparar perplexity entre tokenizers diferentes pode ser enganoso.

---

## 5. Diagnóstico de Pré-Requisitos

Escolha suas duas áreas mais fracas do diagnóstico e escreva:

- por que a área é pré-requisito para LLMs;
- qual falha futura ela causaria;
- qual exercício prático você fará em 7 dias;
- como provará que melhorou.

---

## 6. Autograd

Explique, sem código:

1. o que é grafo computacional;
2. o que `backward()` calcula;
3. por que `zero_grad()` é necessário;
4. como isso se relaciona com fine-tuning de LLMs.

---

## 7. Arquitetura de Ambiente

Desenhe um ambiente mínimo para as próximas 8 semanas:

- local CPU;
- notebooks;
- scripts;
- dados;
- logs;
- checkpoints;
- cloud GPU opcional.

Inclua como você evitará perder resultados ou confundir versões.
