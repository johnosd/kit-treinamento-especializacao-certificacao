# MBA AutoDirigido

Clones autodidatas de especializações de pós-graduação top-tier (Harvard, MIT, Stanford, CMU, Berkeley …) gerados por uma suite de prompts.

Dado um par `(curso, instituição)`, o fluxo produz um kit de estudos com profundidade equivalente à pós-graduação original, baseado em fontes oficiais, com gate de fidelidade explícito.

---

## Estrutura do repositório

```
MBA AutoDirigido/
├── README.md
├── docs/                                      Documentos pessoais de referência
│   ├── Apresentacao.md
│   └── Bibliografia.md
├── templates/                                 Prompts (suite de personagens)
│   ├── especializacao/
│   │   ├── 01-prompt-curriculum.md            Pesquisador Acadêmico
│   │   ├── 02-curriculum-schema.md            Schema canônico de curriculum.md
│   │   ├── 03-kit-rules.md                    Regras pedagógicas transversais
│   │   ├── 04-kit-output-schema.md            Estrutura de arquivos do kit
│   │   ├── 05-kit-workflow.md                 Workflow de execução
│   │   ├── 06-coordenador-curso.md            Coordenador
│   │   ├── 07-professor-disciplina.md         Professor da Disciplina
│   │   ├── 08-engenheiro-labs.md              Engenheiro de Laboratório
│   │   ├── 09-banca-avaliacao.md              Banca Examinadora
│   │   └── 10-revisor-fidelidade.md           Revisor de Fidelidade
│   └── certificacoes/
│       └── template.md                        Fluxo paralelo para certificações de vendor
├── exemplos/                                  Curriculums já preenchidos como referência
│   ├── curriculum-cmu.md
│   └── curriculum-fia.md
└── cursos/                                    Kits gerados
    ├── cmu-generative-ai-llms/
    └── fia-labdata-analytics-ia-data-science/
```

---

## Fluxo em 3 fases

### Fase 1 — Pesquisa

O **Pesquisador Acadêmico** ([01-prompt-curriculum.md](templates/especializacao/01-prompt-curriculum.md)) recebe `(curso, instituição)`, busca em fontes oficiais (WebSearch + WebFetch nativos), extrai grade, ementas, professores e publicações, e grava em `cursos/<slug>/02-curriculum.md` conforme [02-curriculum-schema.md](templates/especializacao/02-curriculum-schema.md).

Para instituições top-tier, exige ≥2 fontes oficiais corroborantes (Source Diversity Rule).

### Fase 2 — Coordenação

O **Coordenador de Curso** ([06-coordenador-curso.md](templates/especializacao/06-coordenador-curso.md)) extrai a filosofia pedagógica do programa (engineering-heavy, research-heavy, systems-heavy, …) e produz a base do kit: `01-README.md`, `03-study-plan.md`, `04-weekly-roadmap.md`, `05-glossary.md`, `06-concept-map.md` e a **matriz de cobertura** (`coverage-matrix.md`).

A matriz mapeia explicitamente cada semana do syllabus original para semana(s) do kit — é o gate de fidelidade da Fase 3.

### Fase 3 — Geração incremental por semana

Para cada semana `NN`, em loop:

1. **Professor da Disciplina** ([07](templates/especializacao/07-professor-disciplina.md)) — `01-theory.md` + `02-readings.md`, adotando voz do professor real quando identificável.
2. **Engenheiro de Labs** ([08](templates/especializacao/08-engenheiro-labs.md)) — `03-lab-guided.md` + `04-lab-speedrun.md` + `code/` com profiling e métrica-alvo.
3. **Banca Examinadora** ([09](templates/especializacao/09-banca-avaliacao.md)) — `05-exercises.md` + `06-mini-project.md` + `07-assessment.md` (com rubrica + model answers) + `08-flashcards.md`.
4. **Revisor de Fidelidade** ([10](templates/especializacao/10-revisor-fidelidade.md)) — `09-coverage.md` da semana e atualização da matriz; se ⚠ ou ✗, retorna para a persona apropriada.

Detalhes do fluxo em [05-kit-workflow.md](templates/especializacao/05-kit-workflow.md).

---

## Regras críticas que garantem o "clone"

Definidas em [03-kit-rules.md](templates/especializacao/03-kit-rules.md):

1. **Source Diversity Rule** — top-tier exige ≥2 fontes oficiais.
2. **Professor Extraction Rule** — publicações dos profs reais viram leituras primárias.
3. **Gap Supplementation Rule** — quando o syllabus oficial omite, suplementar com curso-irmão top-tier, sempre declarando a fonte.
4. **Philosophy Preservation Rule** — filosofia do programa prevalece sobre preferências do aluno (o objetivo é clonar a especialização, não personalizar).

---

## Como rodar um novo kit

```
Crie o curriculum.md para o curso "<NOME_DO_CURSO>" da instituição "<NOME_DA_INSTITUICAO>"
usando templates/especializacao/01-prompt-curriculum.md.
```

Revise o `02-curriculum.md` gerado. Em seguida:

```
Gere a base do kit em cursos/<slug>/ usando 06-coordenador-curso.md
a partir de cursos/<slug>/02-curriculum.md.
```

Revise a filosofia extraída e a matriz de cobertura. Em seguida, semana a semana:

```
Gere a semana 01 do kit cursos/<slug>/ seguindo 05-kit-workflow.md Fase 3.
```

Cada semana só fecha quando o Revisor de Fidelidade aprova (✓ ou + com suplementação declarada).

---

## Kits existentes

| Slug | Programa de referência | Status |
|---|---|---|
| [cmu-generative-ai-llms](cursos/cmu-generative-ai-llms/01-README.md) | CMU — Generative AI & Large Language Models | Base + semana 01 (geração antiga, pré-suite) |
| [fia-labdata-analytics-ia-data-science](cursos/fia-labdata-analytics-ia-data-science/01-README.md) | FIA / Labdata — Analytics e IA — Data Science | Base + semana 01 (geração antiga, pré-suite) |

Esses kits foram gerados antes da reestruturação para suite de personagens — servem como base histórica e referência de output. Kits novos seguirão o fluxo completo de 6 personagens.

---

## Fluxo paralelo: certificações

O subprojeto [templates/certificacoes/](templates/certificacoes/template.md) cobre o caso de certificações de vendor (AZ-204, AWS-SAA, CKA, GH-200, TF-Associate, …). É um fluxo separado, com escopo e regras próprias, mas mora no mesmo repo.
