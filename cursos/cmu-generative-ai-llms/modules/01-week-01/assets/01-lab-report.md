# Lab Report — Semana 01: Self-Attention NumPy vs PyTorch

> Preencha após executar todos os scripts do lab guiado.

---

## 1. Resultado da comparação NumPy vs PyTorch

**max_diff obtido:** ___________

**Passou o critério `< 1e-5`?** ☐ Sim  ☐ Não

Se não passou, descreva o bug encontrado e como foi corrigido:

> _________________________________________

---

## 2. Benchmark de performance

| seq_len | Tempo medido (ms) | Ratio vs seq_len anterior |
|---|---|---|
| 64 | | — |
| 128 | | |
| 256 | | |
| 512 | | |

**A relação observada é linear, quadrática ou outra?**

> _________________________________________

**Confirmou crescimento ~4× ao dobrar seq_len?** ☐ Sim  ☐ Não  ☐ Parcialmente

---

## 3. Experimento de scaling

**Entropia do softmax para d_k=64:**
- Sem scaling: ___________
- Com scaling: ___________

**Diferença de ordem de magnitude?** ☐ Sim  ☐ Não

**Em 1–2 frases: o que aconteceria com o treinamento se não houvesse o fator √d_k?**

> _________________________________________

---

## 4. Pergunta de análise

**Se você quiser que o token 5 não veja o token 3, mas possa ver o token 7, como modificaria a máscara?**

> _________________________________________

---

## 5. Observações livres

> Qualquer insight técnico inesperado, dificuldade encontrada, ou extensão explorada.

> _________________________________________
