"""Compara MultiHeadSelfAttention NumPy com torch.nn.MultiheadAttention.

Executar após: 02_self_attention_numpy.py
Output esperado: 'PASS: outputs são numericamente equivalentes (tol=1e-5)'

A equivalência numérica entre implementações independentes é o padrão de
validação de research engineers — se diferem, há um bug em alguma das duas.
"""

import numpy as np
import torch
import torch.nn as nn

from _02_self_attention_numpy import MultiHeadSelfAttention


def copy_weights_to_pytorch(
    mha_np: MultiHeadSelfAttention,
    mha_pt: nn.MultiheadAttention,
) -> None:
    """Copia pesos NumPy → PyTorch com layout correto.

    PyTorch armazena projeções Q, K, V como uma única matriz 'in_proj_weight'
    no formato [W_Q; W_K; W_V] (concatenação vertical, shape 3*d_model × d_model).
    Precisamos respeitar esse layout ao copiar.
    """
    d = mha_np.d_model

    # Construir in_proj_weight como [W_Q; W_K; W_V]
    # Cada W é (d_model, d_model) em NumPy; PyTorch espera transposto: (d_model, d_model) ainda
    # (PyTorch usa convenção weight @ input.T internamente, mas a API aceita (out, in))
    W_Q_t = mha_np.W_Q.T  # (d_model, d_model) → (d_model, d_model) transposto
    W_K_t = mha_np.W_K.T
    W_V_t = mha_np.W_V.T

    in_proj = np.concatenate([W_Q_t, W_K_t, W_V_t], axis=0)  # (3*d_model, d_model)
    out_proj = mha_np.W_O.T  # (d_model, d_model)

    with torch.no_grad():
        mha_pt.in_proj_weight.copy_(torch.from_numpy(in_proj.astype(np.float32)))
        mha_pt.out_proj.weight.copy_(torch.from_numpy(out_proj.astype(np.float32)))


def compare(
    d_model: int = 64,
    n_heads: int = 8,
    batch: int = 2,
    seq_len: int = 10,
    seed: int = 42,
    tol: float = 1e-5,
) -> None:
    rng = np.random.default_rng(seed)
    x_np = rng.normal(0, 1, (batch, seq_len, d_model)).astype(np.float32)
    x_pt = torch.from_numpy(x_np)

    # NumPy MHA
    mha_np = MultiHeadSelfAttention(d_model=d_model, n_heads=n_heads, seed=seed)
    out_np, _ = mha_np(x_np)

    # PyTorch MHA — batch_first=True para mesma convenção (batch, seq, d_model)
    mha_pt = nn.MultiheadAttention(
        embed_dim=d_model,
        num_heads=n_heads,
        bias=False,      # nosso NumPy não tem bias
        batch_first=True,
    )
    copy_weights_to_pytorch(mha_np, mha_pt)

    mha_pt.eval()
    with torch.no_grad():
        out_pt, _ = mha_pt(x_pt, x_pt, x_pt)
    out_pt_np = out_pt.numpy()

    # Diagnóstico
    max_diff = float(np.abs(out_np - out_pt_np).max())
    mean_abs = float(np.abs(out_np - out_pt_np).mean())

    print(f"NumPy output:   shape {out_np.shape}, mean={out_np.mean():.4f}, std={out_np.std():.4f}")
    print(f"PyTorch output: shape {out_pt_np.shape}, mean={out_pt_np.mean():.4f}, std={out_pt_np.std():.4f}")
    print(f"Max absolute difference: {max_diff:.2e}")
    print(f"Mean absolute difference: {mean_abs:.2e}")

    if max_diff < tol:
        print(f"PASS: outputs são numericamente equivalentes (tol={tol})")
    else:
        print(f"FAIL: max_diff={max_diff:.2e} excede tol={tol}")
        print("Debugging hints:")
        print("  1. Verifique a ordem de concatenação: PyTorch usa [W_Q; W_K; W_V]")
        print("  2. Confirme batch_first=True no PyTorch MHA")
        print("  3. Confirme que W transposto é usado corretamente (PyTorch: weight @ x.T)")


if __name__ == "__main__":
    compare()
