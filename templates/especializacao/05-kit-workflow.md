# 05 — Workflow de execução

> Orquestração das 6 personagens. Define **quando** cada uma é invocada, em **que ordem**, com **que inputs**, e como o estado avança.
>
> A execução é **incremental e manual** — o usuário invoca cada persona explicitamente. Não há orquestrador automático nesta versão.

---

## Diagrama de fases

```
┌─────────────────────────────────────────────────────────────────┐
│ FASE 1 — Pesquisa                                               │
│  └─ Pesquisador Acadêmico (01-prompt-curriculum.md)             │
│       output: cursos/<slug>/02-curriculum.md                    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ FASE 2 — Coordenação (base do kit)                              │
│  └─ Coordenador de Curso (06-coordenador-curso.md)              │
│       output:                                                   │
│         - 01-README.md (com filosofia extraída)                 │
│         - 03-study-plan.md                                      │
│         - 04-weekly-roadmap.md                                  │
│         - 05-glossary.md                                        │
│         - 06-concept-map.md                                     │
│         - coverage-matrix.md (esqueleto com semanas pendentes)  │
│       update no 02-curriculum.md:                               │
│         - seção "Filosofia Pedagógica Extraída"                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ FASE 3 — Geração de semana N (loop)                             │
│                                                                 │
│  3.1  Professor da Disciplina  (07-professor-disciplina.md)     │
│        → 01-theory.md + 02-readings.md                          │
│                                                                 │
│  3.2  Engenheiro de Labs       (08-engenheiro-labs.md)          │
│        → 03-lab-guided.md + 04-lab-speedrun.md + code/          │
│                                                                 │
│  3.3  Banca Examinadora        (09-banca-avaliacao.md)          │
│        → 05-exercises.md + 06-mini-project.md +                 │
│          07-assessment.md (com rubrica + model answers) +       │
│          08-flashcards.md                                       │
│                                                                 │
│  3.4  Revisor de Fidelidade    (10-revisor-fidelidade.md)       │
│        → 09-coverage.md                                         │
│        → update coverage-matrix.md (linha da semana N)          │
│        → se ⚠ ou ✗, RETORNAR para 3.1/3.2/3.3 conforme gap      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
                         (repetir 3 até N final)
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ FASE 4 — Capstone (opcional, ao final)                          │
│  └─ Coordenador + Banca colaboram em capstone/*.md              │
└─────────────────────────────────────────────────────────────────┘
```

---

## Comandos do usuário (interface)

### Iniciar um novo kit

```
Crie o curriculum.md para o curso "<NOME_DO_CURSO>" da instituição "<NOME_DA_INSTITUICAO>"
usando templates/especializacao/01-prompt-curriculum.md.
```

A Fase 1 roda. O resultado fica em `cursos/<slug>/02-curriculum.md`. Antes de seguir, o usuário **revisa** o `02-curriculum.md` (fontes, lacunas, professores extraídos).

### Gerar a base do kit

```
Gere a base do kit em cursos/<slug>/ usando 06-coordenador-curso.md
a partir de cursos/<slug>/02-curriculum.md.
```

A Fase 2 roda. Outputs: `01-README.md`, `03-study-plan.md`, `04-weekly-roadmap.md`, `05-glossary.md`, `06-concept-map.md`, `coverage-matrix.md`, e atualização do `02-curriculum.md` com a filosofia extraída.

O usuário revisa especialmente:
- A **filosofia pedagógica extraída** no `01-README.md`.
- O **mapeamento syllabus original ↔ semanas do kit** no `coverage-matrix.md`.

### Gerar semana N

```
Gere a semana NN do kit cursos/<slug>/ seguindo 05-kit-workflow.md Fase 3.
```

Internamente, isso significa invocar `07` → `08` → `09` → `10` em sequência, gravando em `modules/NN-week-NN/`.

Quando o Revisor (`10`) flagar `⚠` ou `✗`, ele retorna o controle para a persona apropriada (`07`/`08`/`09`) com pedido específico. O loop só termina quando a matriz da semana N estiver sem `✗` (gaps catastróficos) e com todos os `⚠` justificados ou suplementados conforme regra `4.3`.

### Auditoria avulsa

```
Audite cursos/<slug>/modules/NN-week-NN/ usando 10-revisor-fidelidade.md.
```

Útil para retornar a uma semana antiga e revalidar após mudança no `02-curriculum.md`.

---

## Inputs e outputs por fase (resumo tabular)

| Fase | Persona | Lê | Escreve |
|---|---|---|---|
| 1 | Pesquisador (`01`) | inputs do usuário; web | `cursos/<slug>/02-curriculum.md` |
| 2 | Coordenador (`06`) | `02-curriculum.md`; `03-kit-rules.md`; `04-kit-output-schema.md` | `01-README.md`, `03-study-plan.md`, `04-weekly-roadmap.md`, `05-glossary.md`, `06-concept-map.md`, `coverage-matrix.md`; atualiza `02-curriculum.md` (filosofia) |
| 3.1 | Professor (`07`) | `02-curriculum.md`, `03-study-plan.md`, `03-kit-rules.md`, filosofia, professores extraídos | `modules/NN-week-NN/01-theory.md`, `02-readings.md` |
| 3.2 | Eng-Labs (`08`) | `01-theory.md`, `02-readings.md`, filosofia | `modules/NN-week-NN/03-lab-guided.md`, `04-lab-speedrun.md`, `code/` |
| 3.3 | Banca (`09`) | todo conteúdo da semana | `modules/NN-week-NN/05-exercises.md`, `06-mini-project.md`, `07-assessment.md`, `08-flashcards.md` |
| 3.4 | Revisor (`10`) | semana gerada + `02-curriculum.md` + `coverage-matrix.md` | `modules/NN-week-NN/09-coverage.md`; atualiza linha da semana N em `coverage-matrix.md` |

---

## Regras de avanço

- **Não gere uma semana sem ter o `coverage-matrix.md` da base.** O Coordenador precisa ter rodado.
- **Não pule do Pesquisador direto para o Professor.** Sem filosofia extraída pelo Coordenador, o Professor não tem como calibrar a voz.
- **Não feche a semana com `✗` no `09-coverage.md`.** `✗` significa tópico previsto pelo syllabus original sem qualquer cobertura — é falha do clone.
- **Geração incremental, não em lote.** Não gere todas as semanas de uma vez. O loop de revisão é o que garante qualidade.

---

## Diretório operacional

Todas as ações na Fase 2 e Fase 3 escrevem em `cursos/<slug>/`. A Fase 1 também — exceto que ela cria a pasta `cursos/<slug>/` se ainda não existir.

A pasta `templates/` é **read-only** durante o uso. Só é editada quando se itera nos prompts em si (melhorias na metodologia), não durante a geração de um kit.
