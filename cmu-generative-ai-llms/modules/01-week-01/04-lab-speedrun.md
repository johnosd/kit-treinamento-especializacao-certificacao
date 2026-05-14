# 04 — Lab Speedrun

Tempo alvo: 15-25 minutos.

## Comandos

PowerShell:

```powershell
cd cmu-generative-ai-llms\modules\01-week-01\code
python 01_environment_check.py
python 02_prereq_diagnostic.py diagnostic_questions.json --out ..\assets\02-diagnostic-report.md
python 03_tokenize_tensorize.py sample_corpus.txt --out ..\assets\03-tokenization-report.md
```

Linux/macOS:

```bash
cd cmu-generative-ai-llms/modules/01-week-01/code
python 01_environment_check.py
python 02_prereq_diagnostic.py diagnostic_questions.json --out ../assets/02-diagnostic-report.md
python 03_tokenize_tensorize.py sample_corpus.txt --out ../assets/03-tokenization-report.md
```

## Checkpoints

| Checkpoint | Esperado |
|---|---|
| Ambiente | Python e pacotes opcionais listados |
| Diagnóstico | relatório com score por área |
| Tokenização | vocabulário, token IDs, janelas e targets |
| Perplexity demo | cross-entropy e PPL calculadas |

## Desafio Extra

Troque `sample_corpus.txt` por um texto técnico seu com 10-20 linhas e rode novamente:

```powershell
python 03_tokenize_tensorize.py meu_corpus.txt --context-size 6 --out ..\assets\03-tokenization-report-custom.md
```

Compare:

- tamanho do vocabulário;
- proporção de `<unk>`;
- tamanho médio de sequência;
- exemplos de context/target.
