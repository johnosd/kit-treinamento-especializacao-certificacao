"""Environment check for Week 01.

This script uses only the Python standard library. Optional packages are
reported when installed, but they are not required to complete Week 01.
"""

from __future__ import annotations

import importlib.util
import platform
import sys


OPTIONAL_PACKAGES = [
    "pandas",
    "numpy",
    "sklearn",
    "matplotlib",
    "jupyter",
    "torch",
    "tensorflow",
]


def package_status(name: str) -> str:
    spec = importlib.util.find_spec(name)
    if spec is None:
        return "missing"
    return "installed"


def main() -> int:
    print(f"Python: {sys.version.split()[0]}")
    print(f"Executable: {sys.executable}")
    print(f"Platform: {platform.platform()}")
    print("\nOptional packages:")
    for package in OPTIONAL_PACKAGES:
        print(f"  {package}: {package_status(package)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
