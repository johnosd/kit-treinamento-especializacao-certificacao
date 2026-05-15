"""Week 01 environment check."""

from __future__ import annotations

import importlib
import importlib.util
import platform
import sys


PACKAGES = ["torch", "transformers", "tokenizers", "numpy"]


def package_version(name: str) -> str:
    if importlib.util.find_spec(name) is None:
        return "missing"
    module = importlib.import_module(name)
    return getattr(module, "__version__", "installed")


def cuda_status() -> str:
    if importlib.util.find_spec("torch") is None:
        return "unknown (torch missing)"
    import torch

    if not torch.cuda.is_available():
        return "no"
    return f"yes ({torch.cuda.device_count()} device(s): {torch.cuda.get_device_name(0)})"


def main() -> int:
    print(f"Python: {sys.version.split()[0]}")
    print(f"Executable: {sys.executable}")
    print(f"Platform: {platform.platform()}")
    print("\nOptional packages:")
    for package in PACKAGES:
        print(f"  {package}: {package_version(package)}")
    print(f"\nCUDA available: {cuda_status()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
