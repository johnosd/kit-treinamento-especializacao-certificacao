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
│   │   ├── 10-revisor-fidelidade.md           Revisor de Fidelidade
│   │   └── 11-tutor-onboarding.md             Tutor de Onboarding (Fase 2.5)
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

## Fluxo em 4 fases

### Fase 1 — Pesquisa

O **Pesquisador Acadêmico** ([01-prompt-curriculum.md](templates/especializacao/01-prompt-curriculum.md)) recebe `(curso, instituição)`, busca em fontes oficiais (WebSearch + WebFetch nativos), extrai grade, ementas, professores e publicações, e grava em `cursos/<slug>/02-curriculum.md` conforme [02-curriculum-schema.md](templates/especializacao/02-curriculum-schema.md).

Para instituições top-tier, exige ≥2 fontes oficiais corroborantes (Source Diversity Rule).

### Fase 2 — Coordenação

O **Coordenador de Curso** ([06-coordenador-curso.md](templates/especializacao/06-coordenador-curso.md)) extrai a filosofia pedagógica do programa (engineering-heavy, research-heavy, systems-heavy, …) e produz a base do kit: `01-README.md`, `03-study-plan.md`, `04-weekly-roadmap.md`, `05-glossary.md`, `06-concept-map.md` e a **matriz de cobertura** (`coverage-matrix.md`).

A matriz mapeia explicitamente cada semana do syllabus original para semana(s) do kit — é o gate de fidelidade da Fase 3.

### Fase 2.5 — Onboarding & Nivelamento

O **Tutor de Onboarding** ([11-tutor-onboarding.md](templates/especializacao/11-tutor-onboarding.md)) conduz uma entrevista diagnóstica estruturada (matemática, programação, CS fundamentals, domínio) calibrada pelos pré-requisitos do programa. Identifica gaps e — quando há — gera **pré-semanas de nivelamento** em `modules/00-prereq-01/`, `00-prereq-02/`, …, cada uma mapeando para a semana real onde o conhecimento será exigido pela primeira vez.

Quando o aluno tem todos os pré-requisitos sólidos, pula direto para Fase 3. Sem essa fase, o aluno tropeça em derivações de $\sqrt{d_k}$ na semana 01 sem álgebra linear fresca.

### Fase 3 — Geração incremental por semana

Para cada semana `NN`, em loop:

1. **Professor da Disciplina** ([07](templates/especializacao/07-professor-disciplina.md)) — `01-theory.md` (curto, aponta capítulos de livro) + `02-readings.md`, adotando voz do professor real quando identificável.
2. **Engenheiro de Labs** ([08](templates/especializacao/08-engenheiro-labs.md)) — `03-lab-guided.ipynb` (FIA-style: markdown → código → interpretação) + `04-lab-speedrun.md` + `code/` com profiling e métrica-alvo.
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
5. **Theory-as-pointers** — Professor não reescreve livro canônico; aponta capítulo/seção/páginas e escreve resumo curto (300–600 palavras).
6. **Notebook-first practice** — labs são Jupyter notebooks (`.ipynb`) executáveis no formato FIA-style (markdown ↔ código ↔ interpretação), não Markdown narrativo.

---

## Como usar — guia completo

### Pré-requisitos do ambiente

- **Claude Code** (ou outro cliente Claude com `WebSearch` + `WebFetch`) aberto na raiz deste repo.
- **Python 3.10+** com `jupyter` para abrir os `03-lab-guided.ipynb` gerados.
- **Git** (cada kit gerado é commitado em uma branch própria — sugestão, não obrigatório).

### Convenção de slug

Toda interação a seguir usa um `<slug>` que identifica o curso. Formato: `<instituicao-curta>-<curso-curto>`, kebab-case.

Exemplos:
- `cmu-generative-ai-llms`
- `harvard-cs109-data-science`
- `mit-6s191-deep-learning`
- `stanford-cs324-llms`

Use o mesmo slug em todos os comandos de um curso.

---

### Passo 1 — Pesquisa: gerar `02-curriculum.md`

Em uma sessão limpa do Claude Code (raiz do repo), prompte:

> Use **templates/especializacao/01-prompt-curriculum.md**. Pesquise e gere o `02-curriculum.md` para o curso **"<NOME_DO_CURSO>"** da instituição **"<NOME_DA_INSTITUICAO>"**. Salve em `cursos/<slug>/02-curriculum.md`.

**Exemplo concreto**:

> Use templates/especializacao/01-prompt-curriculum.md. Pesquise e gere o `02-curriculum.md` para o curso "CS109: Introduction to Data Science" da instituição "Harvard University". Salve em `cursos/harvard-cs109-data-science/02-curriculum.md`.

**Reviewing checklist** antes de seguir:

- [ ] Seção `## Fontes Consultadas` lista ≥2 URLs oficiais (se top-tier).
- [ ] Seção `# Professores e Publicações Relevantes` tem ao menos 1 professor identificado com publicações.
- [ ] Seção `# Cursos-Irmãos Top-Tier Identificados` tem ≥2 cursos.
- [ ] Gaps de informação marcados como `Não informado publicamente` — não inventados.
- [ ] Seção `# Filosofia Pedagógica Extraída` está **vazia** (Coordenador preenche no próximo passo).

Se algo está faltando: peça correções específicas antes de seguir. O `02-curriculum.md` é a fonte da verdade do clone.

---

### Passo 2 — Coordenação: base do kit + filosofia + matriz

> Use **templates/especializacao/06-coordenador-curso.md** com input `cursos/<slug>/02-curriculum.md`. Gere a base do kit: `01-README.md`, `03-study-plan.md`, `04-weekly-roadmap.md`, `05-glossary.md`, `06-concept-map.md`, `coverage-matrix.md`. Atualize a seção `# Filosofia Pedagógica Extraída` em `02-curriculum.md`.

**Reviewing checklist**:

- [ ] `01-README.md` contém a filosofia em ≤ 200 palavras **com evidências citadas** (não genérica).
- [ ] `04-weekly-roadmap.md` mapeia toda semana do syllabus original para semana(s) do kit (coluna "Mapeia syllabus original").
- [ ] `coverage-matrix.md` tem 1 linha por semana, todas no estado `⏳ pendente`.
- [ ] `05-glossary.md` tem ≥ 30 termos para programas ≥ 24 semanas.
- [ ] `06-concept-map.md` tem ≥ 3 diagramas Mermaid.

**Sanity check da filosofia**: ela bate com o que você sabe do programa? Se o curso é claramente engineering-heavy mas a filosofia extraída diz "research-heavy", há erro de extração — peça revisão antes de seguir.

---

### Passo 3 — Onboarding: diagnóstico + nivelamento

Esta fase **não pode** ser pulada. É o que evita o aluno tropeçar em derivações sem base.

> Use **templates/especializacao/11-tutor-onboarding.md** em `cursos/<slug>/`. Conduza o diagnóstico interativo comigo.

O Tutor vai conduzir uma entrevista por categoria (matemática, programação, CS, domínio) com perguntas estruturadas. Responda honestamente — auto-declaração inflada gera gaps mascarados.

Ao final, ele gera:

- `cursos/<slug>/00-onboarding/diagnostic.md` (transcript + diagnóstico).
- `cursos/<slug>/00-onboarding/leveling-plan.md` (plano).
- (Se há gaps críticos) `cursos/<slug>/modules/00-prereq-01/`, `00-prereq-02/`, … — pré-semanas com scaffolding pesado.

**Reviewing checklist**:

- [ ] Cada pré-semana mapeia para uma semana real específica (não é curso paralelo aleatório).
- [ ] Theory das pré-semanas aponta capítulos de livro de base (Strang para álgebra linear; Murphy/Bishop para probabilidade).
- [ ] Lab é `.ipynb` executável.

**Se o diagnóstico não identifica gap crítico**: o `leveling-plan.md` registra "nenhum gap crítico identificado" — pode pular direto para Passo 4.

---

### Passo 4 — Gerar semana N (loop)

Para cada semana real, do `01` ao último:

> Gere a semana **NN** do kit `cursos/<slug>/` seguindo `05-kit-workflow.md` Fase 3.

Internamente roda Professor → Eng-Labs → Banca → Revisor de Fidelidade em sequência:

- `01-theory.md` — resumo curto + capítulos de livro (Theory-as-pointers).
- `02-readings.md` — papers/livros/docs com perguntas guia.
- `03-lab-guided.ipynb` — notebook FIA-style (markdown → código → interpretação).
- `04-lab-speedrun.md` — cola de comandos.
- `05-exercises.md`, `06-mini-project.md`, `07-assessment.md` (com rubrica + model answers), `08-flashcards.md`.
- `09-coverage.md` — audit do Revisor.

**Reviewing checklist por semana**:

- [ ] `01-theory.md`: respeita cap (300–600 palavras) **OU** declara `> Sem livro canônico identificado` no topo.
- [ ] Bloco `## Leituras canônicas (capítulos)` aponta páginas/seções específicas (não só título).
- [ ] `03-lab-guided.ipynb` abre no Jupyter, executa do início ao fim sem erro, **outputs preservados**.
- [ ] `07-assessment.md`: toda questão tem rubrica + model answer; total de pesos = 100.
- [ ] `09-coverage.md`: nenhum `✗`; todos `⚠` justificados ou suplementados com fonte declarada.
- [ ] `coverage-matrix.md`: linha da semana N atualizada de `⏳` para `✓` / `+`.

**Não avance para NN+1** se há `✗` em aberto. `✗` significa tópico do syllabus original sem cobertura — falha do clone.

---

### Auditoria avulsa

Para revalidar uma semana antiga após mudança no `02-curriculum.md`:

> Audite `cursos/<slug>/modules/NN-week-NN/` usando **templates/especializacao/10-revisor-fidelidade.md`**.

---

### Como retomar uma sessão antiga

O estado vive no próprio repo — não há banco de estado externo. Para retomar:

1. Abra Claude Code na raiz do repo.
2. Leia `cursos/<slug>/coverage-matrix.md` para identificar a próxima semana pendente.
3. Prompte: `Continue a geração de cursos/<slug>/ a partir da semana NN seguindo 05-kit-workflow.md.`

O agente lê `coverage-matrix.md` + última semana fechada e segue.

---

### Troubleshooting comum

| Sintoma | Causa provável | Ação |
|---|---|---|
| Pesquisador não acha syllabus público | Curso só publica brochura de marketing | Aceitar `Não informado publicamente` + apoiar-se em curso-irmão top-tier via Gap Supplementation |
| Filosofia extraída soa genérica | Coordenador foi raso | Pedir reextração citando evidências específicas das fontes |
| Tutor pula categorias do diagnóstico | Não passou todos os pré-requisitos do `02-curriculum.md` | Forçar releitura completa do `02-curriculum.md` antes da entrevista |
| Theory excede 600 palavras sem declarar Caso B | Professor ignorou Theory-as-pointers | Revisor flagará — corrigir com pedido específico ao Professor |
| Notebook não executa | Falta `requirements.txt` ou kernel divergente | Verificar `cursos/<slug>/modules/NN-week-NN/code/requirements.txt` e versão do Python |
| Revisor aprova com ✓ tudo sempre | Revisor leniente | Forçar auditoria tópico-a-tópico citando `10-revisor-fidelidade.md` Passo 2 |

---

## Kits existentes

| Slug | Programa de referência | Status |
|---|---|---|
| [cmu-generative-ai-llms](cursos/cmu-generative-ai-llms/01-README.md) | CMU — Generative AI & Large Language Models | Base + semana 01 (geração antiga, pré-suite) |
| [fia-labdata-analytics-ia-data-science](cursos/fia-labdata-analytics-ia-data-science/01-README.md) | FIA / Labdata — Analytics e IA — Data Science | Base + semana 01 (geração antiga, pré-suite) |

Esses kits foram gerados antes da reestruturação para suite de personagens — servem como base histórica e referência de output. Kits novos seguirão o fluxo completo de 7 personagens (incluindo Tutor de Onboarding na Fase 2.5).

---

## Fluxo paralelo: certificações

O subprojeto [templates/certificacoes/](templates/certificacoes/template.md) cobre o caso de certificações de vendor (AZ-204, AWS-SAA, CKA, GH-200, TF-Associate, …). É um fluxo separado, com escopo e regras próprias, mas mora no mesmo repo.
