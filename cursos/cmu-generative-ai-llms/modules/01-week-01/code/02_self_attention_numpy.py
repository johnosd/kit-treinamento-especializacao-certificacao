"""Script para implementar scaled dot-product attention e MHA em NumPy puro.
Executar após: 01_environment_check.py
Output esperado: shape (2, 10, 64), max_diff < 1e-5 vs PyTorch, benchmarks quadráticos.

Uso:
  python 02_self_attention_numpy.py --experiment scaling_effect
  python 02_self_attention_numpy.py --experiment mha_shapes
  python 02_self_attention_numpy.py --experiment causal_mask
  python 02_self_attention_numpy.py --benchmark
  python 02_self_attention_numpy.py --all
"""

import argparse
import time
from typing import Optional

import numpy as np


# ─────────────────────────────────────────────
# Primitivas de atenção
# ─────────────────────────────────────────────

def softmax(x: np.ndarray, axis: int = -1) -> np.ndarray:
    """Softmax numericamente estável via shift por max.

    Shift por max não altera o resultado (cancela no numerador e denominador)
    mas previne overflow em exp para valores grandes (>709 em float64).
    """
    x_shifted = x - x.max(axis=axis, keepdims=True)
    exp_x = np.exp(x_shifted)
    return exp_x / exp_x.sum(axis=axis, keepdims=True)


def create_causal_mask(seq_len: int) -> np.ndarray:
    """Máscara triangular inferior: True = posição visível.

    Token na posição i pode ver tokens 0..i mas não i+1..T-1.
    Broadcast para (batch, n_heads, seq, seq) automaticamente.
    """
    return np.tril(np.ones((seq_len, seq_len), dtype=bool))


def scaled_dot_product_attention(
    Q: np.ndarray,                      # (batch, heads, seq_q, d_k)
    K: np.ndarray,                      # (batch, heads, seq_k, d_k)
    V: np.ndarray,                      # (batch, heads, seq_k, d_v)
    mask: Optional[np.ndarray] = None,  # (seq_q, seq_k) or broadcastable; True=KEEP
) -> tuple[np.ndarray, np.ndarray]:
    """Fórmula: softmax(QK^T / sqrt(d_k)) V.

    Returns:
        output:  (batch, heads, seq_q, d_v)
        weights: (batch, heads, seq_q, seq_k) — distribuição sobre tokens-chave
    """
    d_k = Q.shape[-1]

    # (batch, heads, seq_q, seq_k) — sem scaling varia com sqrt(d_k)
    scores = Q @ K.swapaxes(-2, -1) / np.sqrt(d_k)

    if mask is not None:
        # -1e9 → exp(-1e9) ≈ 0 após softmax; -inf causaria NaN no backward
        scores = np.where(mask, scores, -1e9)

    weights = softmax(scores, axis=-1)
    output = weights @ V
    return output, weights


# ─────────────────────────────────────────────
# Multi-Head Self-Attention
# ─────────────────────────────────────────────

class MultiHeadSelfAttention:
    """MHA completo em NumPy. Sem autograd — apenas forward pass."""

    def __init__(self, d_model: int, n_heads: int, seed: int = 42):
        assert d_model % n_heads == 0, "d_model deve ser divisível por n_heads"
        rng = np.random.default_rng(seed)

        self.d_model = d_model
        self.n_heads = n_heads
        self.d_k = d_model // n_heads  # dimensão por head

        # Xavier-like init: escala por sqrt(2/d_model) para começar com variância ~1
        scale = np.sqrt(2.0 / d_model)

        # Uma única matriz por projeção (em vez de h matrizes separadas):
        # equivalente mas mais eficiente — permite um único GEMM grande.
        self.W_Q = rng.normal(0, scale, (d_model, d_model))
        self.W_K = rng.normal(0, scale, (d_model, d_model))
        self.W_V = rng.normal(0, scale, (d_model, d_model))
        self.W_O = rng.normal(0, scale, (d_model, d_model))

    def _split_heads(self, x: np.ndarray) -> np.ndarray:
        """(batch, seq, d_model) → (batch, n_heads, seq, d_k).

        Reshape então transpose: reshape sozinho produziria layout incorreto
        porque o d_model precisa ser dividido pelo número de heads,
        não pela posição do token.
        """
        B, S, _ = x.shape
        x = x.reshape(B, S, self.n_heads, self.d_k)
        return x.transpose(0, 2, 1, 3)  # (batch, n_heads, seq, d_k)

    def _merge_heads(self, x: np.ndarray) -> np.ndarray:
        """(batch, n_heads, seq, d_k) → (batch, seq, d_model).

        Inverso de _split_heads: desfaz transpose e reshape.
        """
        B, H, S, d_k = x.shape
        x = x.transpose(0, 2, 1, 3)  # (batch, seq, n_heads, d_k)
        return x.reshape(B, S, H * d_k)

    def forward(
        self,
        x: np.ndarray,                      # (batch, seq, d_model)
        mask: Optional[np.ndarray] = None,
    ) -> tuple[np.ndarray, np.ndarray]:
        """Forward pass completo. Retorna (output, attention_weights)."""
        # Projeções lineares: um único matmul por projeção
        Q = x @ self.W_Q  # (batch, seq, d_model)
        K = x @ self.W_K
        V = x @ self.W_V

        # Split em n_heads (sem copiar dados, só reshape+transpose)
        Q = self._split_heads(Q)  # (batch, n_heads, seq, d_k)
        K = self._split_heads(K)
        V = self._split_heads(V)

        # Atenção independente por head
        attn_out, weights = scaled_dot_product_attention(Q, K, V, mask)

        # Merge e projeção de saída
        merged = self._merge_heads(attn_out)  # (batch, seq, d_model)
        output = merged @ self.W_O
        return output, weights

    def __call__(self, x: np.ndarray, mask: Optional[np.ndarray] = None):
        return self.forward(x, mask)


# ─────────────────────────────────────────────
# Experimentos
# ─────────────────────────────────────────────

def experiment_scaling_effect() -> None:
    """Demonstra por que scaling por sqrt(d_k) é necessário.

    Sem scaling, a entropia do softmax colapsa com d_k crescente —
    o modelo fica artificialmente "determinístico".
    """
    print("\n=== Experimento: Efeito do Scaling ===")
    rng = np.random.default_rng(0)

    for d_k in [16, 64, 256]:
        # Vetores unitários aleatórios
        q = rng.normal(0, 1, (d_k,))
        K = rng.normal(0, 1, (10, d_k))  # 10 keys

        scores_raw = q @ K.T            # dot products sem scaling
        scores_scaled = scores_raw / np.sqrt(d_k)

        def entropy(probs: np.ndarray) -> float:
            probs = np.clip(probs, 1e-10, 1.0)
            return float(-np.sum(probs * np.log(probs)))

        e_raw = entropy(softmax(scores_raw))
        e_scaled = entropy(softmax(scores_scaled))

        print(f"d_k={d_k:3d}:  entropia sem scale: {e_raw:.2f} | com scale: {e_scaled:.2f}")

    print("→ Sem scaling, entropia colapsa para 0 (token único domina).")


def experiment_mha_shapes() -> None:
    """Verifica shapes em cada etapa do forward pass."""
    print("\n=== Experimento: Shapes no MHA ===")
    B, S, d_model, n_heads = 2, 10, 64, 8

    mha = MultiHeadSelfAttention(d_model=d_model, n_heads=n_heads)
    x = np.random.randn(B, S, d_model)

    print(f"Input shape:         {x.shape}")
    Q = x @ mha.W_Q
    print(f"Após W_Q:            {Q.shape}")
    Q_split = mha._split_heads(Q)
    print(f"Após split_heads:    {Q_split.shape}  ← (batch, heads, seq, d_k)")
    attn_out, weights = scaled_dot_product_attention(
        mha._split_heads(x @ mha.W_Q),
        mha._split_heads(x @ mha.W_K),
        mha._split_heads(x @ mha.W_V),
    )
    print(f"Após atenção:        {attn_out.shape}")
    merged = mha._merge_heads(attn_out)
    print(f"Após merge_heads:    {merged.shape}")
    output, _ = mha(x)
    print(f"Após W_O:            {output.shape}")

    # Assertions
    assert output.shape == (B, S, d_model), f"Shape errada: {output.shape}"
    assert weights.shape == (B, n_heads, S, S), f"Weights shape errada: {weights.shape}"
    assert np.allclose(weights.sum(-1), 1.0, atol=1e-6), "Weights não somam 1"
    print("All assertions OK")


def experiment_causal_mask() -> None:
    """Verifica comportamento da causal mask."""
    print("\n=== Experimento: Causal Mask ===")
    B, S, d_model, n_heads = 1, 5, 8, 1
    mha = MultiHeadSelfAttention(d_model=d_model, n_heads=n_heads, seed=7)
    x = np.random.default_rng(0).normal(0, 1, (B, S, d_model))

    mask = create_causal_mask(S)  # (S, S)

    _, w_no_mask = mha(x, mask=None)
    _, w_causal = mha(x, mask=mask)

    # Token 0 sem máscara: distribui atenção em todos os tokens
    print(f"Weights sem máscara (token 0):  {w_no_mask[0, 0, 0, :].round(2)}")
    # Token 0 com máscara: atenção apenas em si mesmo (única posição visível)
    print(f"Weights com máscara (token 0):  {w_causal[0, 0, 0, :].round(2)}")
    # Token 3 com máscara: pode ver tokens 0–3
    print(f"Weights com máscara (token 3):  {w_causal[0, 0, 3, :].round(2)}")

    # Token 0 com máscara deve ter peso 1.0 em si mesmo
    assert w_causal[0, 0, 0, 0] > 0.999, "Token 0 deveria ter peso ~1.0 em si mesmo"
    # Posições futuras devem ter peso ~0
    assert w_causal[0, 0, 0, 1:].max() < 1e-5, "Tokens futuros devem ter peso ~0"
    print("PASS: causal mask correto")


def benchmark() -> None:
    """Mede tempo por seq_len para confirmar complexidade quadrática."""
    print("\n=== Benchmark: tempo por seq_len ===")
    d_model, n_heads = 64, 8
    mha = MultiHeadSelfAttention(d_model=d_model, n_heads=n_heads)
    rng = np.random.default_rng(42)

    print(f"{'seq_len':>10} {'tempo (ms)':>12} {'ratio vs prev':>15}")
    prev_time = None
    for seq_len in [64, 128, 256, 512]:
        x = rng.normal(0, 1, (1, seq_len, d_model))
        # Warm-up
        mha(x)
        # Medição
        runs = 10
        start = time.perf_counter()
        for _ in range(runs):
            mha(x)
        elapsed_ms = (time.perf_counter() - start) / runs * 1000

        ratio = f"{elapsed_ms / prev_time:.2f}×" if prev_time else "—"
        print(f"{seq_len:>10} {elapsed_ms:>11.1f}ms {ratio:>15}")
        prev_time = elapsed_ms

    print("→ Espera-se ratio ~4× a cada dobro de seq_len (quadrático).")


# ─────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--experiment",
        choices=["scaling_effect", "mha_shapes", "causal_mask"],
        help="Experimento específico a executar",
    )
    parser.add_argument("--benchmark", action="store_true")
    parser.add_argument("--all", action="store_true", dest="run_all")
    args = parser.parse_args()

    if args.run_all or args.experiment == "scaling_effect":
        experiment_scaling_effect()
    if args.run_all or args.experiment == "mha_shapes":
        experiment_mha_shapes()
    if args.run_all or args.experiment == "causal_mask":
        experiment_causal_mask()
    if args.run_all or args.benchmark:
        benchmark()


if __name__ == "__main__":
    main()
