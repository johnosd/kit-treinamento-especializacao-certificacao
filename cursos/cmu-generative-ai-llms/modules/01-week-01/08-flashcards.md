# Flashcards — Semana 01

> Formato compatível com Anki. Importe como CSV ou cole manualmente.
> 20 cards — priorizados por frequência de aparição em exames e interviews.

---

## Conceitos

### C1
**Frente:** Qual a fórmula de Scaled Dot-Product Attention e por que o fator de escala é $\sqrt{d_k}$ especificamente?
**Verso:** $\text{Attention}(Q,K,V) = \text{softmax}(QK^\top / \sqrt{d_k}) V$. O fator $\sqrt{d_k}$: se $q_i, k_i \sim \mathcal{N}(0,1)$, então $\text{Var}(q \cdot k) = d_k$. Sem scaling, softmax satura para $d_k$ grande, gradientes → 0. Dividir por $\sqrt{d_k}$ normaliza variância para 1.
**Tags:** semana-01, attention, fundamentos

---

### C2
**Frente:** Qual a diferença entre Post-LN e Pre-LN em um bloco Transformer? Qual é usado em LLaMA/GPT-2+?
**Verso:** Post-LN (original): `LN(x + Attention(x))`. Pre-LN (moderno): `x + Attention(LN(x))`. LLaMA/GPT-2 usam Pre-LN. Razão: gradientes mais estáveis nas primeiras layers — Post-LN pode ter gradient norm alto nas camadas superficiais.
**Tags:** semana-01, layer-norm, arquitetura

---

### C3
**Frente:** Por que Transformers precisam de positional encoding? O que acontece sem ele?
**Verso:** Transformers são permutation-invariant: atenção só usa dot products entre tokens, não posição. Sem PE, "the cat sat" e "sat cat the" produzem outputs idênticos. O modelo não pode diferenciar ordem de palavras.
**Tags:** semana-01, positional-encoding, fundamentos

---

### C4
**Frente:** Qual a complexidade computacional por layer do Transformer em função de n (seq_len) e d (d_model)?
**Verso:** $O(n^2 d)$ em tempo (dominado pelo cálculo de scores $QK^\top$) e $O(n^2)$ em memória (para materializar a matriz de atenção). Para n≫d, o custo quadrático em n domina.
**Tags:** semana-01, complexidade, scaling

---

### C5
**Frente:** Quais as 3 diferenças arquiteturais entre BERT e GPT-2?
**Verso:** 1) BERT: encoder-only, atenção bidirecional; GPT-2: decoder-only, causal masking. 2) BERT: treinado com MLM (15% masking); GPT-2: treinado com CLM (prediz próximo token). 3) BERT: produz representações para NLU; GPT-2: gera texto autoregressivamente.
**Tags:** semana-01, bert, gpt, arquitetura

---

## Fórmulas

### F1
**Frente:** Escreva a expressão de Multi-Head Attention completa (não só a atenção simples).
**Verso:** $\text{MHA}(Q,K,V) = \text{Concat}(\text{head}_1,\ldots,\text{head}_h) W^O$ onde $\text{head}_i = \text{Attention}(QW_i^Q, KW_i^K, VW_i^V)$. Dimensões: $W_i^Q, W_i^K \in \mathbb{R}^{d_{\text{model}} \times d_k}$ com $d_k = d_{\text{model}}/h$.
**Tags:** semana-01, mha, fórmulas

---

### F2
**Frente:** Qual o objetivo de pré-treinamento CLM? Escreva a fórmula da loss.
**Verso:** $\mathcal{L}_{\text{CLM}} = -\sum_{t=1}^{T} \log P_\theta(x_t \mid x_1,\ldots,x_{t-1})$. Prediz cada token dado o contexto anterior. Usado por GPT-2, LLaMA, Claude. Permite geração autoregressiva direta.
**Tags:** semana-01, pre-training, clm, fórmulas

---

### F3
**Frente:** Qual o objetivo de pré-treinamento MLM do BERT? Qual % de tokens é mascarado e como?
**Verso:** $\mathcal{L}_{\text{MLM}} = -\sum_{t \in \mathcal{M}} \log P_\theta(x_t \mid x_{\setminus \mathcal{M}})$. 15% dos tokens são selecionados: 80% → `[MASK]`, 10% → token aleatório, 10% → inalterados. O 10% aleatório e 10% inalterado previnem o modelo de "trapacear" usando apenas a posição do `[MASK]`.
**Tags:** semana-01, mlm, bert, fórmulas

---

### F4
**Frente:** Quantos parâmetros tem a camada MHA de um transformer com d_model=512, n_heads=8?
**Verso:** $W^Q + W^K + W^V$: $3 \times 512 \times 512 = 786{,}432$. $W^O$: $512 \times 512 = 262{,}144$. Total: $\approx 1.05$M por layer de atenção (sem bias). Nota: esse número não muda com n_heads — a distribuição muda, não o total.
**Tags:** semana-01, parâmetros, arquitetura

---

### F5
**Frente:** Qual a expressão do positional encoding sinusoidal para posição pos e dimensão 2i?
**Verso:** $\text{PE}(pos, 2i) = \sin(pos / 10000^{2i/d_{\text{model}}})$; $\text{PE}(pos, 2i+1) = \cos(pos / 10000^{2i/d_{\text{model}}})$. Propriedade: $\text{PE}(pos+k)$ = transformação linear de $\text{PE}(pos)$ para qualquer $k$ fixo.
**Tags:** semana-01, positional-encoding, fórmulas

---

## Arquitetura

### A1
**Frente:** Desenhe (em texto) o fluxo de dados em um bloco decoder-only (Pre-LN). Inclua todas as sub-camadas e residual connections.
**Verso:** `x → LN → MHA(causal) → + x → h → LN → FFN → + h → output`. Expandido: `h = MHA(LN(x)) + x; output = FFN(LN(h)) + h`. Causal mask garante que token t vê apenas tokens 0..t.
**Tags:** semana-01, decoder, arquitetura

---

### A2
**Frente:** O que é `batch_first` no `nn.MultiheadAttention` do PyTorch? Qual o default e por que é importante?
**Verso:** `batch_first=False` é o default: input esperado como `(seq, batch, d_model)`. Com `batch_first=True`: `(batch, seq, d_model)`. Importante: muitos bugs surgem de mismatch de convenção — sempre declarar explicitamente ao usar `nn.MultiheadAttention`.
**Tags:** semana-01, pytorch, arquitetura

---

### A3
**Frente:** Por que `d_ff = 4 × d_model` na FFN? O que acontece se usar d_ff menor?
**Verso:** O fator 4 é heurístico estabelecido em Vaswani 2017 e seguido na literatura. A FFN funciona como "memória" de fatos: capacidade menor → memorização reduzida. Experimentos no paper T5 (Raffel 2020) mostraram que reduzir para 2× degrada quality; aumentar para 8× tem ganhos marginais com muito mais compute.
**Tags:** semana-01, ffn, arquitetura

---

## Pitfalls

### P1
**Frente:** Qual é o pitfall de softmax sem shift por max? Quando ele falha e como corrigir?
**Verso:** `exp(x) / exp(x).sum()` → overflow para x > 709 (float64) ou x > 89 (float32). Solução: `x -= x.max(); exp(x) / exp(x).sum()`. O shift cancela matematicamente (divide numerador e denominador por `exp(max)`), mas previne overflow computacionalmente.
**Tags:** semana-01, softmax, pitfalls, implementação

---

### P2
**Frente:** Por que `w.sum(-1) != 1.0` indica um bug em MHA? O que provavelmente está errado?
**Verso:** Attention weights devem somar 1 por query (eixo -1 = keys). Se não somam 1: softmax foi aplicado no eixo errado (ex: `dim=1` em vez de `dim=-1`), ou o tensor foi transposto incorretamente antes do softmax. Use `assert np.allclose(w.sum(-1), 1.0, atol=1e-6)` como sanity check obrigatório.
**Tags:** semana-01, mha, pitfalls, debugging

---

### P3
**Frente:** Qual o pitfall de inicializar todas as heads de MHA com o mesmo seed? O que acontece durante o treinamento?
**Verso:** Heads idênticas criam simetria que o gradiente não quebra — todas as heads aprendem o mesmo padrão de atenção. O benefício do MHA (múltiplos subespações) é perdido. Sempre usar seeds distintos por head, ou inicialização com variância diferente por head.
**Tags:** semana-01, mha, pitfalls, treinamento

---

### P4
**Frente:** Por que não usar `x.T` para transpor K em batch attention? Qual a correção?
**Verso:** `x.T` transpõe **todos** os eixos do tensor. Para K de shape `(batch, heads, seq_k, d_k)`, `K.T` produz `(d_k, seq_k, heads, batch)` — completamente errado. O correto é `K.swapaxes(-2, -1)` (ou `K.transpose(-2,-1)` em PyTorch) que troca apenas os dois últimos eixos: `(batch, heads, d_k, seq_k)`.
**Tags:** semana-01, numpy, pitfalls, implementação

---

## Limitações

### L1
**Frente:** Qual a limitação fundamental do Transformer original (Vaswani 2017) para sequências longas? Quais papers a endereçaram?
**Verso:** Complexidade quadrática $O(n^2)$ em memória e tempo. E positional encoding sinusoidal não generaliza para n maiores que os vistos em treino. Papers: ALiBi (Press 2022) e RoPE (Su 2021) para PE; FlashAttention (Dao 2022) para complexidade de IO; Longformer (Beltagy 2020) para sparse attention.
**Tags:** semana-01, limitações, transformer

---

### L2
**Frente:** Por que BERT não pode ser usado diretamente para geração de texto (ex: completar frases)?
**Verso:** BERT usa MLM com atenção bidirecional — cada token vê todos os outros. Geração exige processamento autoregressivo: o token T só pode depender de tokens 0..T-1. Sem causal masking, BERT não tem esse constraint. Usar BERT para geração requereria modificação arquitetural (ex: UniLM, BERT-for-generation) ou usar variante encoder-decoder (T5).
**Tags:** semana-01, bert, limitações, geração

---

### L3
**Frente:** O que é "Attention is not Explanation" (Jain & Wallace 2019) e qual a implicação prática?
**Verso:** O paper argumenta que attention weights não são necessariamente explicações causais das predições — é possível modificar os pesos de atenção sem mudar o output do modelo, e correlações de atenção com importância de features não implicam causalidade. Implicação: não use heatmaps de atenção como "explicação" de decisões do modelo em aplicações críticas (saúde, legal) sem análise mais rigorosa.
**Tags:** semana-01, interpretabilidade, limitações

---

## Comandos

### CMD1
**Frente:** Qual o comando PyTorch para verificar que os attention weights somam 1 por query?
**Verso:** `assert torch.allclose(weights.sum(dim=-1), torch.ones_like(weights.sum(dim=-1)), atol=1e-6)`. Ou em NumPy: `assert np.allclose(weights.sum(-1), 1.0, atol=1e-6)`. Deve ser o primeiro assert após qualquer implementação de softmax em atenção.
**Tags:** semana-01, pytorch, debugging, comandos
