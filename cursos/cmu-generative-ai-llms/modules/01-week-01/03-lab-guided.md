# Lab Guiado — Semana 01

> **Estimativa:** 2.5h (setup 15min + implementação NumPy 1h + comparação PyTorch 45min + análise 30min)
> **Pré-requisitos:** NumPy ≥ 1.24, PyTorch ≥ 2.0, Python 3.10+
> **Ambiente:** local CPU (sem GPU necessário — sequências curtas)

---

## Objetivo

Ao final deste lab você terá implementado scaled dot-product attention e Multi-Head Self-Attention completos em NumPy puro — sem autograd, sem frameworks. Você comparará o output numérico com `torch.nn.MultiheadAttention` com pesos idênticos, verificando igualdade dentro de tolerância de ponto flutuante. Este processo de "implementar do zero e validar contra framework" é o padrão de trabalho de research engineers que precisam entender exatamente o que o framework está fazendo.

---

## Resultado esperado

- ✅ Diferença máxima entre output NumPy e PyTorch: `max_diff < 1e-5` (FP32).
- ✅ Weights de atenção somam 1.0 por linha (propriedade do softmax): `|weights.sum(-1) - 1.0| < 1e-6`.
- ✅ Output shape correto: `(batch=2, seq=10, d_model=64)`.
- ✅ Script de benchmark documenta tempo de forward pass para batch=1, seq=[64, 256, 512].

---

## Setup

```bash
cd cursos/cmu-generative-ai-llms/modules/01-week-01/code
pip install -r requirements.txt
python 01_environment_check.py
```

**Saída esperada do sanity check:**
```
[OK] Python 3.10+
[OK] NumPy 1.26.x
[OK] PyTorch 2.x (CPU)
[OK] random seed fixo: array([0.37454012, 0.95071431])
Setup OK — pronto para o lab.
```

Se aparecer `[FAIL]` em qualquer linha, resolva antes de prosseguir. Problemas comuns: versão incompatível do PyTorch com Python 3.12 (`pip install torch --index-url https://download.pytorch.org/whl/cpu`).

---

## Passos

### Passo 1 — Implementar softmax numericamente estável

**Objetivo:** Entender por que softmax ingênuo falha com valores grandes.

**Código:** `code/02_self_attention_numpy.py`, funções `softmax_naive` e `softmax_stable` (linhas 1–40).

**O que está acontecendo:** O softmax ingênuo `exp(x) / sum(exp(x))` produz `inf/inf = NaN` para valores acima de ~709 (limite do `float64`). Para attention scores sem scaling, `d_k=512` produz dot products com desvio padrão $\approx\sqrt{512}\approx 22$ — valores que facilmente causam overflow em treinamento. O shift por `max(x)` não altera o resultado matematicamente (divide numerador e denominador por `exp(max)`), mas mantém os exponentes no intervalo computável.

```python
# Ingênuo — falha para scores > 709
scores_naive = np.array([1000.0, 1001.0, 1002.0])
print(np.exp(scores_naive) / np.exp(scores_naive).sum())  # nan nan nan

# Estável
x_shifted = scores_naive - scores_naive.max()  # [-2, -1, 0]
print(np.exp(x_shifted) / np.exp(x_shifted).sum())  # [0.090, 0.245, 0.665]
```

**Verificação:**
```bash
python -c "import numpy as np; x = np.array([1000., 1001., 1002.]); x_s = x - x.max(); print(np.exp(x_s)/np.exp(x_s).sum())"
# Deve imprimir: [0.09003057 0.24472847 0.66524096]
```

**Troubleshooting:**
- `RuntimeWarning: overflow encountered in exp` → você está usando softmax ingênuo; mude para o shift.
- `nan` no output → mesmo problema; verifique se o shift está sendo aplicado antes do `exp`.

---

### Passo 2 — Implementar scaled dot-product attention

**Objetivo:** Implementar e verificar a fórmula $\text{softmax}(QK^\top / \sqrt{d_k})V$.

**Código:** `code/02_self_attention_numpy.py`, função `scaled_dot_product_attention` (linhas 42–80).

**O que está acontecendo:** O fator $\sqrt{d_k}$ é a decisão técnica central. Se $q_i, k_i \sim \mathcal{N}(0,1)$, então $q \cdot k = \sum_{i=1}^{d_k} q_i k_i$ tem variância $d_k$. Para `d_k=64`, o desvio padrão dos scores sem scaling é $8$ — o softmax tende a concentrar toda a probabilidade no máximo, produzindo gradientes próximos de zero para os demais tokens. O scaling normaliza a variância para 1.

Execute o experimento numérico no script:
```bash
python 02_self_attention_numpy.py --experiment scaling_effect
```
Saída esperada:
```
d_k=16:  softmax entropy (sem scale): 0.41 | (com scale): 1.89
d_k=64:  softmax entropy (sem scale): 0.09 | (com scale): 1.87
d_k=256: softmax entropy (sem scale): 0.01 | (com scale): 1.88
```
A entropia da distribuição softmax colapsa conforme $d_k$ cresce sem scaling — o modelo fica "mais determinístico" artificialmente.

**Verificação (shapes):**
```python
B, H, S, d_k = 2, 4, 10, 16
Q = np.random.randn(B, H, S, d_k)
K = np.random.randn(B, H, S, d_k)
V = np.random.randn(B, H, S, d_k)
out, weights = scaled_dot_product_attention(Q, K, V)
assert out.shape == (B, H, S, d_k)
assert weights.shape == (B, H, S, S)
assert np.allclose(weights.sum(-1), 1.0, atol=1e-6)
print("Shape assertions OK")
```

**Troubleshooting:**
- `shape mismatch in @` → verifique que K está transposto com `.swapaxes(-2, -1)`, não `.T` (que transpõe todas as dimensões).
- Weights não somam 1 → softmax não está sendo aplicado no último eixo (`axis=-1`).

---

### Passo 3 — Implementar Multi-Head Self-Attention completo

**Objetivo:** Conectar projeções W_Q, W_K, W_V, split de heads, atenção, e W_O.

**Código:** `code/02_self_attention_numpy.py`, classe `MultiHeadSelfAttention` (linhas 82–140).

**O que está acontecendo:** A "mágica" do MHA não está na atenção em si — está nos splits. Cada head opera em $d_k = d_{\text{model}}/h$ dimensões, mas as projeções $W_i^Q, W_i^K, W_i^V$ são distintas para cada head. Na implementação eficiente, não criamos $h$ matrizes separadas: criamos uma única $W^Q \in \mathbb{R}^{d_{\text{model}} \times d_{\text{model}}}$, aplicamos, e depois reshapeamos. Isso permite uma única operação GEMM grande em vez de $h$ GEMMs pequenos — muito mais eficiente em GPU.

O `_split_heads` faz: `(batch, seq, d_model) → (batch, n_heads, seq, d_k)` via reshape + transpose. O transpose é necessário porque queremos processar cada head de forma independente; sem ele, os $d_k$ primeiros valores de cada posição seriam a head 0 mas o batch dimension estaria no lugar errado.

**Verificação:**
```bash
python 02_self_attention_numpy.py --experiment mha_shapes
```
```
Input shape: (2, 10, 64)
After W_Q: (2, 10, 64)
After split_heads: (2, 8, 10, 8)
After attention: (2, 8, 10, 8)
After merge heads: (2, 10, 64)
After W_O: (2, 10, 64)
All assertions OK
```

**Troubleshooting:**
- Output tem valores `nan` → verifique se as matrizes de peso foram inicializadas corretamente (não todas-zero).
- Shape wrong após `_split_heads` → a ordem dos eixos no reshape deve ser `(B, S, n_heads, d_k)` antes do transpose.

---

### Passo 4 — Comparar com PyTorch `nn.MultiheadAttention`

**Objetivo:** Verificar equivalência numérica — se diferem, há bug na implementação NumPy.

**Código:** `code/03_compare_attention.py`

**O que está acontecendo:** `torch.nn.MultiheadAttention` aceita `in_proj_weight` (concatenação de W_Q, W_K, W_V) e `out_proj.weight`. Para comparar com nossa implementação NumPy, precisamos:
1. Criar a camada PyTorch com `bias=False` (nosso NumPy não tem bias).
2. Copiar os pesos NumPy para o estado do PyTorch (`load_state_dict`).
3. Rodar forward em ambos com o mesmo input.
4. Comparar outputs com `np.allclose(tol=1e-5)`.

**Detalhe crítico:** PyTorch normaliza `in_proj_weight` como `[W_Q; W_K; W_V]` (concatenação vertical) — diferente de três matrizes separadas. O script faz essa conversão automaticamente.

```bash
python 03_compare_attention.py
```

Saída esperada:
```
NumPy output:  shape (2, 10, 64), mean=0.0023, std=0.9841
PyTorch output: shape (2, 10, 64), mean=0.0023, std=0.9841
Max absolute difference: 3.8e-7
PASS: outputs são numericamente equivalentes (tol=1e-5)
```

Se aparecer `FAIL: max_diff=X.Xe-3`:
1. Verifique a ordem de concatenação dos pesos em `in_proj_weight`.
2. PyTorch usa `embed_dim` como primeiro argumento: `nn.MultiheadAttention(embed_dim=d_model, num_heads=n_heads)`.
3. Confirme `batch_first=True` — o padrão PyTorch é `(seq, batch, d_model)`, não `(batch, seq, d_model)`.

---

### Passo 5 — Causal masking

**Objetivo:** Implementar e verificar máscara triangular inferior para geração autoregressiva.

**Código:** `code/02_self_attention_numpy.py`, função `create_causal_mask` e uso em `scaled_dot_product_attention`.

**O que está acontecendo:** Em geração, o token na posição $t$ não deve "ver" tokens nas posições $t+1, \ldots, T$. Implementamos isso colocando $-10^9$ nas posições acima da diagonal antes do softmax. Após `exp(-1e9) ≈ 0`, esses tokens têm peso de atenção praticamente nulo.

```python
def create_causal_mask(seq_len: int) -> np.ndarray:
    # True = posição VISÍVEL (mantém o score)
    # Lower triangular matrix (inclusive diagonal)
    return np.tril(np.ones((seq_len, seq_len), dtype=bool))
    # Shape: (seq, seq) — broadcast para (batch, heads, seq, seq) no attention

# Verificação: token 0 vê apenas ele mesmo
# Token 1 vê tokens 0 e 1
# Token T-1 vê todos os anteriores
mask = create_causal_mask(5)
assert mask[0, :].tolist() == [True, False, False, False, False]
assert mask[4, :].tolist() == [True, True, True, True, True]
```

**Verificação:**
```bash
python 02_self_attention_numpy.py --experiment causal_mask
```
```
Attention weights sem máscara (token 0):  [0.23, 0.18, 0.21, 0.19, 0.19]  ← vê todos
Attention weights com máscara (token 0):  [1.00, 0.00, 0.00, 0.00, 0.00]  ← vê só ele
Attention weights com máscara (token 3):  [0.28, 0.19, 0.27, 0.26, 0.00]  ← vê tokens 0-3
PASS: causal mask correto
```

---

## Profiling

```bash
# Tempo de forward pass por seq_len
python 02_self_attention_numpy.py --benchmark
```

Tabela de referência (CPU, NumPy, sem otimizações):

| seq_len | d_model | n_heads | Tempo médio (ms) | Memória (MB) |
|---|---|---|---|---|
| 64 | 64 | 8 | ~0.8 | ~0.1 |
| 256 | 64 | 8 | ~12 | ~1.6 |
| 512 | 64 | 8 | ~48 | ~6.4 |
| 1024 | 64 | 8 | ~192 | ~25 |

**Padrão observável:** tempo $\propto n^2$ (quadrático) conforme sequência cresce — manifesta-se como 4× mais tempo ao dobrar a sequência. Essa é a complexidade que FlashAttention (S29) endereça.

**Profiling com Python:**
```bash
python -m cProfile -s cumulative 02_self_attention_numpy.py --benchmark 2>&1 | head -30
```

---

## Interpretação de resultados

Preencha o template em `assets/01-lab-report.md` com:
1. O valor de `max_diff` obtido na comparação NumPy vs PyTorch. Se > 1e-4, investigar e corrigir antes de continuar.
2. Os tempos medidos no benchmark e a relação observada entre seq_len e tempo (linear, quadrática, ou outra?).
3. Entropy do softmax com e sem scaling para `d_k=64` — o experimento do Passo 2 deve mostrar diferença de ordem de magnitude.
4. Resposta à pergunta: "Se você quiser que o token 5 não veja o token 3, mas possa ver o token 7, como você modificaria a máscara?"

---

## Failure modes observados

**OOM mesmo em CPU:** `d_model` muito grande com `seq_len` longa. Reduza um dos dois.

**Outputs idênticos em todas as heads:** Verifique se as projeções W_Q, W_K, W_V foram inicializadas com seeds distintos por head. Inicializar com a mesma seed cria heads idênticas — simetria que o gradiente não quebra.

**max_diff > 1e-3 na comparação:** Quase sempre é erro na ordem de concatenação dos pesos. PyTorch usa `[W_Q; W_K; W_V]` (stack vertical), não `W_Q | W_K | W_V` (horizontal).

**Weights de atenção não somam 1:** softmax aplicado no eixo errado (`axis=-2` em vez de `axis=-1`).

---

## Próximo passo

Este lab produz `MultiHeadSelfAttention` em NumPy com pesos validados contra PyTorch. Na S02, você adicionará:
1. RoPE como substituto do PE sinusoidal (altera como Q e K são rotacionados antes do dot-product).
2. RMSNorm em vez de LayerNorm.
3. GQA (heads de K e V compartilhadas entre grupos de heads de Q).

O artefato NumPy desta semana será estendido nesses labs subsequentes.
