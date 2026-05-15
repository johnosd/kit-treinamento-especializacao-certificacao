# Exercícios — Semana 01

> Exercícios de prática durante a semana — distintos do assessment final.
> Entregáveis em `code/exercises/` ou `assets/`.

---

## E1. Derivar o gradiente da atenção

**Categoria:** análise (matemática)
**Tempo estimado:** 45min
**Entregável:** `assets/E1-gradient-derivation.md` com a derivação escrita à mão ou em LaTeX.

### Enunciado

Dado $\mathbf{o} = \text{softmax}(s)\mathbf{V}$ com $s = \mathbf{q}\mathbf{K}^\top / \sqrt{d_k}$, derive $\partial \mathcal{L} / \partial \mathbf{q}$ em termos de $\partial \mathcal{L} / \partial \mathbf{o}$. Assuma $\mathcal{L}$ escalar.

Dica: use a regra da cadeia em duas etapas — (1) $\partial \mathcal{L}/\partial s$ via Jacobiano do softmax, (2) $\partial \mathcal{L}/\partial \mathbf{q}$ via chain rule.

### Critérios de pass

- ✅ Jacobiano do softmax escrito corretamente: $\partial \sigma_i / \partial z_j = \sigma_i(\delta_{ij} - \sigma_j)$.
- ✅ Dimensões corretas em cada passo (não apenas resultado final).
- ✅ Identifica por que o gradiente colapsa quando o softmax satura (alta confiança → gradiente ~0).

---

## E2. Debugging — Atenção com output constante

**Categoria:** debugging
**Tempo estimado:** 30min
**Entregável:** `code/exercises/E2_debug_attention.py` com o bug identificado e corrigido.

### Enunciado

O código abaixo produz output idêntico para todos os tokens (vetor constante ao longo da dimensão seq). Identifique o bug e corrija-o sem reescrever a lógica.

```python
import numpy as np

def broken_attention(Q, K, V):
    d_k = Q.shape[-1]
    scores = Q @ K.T / np.sqrt(d_k)
    weights = np.exp(scores) / np.exp(scores).sum()  # BUG aqui
    return weights @ V

B, S, d = 2, 5, 8
Q = np.random.randn(B, S, d)
K = np.random.randn(B, S, d)
V = np.random.randn(B, S, d)
# Este código vai dar erro de shape ou resultado incorreto
out = broken_attention(Q[0], K[0], V[0])
print(out)  # Todos os vetores deveriam ser diferentes
```

### Critérios de pass

- ✅ Identifica o bug (dica: `sum()` sem `axis=-1` normaliza sobre todos os elementos, não por linha).
- ✅ Versão corrigida passa em `assert not np.allclose(out[0], out[1])`.
- ✅ Explica em 2 linhas por que o bug produz output constante.

---

## E3. Comparação: Post-LN vs Pre-LN

**Categoria:** comparação
**Tempo estimado:** 45min
**Entregável:** `assets/E3-ln-comparison.md` com diagrama e análise.

### Enunciado

(a) Escreva a expressão matemática de um bloco transformer com Post-LN (original) e com Pre-LN (LLaMA/GPT-2). As expressões devem cobrir tanto a sub-camada de atenção quanto a FFN.

(b) Argumente em ≤ 150 palavras qual das duas tem gradientes mais estáveis durante treinamento e por que. Use como evidência o comportamento do gradient norm nas camadas mais profundas.

(c) Consulte o paper do LLaMA (Touvron 2023, seção 2) para verificar qual escolha eles fazem e citar a justificativa deles.

### Critérios de pass

- ✅ Expressões matemáticas corretas para ambas as variantes.
- ✅ Argumento de estabilidade de gradiente com raciocínio causal (não apenas "Pre-LN é melhor").
- ✅ Cita LLaMA paper com paráfrase fiel da justificativa dos autores.

---

## E4. Implementar causal masking com padding mask combinada

**Categoria:** implementação
**Tempo estimado:** 1h
**Entregável:** `code/exercises/E4_combined_mask.py`

### Enunciado

Em batched inference, sequências têm comprimentos diferentes — usa-se padding (tokens extras `[PAD]`) para igualar comprimentos. A máscara final deve ser a interseção de:
- **Causal mask:** token $i$ não vê $j > i$.
- **Padding mask:** nenhum token vê posições de `[PAD]`.

Implemente `create_combined_mask(seq_len: int, padding_lengths: list[int]) -> np.ndarray` que retorna uma máscara de shape `(batch, 1, seq_len, seq_len)` booleana.

Exemplo de entrada:
```python
# Batch de 2: sequências de comprimentos reais [3, 5] em janela de seq_len=5
mask = create_combined_mask(seq_len=5, padding_lengths=[3, 5])
# seq 0: apenas posições 0,1,2 são válidas; 3,4 são padding
# seq 1: todas as 5 posições são válidas
```

### Critérios de pass

- ✅ `mask[0, 0, 2, 3]` é `False` (token 2 não vê token 3, que é padding).
- ✅ `mask[0, 0, 2, 0]` é `True` (token 2 pode ver token 0).
- ✅ `mask[0, 0, 0, 2]` é `False` (causal: token 0 não vê token 2 mesmo que seja válido).
- ✅ `mask[1, 0, 3, 2]` é `True` (seq 1 sem padding, token 3 vê token 2).

---

## E5. Analisar head specialization com attention patterns

**Categoria:** análise
**Tempo estimado:** 1h
**Entregável:** `assets/E5-head-analysis.md` com visualizações e interpretação.

### Enunciado

Use um modelo GPT-2 Small pré-treinado via HuggingFace para extrair os attention weights da layer 0 para a seguinte sentença:

```
"The cat sat on the mat and the dog lay on the rug."
```

(a) Plote os attention weights das 12 heads como heatmaps (seq × seq). Pode usar `matplotlib.imshow`.

(b) Identifique pelo menos 2 heads com padrões claramente distintos (ex: "diagonal" = atenção local, "coluna" = token especial como `.`).

(c) Consulte o paper "Attention is not Explanation" (Jain & Wallace 2019) e descreva em 100 palavras a crítica principal ao uso de attention weights como explicação.

```python
from transformers import GPT2Model, GPT2Tokenizer
model = GPT2Model.from_pretrained("gpt2", output_attentions=True)
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
```

### Critérios de pass

- ✅ Heatmaps das 12 heads da layer 0 plotados.
- ✅ ≥ 2 heads com padrões distintos identificados e nomeados.
- ✅ Crítica de Jain & Wallace citada com paráfrase fiel.

---

## E6. Implementar transformer one-liner com `einops`

**Categoria:** implementação + comparação
**Tempo estimado:** 45min
**Entregável:** `code/exercises/E6_einops_attention.py`

### Enunciado

Reimplemente `scaled_dot_product_attention` usando `einops.einsum` e `einops.rearrange` em vez de `np.matmul` e `reshape/transpose`. Compare a legibilidade com a implementação do lab guiado.

```bash
pip install einops
```

Exemplo de uso esperado:
```python
from einops import einsum, rearrange
# Q: (batch heads seq_q d_k)
# K: (batch heads seq_k d_k)
scores = einsum(Q, K, 'b h sq dk, b h sk dk -> b h sq sk') / np.sqrt(d_k)
```

### Critérios de pass

- ✅ Resultado idêntico à implementação NumPy (max_diff < 1e-7).
- ✅ Código usa `einops` e não `@`/`transpose` diretamente.
- ✅ Comentário de 1 linha: qual versão você prefere para legibilidade e por quê.
