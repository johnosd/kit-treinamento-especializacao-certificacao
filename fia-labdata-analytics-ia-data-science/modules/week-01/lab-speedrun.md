# Lab Speedrun — Week 01

Tempo alvo: 15-20 minutos.

## Comandos

```powershell
cd fia-labdata-analytics-ia-data-science\modules\week-01\code
python environment_check.py
Copy-Item problem_spec.example.json problem_spec.json
python problem_framing_validator.py problem_spec.json --out ..\assets\problem-report.md
```

Linux/macOS:

```bash
cd fia-labdata-analytics-ia-data-science/modules/week-01/code
python environment_check.py
cp problem_spec.example.json problem_spec.json
python problem_framing_validator.py problem_spec.json --out ../assets/problem-report.md
```

## Checkpoints

| Checkpoint | Esperado |
|---|---|
| Ambiente | Python e plataforma impressos |
| Spec | `problem_spec.json` existe |
| Validação | `OK: required fields present` |
| Relatório | `assets/problem-report.md` criado |

## Desafio Extra

Troque o exemplo de churn por um problema próprio e rode novamente o validador. O spec só conta se tiver:

- decisão operacional;
- target com janela temporal;
- pelo menos 2 métricas técnicas;
- pelo menos 1 métrica de negócio;
- baseline;
- 5 riscos.

## Troubleshooting Rápido

| Erro | Fix |
|---|---|
| `python` não encontrado | tente `py` no Windows |
| JSON inválido | remova comentários e vírgulas finais |
| campo ausente | copie a chave do exemplo |
| campo vago | substitua texto genérico por critério mensurável |
| saída não criada | confira o caminho de `--out` |
