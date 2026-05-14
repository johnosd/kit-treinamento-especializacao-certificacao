"""Validate and render a problem framing specification.

Usage:
    python problem_framing_validator.py problem_spec.json --out ../assets/problem-report.md
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = [
    "problem_name",
    "decision_to_improve",
    "stakeholders",
    "prediction_unit",
    "prediction_horizon",
    "target_definition",
    "data_sources",
    "technical_metrics",
    "business_metrics",
    "baseline",
    "error_costs",
    "risks",
    "go_no_go_criteria",
]

VAGUE_TERMS = {
    "tbd",
    "todo",
    "n/a",
    "na",
    "a definir",
    "melhorar",
    "usar ia",
    "usar inteligência artificial",
}


def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path}: {exc}") from exc


def is_empty(value: Any) -> bool:
    if value is None:
        return True
    if isinstance(value, str):
        return not value.strip()
    if isinstance(value, (list, dict)):
        return len(value) == 0
    return False


def looks_vague(value: Any, *, allow_short_terms: bool = False) -> bool:
    if isinstance(value, str):
        normalized = value.strip().lower()
        if normalized in VAGUE_TERMS:
            return True
        return (not allow_short_terms) and len(normalized) < 8
    if isinstance(value, list):
        return any(looks_vague(item, allow_short_terms=True) for item in value)
    if isinstance(value, dict):
        return any(looks_vague(item, allow_short_terms=True) for item in value.values())
    return False


def validate(spec: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for field in REQUIRED_FIELDS:
        if field not in spec:
            errors.append(f"Missing required field: {field}")
            continue
        if is_empty(spec[field]):
            errors.append(f"Empty required field: {field}")
        elif looks_vague(spec[field]):
            errors.append(f"Field looks vague: {field}")

    if isinstance(spec.get("technical_metrics"), list) and len(spec["technical_metrics"]) < 2:
        errors.append("technical_metrics should include at least 2 metrics")
    if isinstance(spec.get("risks"), list) and len(spec["risks"]) < 5:
        errors.append("risks should include at least 5 explicit risks")
    return errors


def as_bullets(items: Any) -> str:
    if isinstance(items, list):
        return "\n".join(f"- {item}" for item in items)
    if isinstance(items, dict):
        return "\n".join(f"- **{key}:** {value}" for key, value in items.items())
    return f"- {items}"


def render_report(spec: dict[str, Any]) -> str:
    sections = [
        f"# Problem Report — {spec['problem_name']}",
        "## Decision",
        str(spec["decision_to_improve"]),
        "## Stakeholders",
        as_bullets(spec["stakeholders"]),
        "## Prediction / Analysis Unit",
        str(spec["prediction_unit"]),
        "## Horizon",
        str(spec["prediction_horizon"]),
        "## Target Definition",
        str(spec["target_definition"]),
        "## Data Sources",
        as_bullets(spec["data_sources"]),
        "## Technical Metrics",
        as_bullets(spec["technical_metrics"]),
        "## Business Metrics",
        as_bullets(spec["business_metrics"]),
        "## Baseline",
        str(spec["baseline"]),
        "## Error Costs",
        as_bullets(spec["error_costs"]),
        "## Risks",
        as_bullets(spec["risks"]),
        "## Go/No-Go Criteria",
        as_bullets(spec["go_no_go_criteria"]),
    ]
    return "\n\n".join(sections) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("spec", type=Path)
    parser.add_argument("--out", type=Path, default=Path("problem-report.md"))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    spec = load_json(args.spec)
    errors = validate(spec)
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(render_report(spec), encoding="utf-8")
    print("OK: required fields present")
    print(f"Report written to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
