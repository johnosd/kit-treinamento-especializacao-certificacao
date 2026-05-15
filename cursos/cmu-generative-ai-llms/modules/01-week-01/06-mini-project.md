# Mini-Project — Semana 01: Single-Layer Transformer Block Validado

> **Tempo estimado:** 4–5h
> **Conexão:** Este bloco NumPy será extendido na S02 (RoPE, RMSNorm) e S07 (profiling de training loop). É o artefato base de toda a parte de implementação do Módulo 1.

---

## Objetivo

Construir um bloco transformer completo — Pre-LN + MHA + FFN + residual connections — em NumPy puro. A métrica de sucesso não é "roda sem erro" mas equivalência numérica verificada contra a implementação PyTorch equivalente, com um gap < 1e-5. Ao final você terá um transformer block que você entende em cada linha — sem caixa preta.

---

## Especificação técnica

**Inputs:**
- `x`: tensor de shape `(batch=2, seq=20, d_model=64)`, dtype `float32`.
- Pesos gerados com `np.random.default_rng(42)`.

**Outputs:**
- `output`: mesmo shape do input `(batch, seq, d_model)` — os transformers são shape-invariant.
- `attention_weights`: `(batch, n_heads, seq, seq)`.

**Arquitetura a implementar:**
```
Pre-LN Transformer Block:
  h = MHA(LayerNorm(x)) + x          ← sub-camada 1 com residual
  y = FFN(LayerNorm(h)) + h          ← sub-camada 2 com residual

FFN:
  FFN(z) = W2 · ReLU(W1 · z)
  d_ff = 4 × d_model = 256
```

**Restrições:**
- Apenas NumPy (sem PyTorch no bloco em si — PyTorch só para validação final).
- `n_heads = 8`, `d_model = 64`, `d_ff = 256`.
- Sem bias em nenhuma camada (compatível com PyTorch default `bias=False`).

---

## Entregáveis

1. `code/mini-project/transformer_block.py` — implementação completa.
2. `code/mini-project/validate_block.py` — script de validação contra PyTorch.
3. `assets/mini-project-report.md` — relatório seguindo o template abaixo.

---

## Critérios de aceitação

- ✅ `max_diff(output_numpy, output_pytorch) < 1e-5`.
- ✅ `output.shape == (2, 20, 64)` confirmado por assertion.
- ✅ Residual connection verificada: `output ≠ input` mas `output - mha_out - ffn_out ≈ input` (em valor absoluto, diferença < 1e-5).
- ✅ `assets/mini-project-report.md` preenchido com métricas medidas.

---

## Template do relatório (`assets/mini-project-report.md`)

```
# Mini-Project Report — Semana 01

## Arquitetura implementada

[Diagrama ou descrição das camadas em ordem]

## Validação numérica

- max_diff: ___
- Passou critério < 1e-5: Sim / Não
- Se não passou: bug identificado e como foi corrigido

## Checklist de invariantes verificados

- [ ] output.shape == (batch, seq, d_model)
- [ ] LayerNorm produz média ≈ 0 e variância ≈ 1 por token
- [ ] ReLU mantém não-negatividade no hidden state do FFN
- [ ] Residual: output sem residual connection difere de output com residual

## Insight técnico

[1 parágrafo: algo que você aprendeu que não estava óbvio antes de implementar]
```

---

## Extensões opcionais

**E1 (conecta com S02):** Substitua o Layer Norm por RMS Norm: $\text{RMSNorm}(x) = x / \text{rms}(x) \cdot \gamma$ onde $\text{rms}(x) = \sqrt{(1/d)\sum x_i^2}$. Verifique que a diferença de performance é negligível mas a implementação é mais simples.

**E2 (conecta com S07):** Adicione contagem de FLOPs manual para o bloco completo. Verifique que sua fórmula bate com a do paper de Kaplan 2020 (seção 2.1) para a configuração usada.

**E3 (conecta com S29):** Profile a memória do forward pass com diferentes seq_len (64, 128, 256, 512). Trace o crescimento de memória e confirme que é $O(n^2)$ — este é o custo que FlashAttention endereça.
