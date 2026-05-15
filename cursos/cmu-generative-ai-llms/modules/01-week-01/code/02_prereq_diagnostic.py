"""Generate a self-scored prerequisite diagnostic report.

This script intentionally does not grade your answers. It creates a structured
rubric and asks you to fill scores honestly after answering the questions.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Any


def load_questions(path: Path) -> list[dict[str, Any]]:
    return json.loads(path.read_text(encoding="utf-8"))


def render_report(questions: list[dict[str, Any]]) -> str:
    by_area: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in questions:
        by_area[item["area"]].append(item)

    lines = [
        "# 02 — Prerequisite Diagnostic Report",
        "",
        "Responda cada pergunta antes de preencher o score. Use 0 se não conseguir explicar sem consulta.",
        "",
        "## Summary",
        "",
        "| Área | Score obtido | Score máximo | Status |",
        "|---|---:|---:|---|",
    ]
    for area, items in by_area.items():
        max_score = sum(int(item["max_score"]) for item in items)
        lines.append(f"| {area} | TODO | {max_score} | TODO |")

    lines.extend(["", "## Questions", ""])
    for area, items in by_area.items():
        lines.append(f"### {area}")
        lines.append("")
        for idx, item in enumerate(items, 1):
            lines.append(f"{idx}. {item['question']}")
            lines.append(f"   - Max score: {item['max_score']}")
            lines.append("   - Your answer:")
            lines.append("   - Score:")
            lines.append("   - Remediation:")
            lines.append("")

    lines.extend(
        [
            "## Go/No-Go",
            "",
            "- Go to Week 02?",
            "- Blocking gaps:",
            "- Remediation tasks:",
            "- Date to re-check:",
            "",
        ]
    )
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("questions", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    questions = load_questions(args.questions)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(render_report(questions), encoding="utf-8")
    print(f"Diagnostic report written to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
