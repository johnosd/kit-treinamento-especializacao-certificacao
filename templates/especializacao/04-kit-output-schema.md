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
├── coverage-matrix.md          ← gerado pelo Coordenador; atualizado pelo Revisor
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
    ├── 01-week-01/
    ├── 02-week-02/
    └── ...
```

## Estrutura interna de cada semana

```
modules/NN-week-NN/
├── 01-theory.md          ← gerado pelo Professor
├── 02-readings.md        ← gerado pelo Professor
├── 03-lab-guided.md      ← gerado pelo Eng. de Labs
├── 04-lab-speedrun.md    ← gerado pelo Eng. de Labs
├── 05-exercises.md       ← gerado pela Banca
├── 06-mini-project.md    ← gerado pela Banca
├── 07-assessment.md      ← gerado pela Banca
├── 08-flashcards.md      ← gerado pela Banca
├── 09-coverage.md        ← gerado pelo Revisor (audit report da semana)
├── code/
│   ├── requirements.txt
│   └── <scripts numerados: 01_*.py, 02_*.py, …>
└── assets/
    └── <relatórios, diagramas, templates>
```

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

Gerado pelo Coordenador. Atualizado pelo Revisor de Fidelidade após cada semana.

Estrutura:

```markdown
# Matriz de Cobertura

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
