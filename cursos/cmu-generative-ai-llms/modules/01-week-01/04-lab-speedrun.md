# Lab Speedrun — Semana 01

> Versão executiva para re-execução após ter concluído o lab guiado.

---

## Comandos

```bash
cd cursos/cmu-generative-ai-llms/modules/01-week-01/code
pip install -r requirements.txt

python 01_environment_check.py
python 02_self_attention_numpy.py --all
python 03_compare_attention.py
```

---

## Checkpoints

| Etapa | Tempo esperado | Output esperado |
|---|---|---|
| `01_environment_check.py` | < 5s | `Setup OK — pronto para o lab.` |
| `02_self_attention_numpy.py --experiment scaling_effect` | < 2s | Tabela de entropia com e sem scaling |
| `02_self_attention_numpy.py --experiment mha_shapes` | < 2s | `All assertions OK` |
| `02_self_attention_numpy.py --experiment causal_mask` | < 2s | `PASS: causal mask correto` |
| `02_self_attention_numpy.py --benchmark` | < 30s | Tabela de tempo por seq_len |
| `03_compare_attention.py` | < 5s | `PASS: outputs são numericamente equivalentes` |

---

## Critérios de pass

- ✅ `max_diff < 1e-5` na comparação NumPy vs PyTorch.
- ✅ `weights.sum(-1)` dentro de `1e-6` de 1.0 para todas as posições.
- ✅ Tempo ~4× maior ao dobrar seq_len (confirma quadratic scaling).
- ✅ `assets/01-lab-report.md` preenchido com valores medidos.
- ✅ Nenhum `nan` ou `inf` em qualquer output.
