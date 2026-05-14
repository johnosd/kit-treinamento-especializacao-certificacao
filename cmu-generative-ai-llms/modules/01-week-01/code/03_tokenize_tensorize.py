"""Minimal tokenization and tensorization demo for Week 01.

The implementation uses only the standard library so the core mechanics are
visible before relying on production tokenizers.
"""

from __future__ import annotations

import argparse
import math
import re
from collections import Counter
from pathlib import Path


SPECIAL_TOKENS = ["<pad>", "<unk>", "<bos>", "<eos>"]
TOKEN_RE = re.compile(r"[A-Za-z0-9]+|[^\w\s]", re.UNICODE)


def tokenize(text: str) -> list[str]:
    return TOKEN_RE.findall(text.lower())


def build_vocab(tokens: list[str]) -> dict[str, int]:
    counts = Counter(tokens)
    vocab = {token: idx for idx, token in enumerate(SPECIAL_TOKENS)}
    for token, _ in counts.most_common():
        if token not in vocab:
            vocab[token] = len(vocab)
    return vocab


def encode(tokens: list[str], vocab: dict[str, int]) -> list[int]:
    return [vocab.get(token, vocab["<unk>"]) for token in tokens]


def make_examples(ids: list[int], context_size: int) -> list[tuple[list[int], int]]:
    examples: list[tuple[list[int], int]] = []
    for pos in range(1, len(ids)):
        start = max(0, pos - context_size)
        context = ids[start:pos]
        if len(context) < context_size:
            context = [0] * (context_size - len(context)) + context
        examples.append((context, ids[pos]))
    return examples


def softmax(logits: list[float]) -> list[float]:
    max_logit = max(logits)
    exps = [math.exp(value - max_logit) for value in logits]
    denom = sum(exps)
    return [value / denom for value in exps]


def cross_entropy(probs: list[float], target_index: int) -> float:
    return -math.log(max(probs[target_index], 1e-12))


def render_report(text: str, context_size: int) -> str:
    raw_tokens = tokenize(text)
    sequence = ["<bos>"] + raw_tokens + ["<eos>"]
    vocab = build_vocab(sequence)
    ids = encode(sequence, vocab)
    examples = make_examples(ids, context_size)

    demo_logits = [2.0, 1.0, 0.1]
    demo_probs = softmax(demo_logits)
    demo_ce = cross_entropy(demo_probs, 0)
    demo_ppl = math.exp(demo_ce)

    inverse_vocab = {idx: token for token, idx in vocab.items()}
    sample_examples = examples[: min(8, len(examples))]

    lines = [
        "# 03 — Tokenization and Tensorization Report",
        "",
        "## Corpus Summary",
        "",
        f"- Characters: {len(text)}",
        f"- Tokens including special tokens: {len(sequence)}",
        f"- Vocabulary size: {len(vocab)}",
        f"- Context size: {context_size}",
        "",
        "## Vocabulary",
        "",
    ]
    for token, idx in sorted(vocab.items(), key=lambda item: item[1]):
        lines.append(f"- `{idx}` -> `{token}`")

    lines.extend(["", "## Encoded Sequence", "", f"```txt\n{ids}\n```", ""])
    lines.extend(["## Context / Target Examples", ""])
    for context, target in sample_examples:
        context_tokens = [inverse_vocab[item] for item in context]
        target_token = inverse_vocab[target]
        lines.append(f"- context IDs `{context}` -> target `{target}` (`{target_token}`)")
        lines.append(f"  - context tokens: `{context_tokens}`")

    lines.extend(
        [
            "",
            "## Softmax / Cross-Entropy / Perplexity Demo",
            "",
            f"- Demo logits: `{demo_logits}`",
            f"- Softmax probabilities: `{[round(value, 6) for value in demo_probs]}`",
            f"- Target index: `0`",
            f"- Cross-entropy: `{demo_ce:.6f}`",
            f"- Perplexity: `{demo_ppl:.6f}`",
            "",
            "## Interpretation",
            "",
            "- This tokenizer is intentionally simple and not production-grade.",
            "- The context/target pairs show the next-token prediction objective.",
            "- Perplexity here is a numerical demonstration, not a model evaluation.",
            "",
        ]
    )
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("corpus", type=Path)
    parser.add_argument("--context-size", type=int, default=4)
    parser.add_argument("--out", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    text = args.corpus.read_text(encoding="utf-8")
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(render_report(text, args.context_size), encoding="utf-8")
    print(f"Tokenization report written to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
