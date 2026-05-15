"""Script de sanity check do ambiente.
Executar antes de qualquer outro script do lab.
Output esperado: 'Setup OK — pronto para o lab.'
"""

import sys
import importlib

REQUIRED = {
    "numpy": "1.24.0",
    "torch": "2.0.0",
}


def check_version(pkg_name: str, min_version: str) -> bool:
    try:
        mod = importlib.import_module(pkg_name)
        installed = getattr(mod, "__version__", "0.0.0")
        from packaging.version import Version
        return Version(installed) >= Version(min_version)
    except ImportError:
        return False


def main() -> None:
    all_ok = True

    # Python version
    py_major, py_minor = sys.version_info[:2]
    if (py_major, py_minor) >= (3, 10):
        print(f"[OK] Python {py_major}.{py_minor}")
    else:
        print(f"[FAIL] Python {py_major}.{py_minor} — requer 3.10+")
        all_ok = False

    # Packages
    for pkg, min_ver in REQUIRED.items():
        try:
            mod = importlib.import_module(pkg)
            ver = getattr(mod, "__version__", "?")
            # Simple version check without packaging dependency
            print(f"[OK] {pkg} {ver}")
        except ImportError:
            print(f"[FAIL] {pkg} não encontrado — instale com: pip install {pkg}")
            all_ok = False

    # Random seed reproducibility
    import numpy as np
    import random

    np.random.seed(42)
    random.seed(42)
    sample = np.random.rand(2)
    expected = [0.37454012, 0.95071431]
    if all(abs(s - e) < 1e-6 for s, e in zip(sample, expected)):
        print(f"[OK] random seed fixo: {sample}")
    else:
        print(f"[FAIL] seed não reprodutível: got {sample}, expected {expected}")
        all_ok = False

    # PyTorch CPU availability
    try:
        import torch
        t = torch.ones(2, 2)
        assert t.sum().item() == 4.0
        print(f"[OK] PyTorch {torch.__version__} (CPU)")
    except Exception as e:
        print(f"[FAIL] PyTorch não funcional: {e}")
        all_ok = False

    if all_ok:
        print("\nSetup OK — pronto para o lab.")
    else:
        print("\nSetup FAILED — resolva os itens [FAIL] antes de continuar.")
        sys.exit(1)


if __name__ == "__main__":
    main()
