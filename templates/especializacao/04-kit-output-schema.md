# 04 — Schema de saída do kit gerado

> Define a estrutura de arquivos do kit autodidata. Convenção numérica obrigatória para preservar ordem de leitura.

---

## Estrutura de pastas

```
cursos/<slug>/
├── 01-README.md                ← gerado pelo Coordenador
├── 02-curriculum.md            ← gerado pelo Pesquisador (Fase 1)
├── 03-study-plan.md            ← gerado pelo Coordenador
├── 04-weekly-roadmap.md        ← gerado pelo Coordenador
├── 05-glossary.md              ← gerado pelo Coordenador
├── 06-concept-map.md           ← gerado pelo Coordenador
├── coverage-matrix.md          ← gerado pelo Coordenador; atualizado pelo Revisor + Tutor
├── 00-onboarding/              ← gerado pelo Tutor de Onboarding (Fase 2.5)
│   ├── diagnostic.md           ← transcript + resultado da entrevista
│   └── leveling-plan.md        ← plano de nivelamento (quantas pré-semanas, em que ordem)
├── papers/                     ← acumulado por semana
│   ├── weekly-papers.md
│   ├── paper-review-template.md
│   └── paper-reading-guide.md
├── projects/                   ← projetos maiores intermediários
├── capstone/                   ← projeto final
│   ├── 01-proposal.md
│   ├── 02-milestones.md
│   ├── 03-technical-spec.md
│   ├── 04-evaluation-rubric.md
│   ├── 05-final-report-template.md
│   └── 06-defense-template.md
├── flashcards/                 ← consolidação de flashcards por semana
└── modules/
    ├── 00-prereq-01/           ← pré-semana de nivelamento (gerada pelo Tutor; só se houver gap)
    ├── 00-prereq-02/
    ├── ...
    ├── 01-week-01/             ← semanas reais do programa
    ├── 02-week-02/
    └── ...
```

## Estrutura interna de cada semana (real ou pré-semana)

```
modules/NN-week-NN/   (ou modules/00-prereq-NN/)
├── 01-theory.md (ou .ipynb)         ← gerado pelo Professor
├── 02-readings.md                   ← gerado pelo Professor
├── 03-lab-guided.ipynb              ← DEFAULT V2: notebook executável (FIA-style)
├── 04-lab-speedrun.md               ← gerado pelo Eng. de Labs (.md, referência condensada)
├── 05-exercises.md                  ← gerado pela Banca
├── 06-mini-project.md               ← gerado pela Banca
├── 07-assessment.md                 ← gerado pela Banca
├── 08-flashcards.md                 ← gerado pela Banca
├── 09-coverage.md                   ← gerado pelo Revisor (em pré-semanas: auto-audit do Tutor)
├── code/
│   ├── requirements.txt             ← versões pinned
│   └── <scripts numerados: 01_*.py, 02_*.py, …>
└── assets/
    └── <relatórios, diagramas, templates>
```

### Formato dos arquivos por extensão

- **`01-theory`** — por default `.md`. **Pode** ser `.ipynb` quando o tópico é "aprende fazendo" (feature engineering, EDA, transformações de dados). Quando `.md`, cap de 300–600 palavras e bloco `## Leituras canônicas (capítulos)` obrigatório (ver Theory-as-pointers, `03-kit-rules.md` §4.5). Sem livro canônico → declara `> Sem livro canônico identificado` e escreve denso.
- **`03-lab-guided`** — sempre `.ipynb` (Notebook-first Practice Rule, `03-kit-rules.md` §4.6). Estrutura FIA-style: markdown curto (200–400 palavras) → célula de código → markdown de interpretação → repete. Outputs preservados após execução. Kernel Python 3.x declarado.
- **`04-lab-speedrun`** — sempre `.md`. Cola condensada de comandos + checkpoints + critérios de pass. Não é executável; é referência para re-execução rápida em revisão.

---

## Conteúdo esperado por arquivo

### `01-README.md`

Gerado pelo Coordenador.

- Visão geral do programa de referência (≤ 300 palavras).
- Filosofia pedagógica extraída (≤ 200 palavras), com evidências curtas.
- Duração do kit, carga horária semanal, proporção.
- Objetivos finais (lista executável: "ao concluir, o aluno será capaz de…").
- Metodologia (4 camadas: teoria, implementação, engenharia de sistemas, produção intelectual).
- Workflow semanal (ordem dos arquivos `01-…08-`).
- Definição de sucesso por semana ("não avance sem entregar X").
- Roadmap macro com links para `03-study-plan.md` e `04-weekly-roadmap.md`.
- Milestones (mês 3, mês 6, mês 9, mês 12 — ou equivalente).
- Aviso de não-oficialidade (este kit não é material oficial da instituição).

### `02-curriculum.md`

Gerado pelo Pesquisador. Conforma 100% ao schema canônico em `02-curriculum-schema.md`.

### `03-study-plan.md`

Gerado pelo Coordenador.

- Cronograma completo de N semanas.
- Cada semana: tema, complexidade, deliverable, tempo estimado por camada (teoria/readings/lab/mini-project/assessment/revisão).
- Dependências entre semanas explicitadas.

### `04-weekly-roadmap.md`

Gerado pelo Coordenador. Tabela macro:

| Semana | Tema | Complexidade | Deliverable | Mapeia syllabus original | Tipo |
|---:|---|---|---|---|---|
| 01 | | fundamentos / intermediário / avançado / research | | week N do original | core / supplemented / bridge |

### `05-glossary.md`

Gerado pelo Coordenador. Termos técnicos avançados do domínio. Cada termo:

- definição
- fórmula/conceito formal
- aplicação
- pitfalls
- referência oficial/paper

### `06-concept-map.md`

Gerado pelo Coordenador. Diagramas Mermaid:

- relações entre conceitos do programa
- fluxo de sistemas
- arquiteturas-chave (treino, serving, RAG, multimodal, …, conforme domínio)

### `coverage-matrix.md`

Gerado pelo Coordenador. Atualizado pelo Tutor de Onboarding (Fase 2.5) e pelo Revisor de Fidelidade (após cada semana real).

Estrutura:

```markdown
# Matriz de Cobertura

## Pré-entrada (nivelamento)

| Pré-semana | Gap diagnosticado | Mapeia para (semana real que exige) | Coberto? | Nota |
|---:|---|---:|---|---|
| 00-prereq-01 | Álgebra linear (produto interno, normas) | 01 | ⏳ pendente | — |
| 00-prereq-02 | Probabilidade + softmax | 03 | ⏳ | — |

## Semanas reais

| Semana original | Tópicos oficiais | Deliverables originais | Semana do kit | Coberto? | Suplementado? | Nota |
|---:|---|---|---:|---|---|---|
| 01 | tokenization, attention | Lab tokenizer | 01 | ⏳ pendente | — | — |
| 02 | … | … | 02 | ⏳ | — | — |
```

Estados:
- `⏳ pendente` — semana ainda não gerada
- `✓ coberto` — todos os tópicos cobertos sem suplementação
- `+ suplementado` — alguns tópicos suplementados (com fonte declarada)
- `⚠ raso` — coberto mas profundidade abaixo do original
- `✗ ausente` — tópico originalmente previsto não foi coberto

### `00-onboarding/diagnostic.md`

Gerado pelo Tutor de Onboarding. Contém:

- **Perfil declarado** do aluno (resumo de `# Observações para Adaptação Autodidata`).
- **Mapa de pré-requisitos do programa** extraído de `02-curriculum.md` + tópicos da primeira `01-theory.md` planejada.
- **Transcript da entrevista** (perguntas + respostas do usuário).
- **Diagnóstico por categoria** (matemática, programação, CS, domínio): `confortável` / `enferrujado` / `vazio`.
- **Auto-audit**: cada pré-semana gerada cobre qual gap específico?

### `00-onboarding/leveling-plan.md`

Gerado pelo Tutor de Onboarding. Contém:

- Total de pré-semanas: N (ou 0 se diagnóstico não exige).
- Ordem das pré-semanas e tema de cada uma.
- Mapeamento: pré-semana → gap → semana real onde o conhecimento será usado pela primeira vez.
- Tempo estimado total do nivelamento (horas).

### `09-coverage.md` por semana

Gerado pelo Revisor de Fidelidade. Audit report da semana. Para cada tópico previsto na semana N do syllabus original:

```markdown
## Tópico: <nome>

- **Previsto no original:** sim | parcialmente | não
- **Coberto no kit:** ✓ / ⚠ / ✗ / +
- **Profundidade comparada:** equivalente | abaixo | acima
- **Evidência:** <link interno: 01-theory.md#section, 02-readings.md, código X>
- **Gap action:** <nenhuma | retornar para Professor | retornar para Eng-Labs | retornar para Banca>
```

### Arquivos da semana (`01-theory.md` ... `08-flashcards.md`)

Ver responsabilidades das personas em `06`–`09`. Cada arquivo segue regras de `03-kit-rules.md`.

---

## Convenções de nomenclatura

- **Slug** do curso: `<instituicao-curta>-<curso-curto>`, kebab-case.
- **Pasta de semana**: `NN-week-NN/` (zero-padded). Ex: `01-week-01/`, `12-week-12/`.
- **Arquivos com prefixo numérico** para preservar ordem visual.
- **Scripts em `code/`**: prefixo numérico também (`01_environment_check.py`, `02_*.py`).
- **Idioma**: pt-BR para texto explicativo, com termos técnicos em inglês quando padrão na literatura.
