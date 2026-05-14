# 07 — Assessment

Responda sem consultar os arquivos. Depois revise.

## Parte A — Conceitos

1. O que é um autoregressive language model?
2. Escreva a fatoração de probabilidade de uma sequência.
3. Qual é a diferença entre token, token ID, embedding e tensor?
4. O que softmax faz com logits?
5. Por que softmax precisa de cuidado numérico?
6. O que cross-entropy mede?
7. Como perplexity se relaciona com cross-entropy?
8. Por que perplexity não mede factualidade?
9. O que é autograd?
10. Qual é o papel de `zero_grad()` em PyTorch?

## Parte B — Implementação

1. Descreva o pipeline mínimo para transformar texto em pares `(context, target)`.
2. Que tokens especiais você adicionaria em um tokenizer real?
3. Como você detectaria que a tokenização penaliza um domínio específico?
4. Que informações um relatório de ambiente precisa conter?
5. O que muda quando o pipeline usa Hugging Face Tokenizers em vez de whitespace tokenization?

## Parte C — Design Review

Você precisa preparar ambiente para as próximas 8 semanas do curso. Especifique:

- versão de Python;
- ambiente virtual;
- pacotes mínimos;
- estratégia para GPU/cloud;
- estrutura de diretórios;
- rastreamento de experimentos;
- política para dados e checkpoints.

## Parte D — Debugging

Explique a causa provável:

1. Loss vira `nan`.
2. Tensor tem shape inesperado.
3. GPU não aparece para PyTorch.
4. Dois runs dão resultados diferentes.
5. Tokenizer gera muitas unidades para termos técnicos.
6. Perplexity melhora, mas respostas pioram.

## Parte E — Aprovação

Você passa se consegue:

- resolver Parte A com 80% de precisão;
- executar os três scripts do lab;
- gerar readiness audit;
- defender go/no-go para Semana 02;
- listar pelo menos 5 gaps e ações de correção.
