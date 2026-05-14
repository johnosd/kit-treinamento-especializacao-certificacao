# 08 — Flashcards

### Q: O que é um autoregressive language model?
**A:** Um modelo que estima cada token condicionado aos tokens anteriores: `P(x_t | x_<t)`.

### Q: Qual é a fatoração de uma sequência em um LM autoregressivo?
**A:** `P(x_1...x_T)=Π_t P(x_t | x_<t)`.

### Q: O que é tokenização?
**A:** Conversão de texto bruto em unidades discretas chamadas tokens.

### Q: O que é token ID?
**A:** Inteiro que representa um token no vocabulário.

### Q: O que é embedding?
**A:** Vetor denso associado a token, texto, imagem ou entidade.

### Q: O que softmax transforma?
**A:** Logits não normalizados em uma distribuição de probabilidade.

### Q: Fórmula do softmax?
**A:** `softmax(z_i)=exp(z_i)/Σ_j exp(z_j)`.

### Q: O que é cross-entropy para classe correta?
**A:** `-log p(y)`.

### Q: O que perplexity mede?
**A:** A incerteza média efetiva do modelo por token, como `exp(cross_entropy_media)`.

### Q: Por que perplexity é insuficiente?
**A:** Não mede factualidade, utilidade, segurança, robustez ou alinhamento.

### Q: Por que perplexity depende do tokenizador?
**A:** Porque a unidade de predição muda: tokens diferentes alteram comprimentos e probabilidades.

### Q: O que é next-token prediction?
**A:** Tarefa de prever o próximo token dado um prefixo.

### Q: O que é causal mask?
**A:** Máscara que impede o token atual de atender a tokens futuros.

### Q: O que é autograd?
**A:** Sistema que registra operações em tensors e calcula gradientes automaticamente.

### Q: O que `backward()` faz?
**A:** Calcula gradientes da loss em relação aos parâmetros no grafo computacional.

### Q: Por que chamar `zero_grad()`?
**A:** Gradientes acumulam por padrão; é preciso zerá-los antes do próximo passo.

### Q: O que é um tensor?
**A:** Estrutura numérica multidimensional usada em computação vetorizada e deep learning.

### Q: O que é vocabulário?
**A:** Mapeamento entre tokens e IDs.

### Q: O que é `<unk>`?
**A:** Token especial para itens fora do vocabulário.

### Q: O que é `<pad>`?
**A:** Token usado para preencher sequências em batch.

### Q: O que é `<bos>`?
**A:** Token de início de sequência.

### Q: O que é `<eos>`?
**A:** Token de fim de sequência.

### Q: O que é gap bloqueante?
**A:** Deficiência que impede progresso seguro no curso, como não entender gradiente ou probabilidade condicional.

### Q: Qual é a saída central da Semana 01?
**A:** Technical readiness audit com ambiente, diagnóstico, tokenização e plano de remediação.
