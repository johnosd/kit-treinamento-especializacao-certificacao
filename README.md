# MBA AutoDirigido — Guias, Prompts e Kits de Estudo

Este repositório organiza prompts e materiais gerados para criar kits de estudo autodirigido em nível de pós-graduação técnica, com foco em profundidade, implementação real, leitura de papers, engenharia de sistemas e produção de projetos.

O fluxo foi desenhado para funcionar em duas etapas:

1. **Extrair e estruturar uma grade curricular oficial** a partir de fontes públicas.
2. **Gerar um kit de estudos incremental** a partir dessa grade, sem criar o curso inteiro de uma vez.

---

## Estrutura Geral

```txt
MBA AutoDirigido/
├── README.md
├── Apresentacao.md
├── Bibliografia.md
├── kit-estudo-especializacao/
│   ├── template.md
│   └── curriculum-source/
│       ├── prompt-curriculum.md
│       ├── template_curriculum.md
│       ├── curriculum-fia.md
│       └── curriculum-cmu.md
├── kit-estudo-certificacoes/
│   └── template.md
├── fia-labdata-analytics-ia-data-science/
└── cmu-generative-ai-llms/
```

## Componentes Principais

| Caminho | Função |
|---|---|
| `kit-estudo-especializacao/curriculum-source/prompt-curriculum.md` | Prompt para pesquisar e estruturar currículos oficiais. |
| `kit-estudo-especializacao/curriculum-source/template_curriculum.md` | Template manual para preencher uma fonte curricular quando a pesquisa já foi feita. |
| `kit-estudo-especializacao/template.md` | Prompt principal para gerar o kit de especialização a partir de um currículo estruturado. |
| `kit-estudo-certificacoes/template.md` | Prompt separado para kits de certificações técnicas. |
| `kit-estudo-especializacao/curriculum-source/curriculum-fia.md` | Currículo estruturado da FIA/Labdata. |
| `kit-estudo-especializacao/curriculum-source/curriculum-cmu.md` | Currículo estruturado da CMU. |
| `fia-labdata-analytics-ia-data-science/` | Kit gerado para FIA/Labdata. |
| `cmu-generative-ai-llms/` | Kit gerado para CMU. |

---

## Fluxo de Uso

### 1. Escolher um curso de referência

Defina:

- nome do curso;
- instituição;
- URL oficial;
- páginas complementares, como syllabus, schedule, assignments, PDFs ou ementas públicas.

Exemplo:

```txt
Curso: CMU — Generative AI & Large Language Models
Instituição: Carnegie Mellon University
URL: https://www.cmu.edu/online/generative-ai-llms
Complementos:
- https://2025.cmu-llms.org/syllabus/
- https://2025.cmu-llms.org/schedule/
- https://2025.cmu-llms.org/assignments/
```

---

### 2. Criar o currículo-fonte

Use o prompt:

```txt
kit-estudo-especializacao/curriculum-source/prompt-curriculum.md
```

Objetivo desse prompt:

- pesquisar a grade curricular oficial;
- priorizar fontes oficiais;
- extrair módulos, disciplinas, ementas, avaliações e bibliografia;
- marcar campos não publicados como `Não informado`;
- organizar tudo em Markdown.

Saída recomendada:

```txt
kit-estudo-especializacao/curriculum-source/curriculum-<slug>.md
```

Exemplos atuais:

```txt
kit-estudo-especializacao/curriculum-source/curriculum-fia.md
kit-estudo-especializacao/curriculum-source/curriculum-cmu.md
```

Regra importante: o currículo-fonte deve preservar a distinção entre:

- informação publicada oficialmente;
- complemento curricular público;
- inferência pedagógica;
- lacuna não publicada.

---

### 3. Gerar o kit de especialização

Use o prompt:

```txt
kit-estudo-especializacao/template.md
```

Informe explicitamente qual currículo-fonte deve ser usado:

```txt
Use o template.md e como entrada use:
kit-estudo-especializacao/curriculum-source/curriculum-cmu.md
```

O template deve gerar apenas o **Passo 1**:

```txt
README
curriculum
study-plan
weekly-roadmap
glossary
concept-map
```

Não gere semanas, labs, papers completos, capstone ou projetos avançados nessa etapa inicial.

---

### 4. Gerar semanas incrementalmente

Depois do Passo 1, solicite:

```txt
Generate Week 01
```

ou, em português:

```txt
gere a primeira semana
```

Cada semana deve criar apenas a pasta daquela semana.

Para kits numerados, use:

```txt
modules/
├── 01-week-01/
├── 02-week-02/
└── ...
```

Dentro da semana:

```txt
01-theory.md
02-readings.md
03-lab-guided.md
04-lab-speedrun.md
05-exercises.md
06-mini-project.md
07-assessment.md
08-flashcards.md
code/
assets/
```

Essa convenção melhora navegação e evita dúvida sobre a ordem de estudo.

---

## Kits Gerados Atualmente

### FIA/Labdata — Analytics e Inteligência Artificial — Data Science

Pasta:

```txt
fia-labdata-analytics-ia-data-science/
```

Status:

- Passo 1 gerado.
- Semana 01 gerada.
- Arquivos ainda seguem a convenção original sem prefixos numéricos nos arquivos base.

Semana 01:

```txt
fia-labdata-analytics-ia-data-science/modules/week-01/
```

Tema:

- Ciência de Dados, Analytics e IA.
- Framing de problema.
- Métrica, baseline, riscos e go/no-go.

---

### CMU — Generative AI & Large Language Models

Pasta:

```txt
cmu-generative-ai-llms/
```

Status:

- Passo 1 gerado.
- Semana 01 gerada.
- Arquivos seguem prefixos numéricos.

Arquivos base:

```txt
01-README.md
02-curriculum.md
03-study-plan.md
04-weekly-roadmap.md
05-glossary.md
06-concept-map.md
```

Semana 01:

```txt
cmu-generative-ai-llms/modules/01-week-01/
```

Tema:

- Diagnóstico técnico.
- Setup.
- PyTorch/Hugging Face readiness.
- Tokenização mínima.
- Tensorização.
- Cross-entropy, softmax, perplexity e next-token prediction.

---

## Como Usar Cada Kit

Para cada kit, siga esta ordem:

1. Leia o `README`.
2. Leia o `curriculum`.
3. Leia o `study-plan`.
4. Consulte o `weekly-roadmap`.
5. Use o `glossary` como referência contínua.
6. Consulte o `concept-map` para entender relações entre conceitos.
7. Entre na semana atual em `modules/`.
8. Siga a ordem dos arquivos da semana.
9. Execute os labs.
10. Complete assessment e flashcards.
11. Só então gere a próxima semana.

Regra prática: não avance semana se você não produziu o entregável técnico da semana atual.

---

## Critérios de Qualidade

Todo material gerado deve seguir estes critérios:

- usar fontes oficiais, papers ou documentação primária;
- separar fato oficial de inferência;
- incluir teoria, implementação, arquitetura, tradeoffs e limitações;
- exigir código ou artefato técnico quando aplicável;
- incluir avaliação, failure modes e custo computacional;
- evitar conteúdo superficial, motivacional ou tutorial trivial;
- priorizar projetos acumulativos e defesa técnica.

---

## Convenções Recomendadas

### Currículos-fonte

```txt
kit-estudo-especializacao/curriculum-source/curriculum-<instituicao-ou-curso>.md
```

Exemplos:

```txt
curriculum-cmu.md
curriculum-fia.md
```

### Kits gerados

```txt
<slug-do-programa>/
```

Exemplos:

```txt
cmu-generative-ai-llms/
fia-labdata-analytics-ia-data-science/
```

### Arquivos base numerados

Para novos kits, prefira:

```txt
01-README.md
02-curriculum.md
03-study-plan.md
04-weekly-roadmap.md
05-glossary.md
06-concept-map.md
```

### Semanas numeradas

```txt
modules/01-week-01/
modules/02-week-02/
modules/03-week-03/
```

### Arquivos internos da semana

```txt
01-theory.md
02-readings.md
03-lab-guided.md
04-lab-speedrun.md
05-exercises.md
06-mini-project.md
07-assessment.md
08-flashcards.md
```

---

## Próximos Passos de Melhoria

### 1. Atualizar o `template.md` para aceitar fonte parametrizada

Hoje o template menciona `curriculum.md` como fonte padrão, mas na prática já usamos múltiplas fontes:

```txt
curriculum-fia.md
curriculum-cmu.md
```

Melhoria:

```txt
<<CURRICULUM_SOURCE_FILE>>
```

Exemplo:

```txt
<<CURRICULUM_SOURCE_FILE>> = kit-estudo-especializacao/curriculum-source/curriculum-cmu.md
```

---

### 2. Incorporar oficialmente a convenção de numeração

Adicionar ao template principal:

- arquivos base com prefixos `01-`, `02-`, etc.;
- semanas como `01-week-01`;
- arquivos internos da semana numerados.

Isso deve virar regra padrão para todos os novos kits.

---

### 3. Criar um `status.md` por kit

Cada kit pode ter:

```txt
00-status.md
```

Com:

- semanas geradas;
- semanas concluídas;
- labs executados;
- pendências;
- próximos comandos recomendados.

---

### 4. Criar validação automática de estrutura

Adicionar script para checar:

- arquivos obrigatórios do Passo 1;
- estrutura de cada semana;
- presença de `code/` e `assets/`;
- links quebrados internos;
- placeholders `TODO` ou `<<...>>` não resolvidos.

Sugestão:

```txt
tools/validate-kit.py
```

---

### 5. Criar templates reutilizáveis para semanas

Criar:

```txt
kit-estudo-especializacao/templates/week/
```

Com arquivos vazios ou parcialmente preenchidos:

```txt
01-theory.md
02-readings.md
03-lab-guided.md
04-lab-speedrun.md
05-exercises.md
06-mini-project.md
07-assessment.md
08-flashcards.md
```

---

### 6. Melhorar geração de papers

Criar uma pasta por kit:

```txt
papers/
├── 01-weekly-papers.md
├── 02-paper-review-template.md
└── 03-paper-reading-guide.md
```

Cada semana deve ter 2-5 papers:

- seminal;
- foundational;
- SOTA relevante;
- systems paper quando houver impacto operacional.

---

### 7. Adicionar exportação Anki

Além de `flashcards.md`, gerar:

```txt
flashcards.csv
```

Formato:

```csv
frente;verso;tags
```

---

### 8. Separar ambientes por kit

Cada kit pode ter:

```txt
environment/
├── requirements.txt
├── requirements-gpu.txt
├── environment.yml
└── setup.md
```

Isso evita misturar dependências de Data Science clássico, LLM systems e multimodal.

---

### 9. Versionar decisões pedagógicas

Criar:

```txt
decision-log.md
```

Para registrar:

- por que o plano tem 48 ou 64 semanas;
- por que um paper foi escolhido;
- quais tópicos foram inferidos;
- quais fontes oficiais não publicaram detalhes.

---

### 10. Gerar capstone desde o início

Mesmo que o capstone só seja implementado no fim, criar cedo:

```txt
capstone/
├── 01-proposal.md
├── 02-milestones.md
├── 03-technical-spec.md
├── 04-evaluation-rubric.md
├── 05-final-report-template.md
└── 06-defense-template.md
```

Assim cada semana pode alimentar o projeto final.

---

## Comandos Úteis Para Continuação

Gerar próxima semana do CMU:

```txt
gere a segunda semana do kit cmu-generative-ai-llms seguindo a convenção numerada
```

Gerar próxima semana do FIA:

```txt
gere a segunda semana do kit fia-labdata-analytics-ia-data-science
```

Criar novo currículo-fonte:

```txt
use prompt-curriculum.md para criar curriculum-<slug>.md do curso <nome> da instituição <instituição>
```

Criar novo kit:

```txt
use template.md com entrada curriculum-<slug>.md e gere somente o Passo 1 com arquivos numerados
```

---

## Regra Central

Este repositório deve crescer incrementalmente. Primeiro fonte curricular, depois kit base, depois semanas uma por uma. A qualidade vem de manter o ciclo pequeno, verificável e tecnicamente defensável.
