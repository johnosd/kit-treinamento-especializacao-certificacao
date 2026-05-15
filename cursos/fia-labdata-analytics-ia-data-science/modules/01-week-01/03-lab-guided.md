# Lab Guided — Problem Framing e Setup Técnico

## Objetivo

Você vai criar uma especificação estruturada de problema orientado a dados e validá-la com um script local. O objetivo não é automatizar pensamento crítico, mas impedir que campos essenciais fiquem vagos.

Ao final, você terá:

- ambiente Python verificado;
- um `problem_spec.json` preenchido;
- um relatório Markdown gerado automaticamente;
- uma lista explícita de riscos, métricas, baseline e decisão.

---

## Pré-requisitos

- Python 3.10+.
- Terminal PowerShell, bash ou equivalente.
- Editor de texto.
- Leitura prévia de `theory.md`.

Opcional:

- ambiente virtual com `venv`;
- Git para versionar o exercício.

---

## Estrutura do Lab

```txt
week-01/
├── code/
│   ├── environment_check.py
│   ├── problem_framing_validator.py
│   ├── problem_spec.example.json
│   └── requirements.txt
└── assets/
    └── problem-framing-canvas.md
```

---

## Passo 1 — Verificar Ambiente

No diretório `modules/week-01/code`, execute:

```powershell
python environment_check.py
```

Por quê:

- antes de qualquer análise, você precisa saber qual runtime está usando;
- erros de ambiente confundem diagnóstico de código;
- registrar versões ajuda reprodutibilidade.

Resultado esperado:

```txt
Python: 3.x.x
Platform: ...
Optional packages:
  pandas: ...
  numpy: ...
  sklearn: ...
```

Se algum pacote aparecer como `missing`, isso não bloqueia a Semana 01. O script desta semana usa apenas biblioteca padrão.

---

## Passo 2 — Copiar o Exemplo

Copie o arquivo de exemplo:

```powershell
Copy-Item problem_spec.example.json problem_spec.json
```

No Linux/macOS:

```bash
cp problem_spec.example.json problem_spec.json
```

Por quê:

- o exemplo já demonstra granularidade esperada;
- trabalhar em uma cópia evita sobrescrever o template;
- JSON força estrutura explícita.

---

## Passo 3 — Escolher um Problema Realista

Escolha um problema que você consiga defender com dados. Exemplos:

- priorização de clientes com risco de churn;
- previsão de demanda por produto;
- triagem de tickets de suporte;
- detecção de transações suspeitas;
- classificação de documentos internos;
- assistente RAG para políticas corporativas.

Evite:

- "usar IA para melhorar vendas";
- "fazer um chatbot";
- "prever tudo";
- "automatizar atendimento" sem métrica e usuário.

---

## Passo 4 — Preencher `problem_spec.json`

Campos mínimos:

| Campo | O que deve conter |
|---|---|
| `problem_name` | nome curto e específico |
| `decision_to_improve` | decisão operacional que muda |
| `stakeholders` | usuários e responsáveis |
| `prediction_unit` | entidade prevista: cliente, pedido, documento |
| `prediction_horizon` | janela temporal |
| `target_definition` | rótulo mensurável |
| `data_sources` | fontes e granularidade |
| `technical_metrics` | métricas offline |
| `business_metrics` | métricas de valor |
| `baseline` | regra/modelo simples |
| `error_costs` | custo de falsos positivos/negativos ou erros relevantes |
| `risks` | leakage, viés, privacidade, custo, operação |
| `go_no_go_criteria` | critério objetivo para seguir ou parar |

Por quê:

- cada campo reduz ambiguidade;
- decisões reais exigem unidade, tempo, métrica e custo;
- o baseline disciplina expectativa.

---

## Passo 5 — Validar o Spec

Execute:

```powershell
python problem_framing_validator.py problem_spec.json --out ../assets/problem-report.md
```

Resultado esperado:

```txt
OK: required fields present
Report written to ../assets/problem-report.md
```

Se houver erro, o script listará campos ausentes ou vagos.

---

## Passo 6 — Revisão Crítica Manual

Abra `../assets/problem-report.md` e responda:

1. O problema pode ser resolvido com regra simples?
2. O target seria conhecido no momento correto?
3. A métrica técnica está alinhada à decisão?
4. Existe algum risco de otimizar uma proxy errada?
5. O custo de erro está explicitado?
6. O projeto exige Analytics, ML, DL ou GenAI?

Se você não consegue responder, o problema ainda está mal especificado.

---

## Troubleshooting

| Erro | Causa provável | Correção |
|---|---|---|
| `python` não encontrado | Python não está no PATH | use o launcher `py` no Windows ou instale Python |
| `Invalid JSON` | vírgula sobrando, aspas inválidas ou comentário em JSON | valide o arquivo e remova comentários |
| campo marcado como vago | texto genérico demais | escreva decisão, métrica ou baseline de forma mensurável |
| relatório não é criado | caminho `--out` inválido | crie a pasta ou use caminho relativo simples |
| baseline parece forte demais | isso é bom | mantenha-o; modelo avançado deve justificar complexidade |

---

## Interpretação dos Resultados

O validador não mede qualidade estatística. Ele só impede omissões estruturais. A qualidade real depende da sua capacidade de defender as premissas.

Um spec bom costuma ter:

- decisão operacional explícita;
- horizonte temporal;
- target auditável;
- métrica técnica e de negócio;
- baseline competitivo;
- riscos e critério de parada.

---

## Critério de Conclusão

O lab está concluído quando:

- `environment_check.py` foi executado;
- `problem_spec.json` foi preenchido com um problema próprio;
- `problem-report.md` foi gerado;
- você revisou manualmente os riscos;
- o spec está pronto para evoluir nas próximas semanas para plano de dados e EDA.
