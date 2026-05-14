````md
# 🎓 Prompt Template — LLM / Generative AI Graduate-Level Self-Study Kit

> Objetivo:
> Gerar um kit de estudos autodidata equivalente a uma pós-graduação técnica em LLMs / Generative AI, baseado em uma grade curricular oficial (ex: CMU, Stanford, Berkeley etc.), com geração incremental por semana/módulo.
>
> O foco NÃO é certificação.
>
> O foco é:
> - profundidade técnica;
> - implementação real;
> - leitura de papers;
> - engenharia de sistemas;
> - raciocínio crítico;
> - produção de projetos;
> - domínio equivalente ao de uma pós-graduação séria.

---

# 📋 Variáveis

## Obrigatórias

| Variável | Exemplo |
|---|---|
| `<<PROGRAM_NAME>>` | `CMU — Generative AI & Large Language Models` |
| `<<PROGRAM_DURATION>>` | `12 months`, `24 weeks`, `36 weeks` |
| `<<HOURS_PER_WEEK>>` | `10`, `15`, `20` |
| `<<FOCUS_RATIO>>` | `60% engineering / 40% theory` |
| `<<PRIMARY_STACK>>` | `Python + PyTorch + HuggingFace + vLLM + OpenAI APIs` |
| `<<EXECUTION_ENVIRONMENT>>` | `local GPU`, `cloud GPU`, `CPU-only`, `mixed` |
| `<<LANGUAGE>>` | `pt-BR`, `en-US` |

---

## Opcionais

| Variável | Exemplo |
|---|---|
| `<<BACKGROUND>>` | `Data Engineer with ML basics` |
| `<<WEAK_AREAS>>` | `mathematics, distributed systems` |
| `<<STRONG_AREAS>>` | `Python, backend engineering` |
| `<<NOTE_TOOL>>` | `Obsidian`, `Notion`, `none` |
| `<<LEARNING_STYLE>>` | `hands-on heavy`, `research heavy`, `balanced` |
| `<<USE_COMMERCIAL_APIS>>` | `yes/no` |
| `<<USE_OPEN_SOURCE_MODELS>>` | `yes/no` |
| `<<TARGET_OUTCOME>>` | `research engineer`, `LLM systems engineer`, `GenAI architect` |

---

# 📚 Input obrigatório — Curriculum Source

Você deve ler obrigatoriamente o arquivo abaixo, relativo à raiz deste workspace:

```txt
kit-estudo-especializacao/curriculum-source/curriculum.md
```

Este arquivo será a FONTE CENTRAL da geração. Ele deve conter:

- a grade curricular oficial do programa;
- links oficiais da instituição ou disciplina;
- módulos, semanas, tópicos, leituras, papers, labs e avaliações oficiais;
- o material bruto colado da fonte, quando disponível;
- os valores preenchidos para as variáveis obrigatórias e opcionais do kit.

NÃO use `template.md` como fonte curricular. O `template.md` define as regras de geração; o conteúdo curricular deve vir de `curriculum-source/curriculum.md`.

## Ordem de precedência dos dados

Ao gerar o kit, resolva os dados nesta ordem:

1. Valores preenchidos em `kit-estudo-especializacao/curriculum-source/curriculum.md`.
2. Texto bruto colado na seção `Material Bruto Colado da Fonte` do mesmo arquivo.
3. Variáveis informadas explicitamente pelo usuário no pedido atual.
4. Inferências conservadoras a partir da grade oficial.

Se uma variável obrigatória continuar ausente ou ambígua, registre a pendência no arquivo gerado e use um placeholder claro, em vez de inventar.

Você deve:
- parsear;
- estruturar;
- decompor em semanas/módulos;
- inferir dependências;
- identificar fundamentos;
- identificar tópicos avançados;
- identificar sequência pedagógica ideal.
- extrair ou validar as variáveis `<<PROGRAM_NAME>>`, `<<PROGRAM_DURATION>>`, `<<HOURS_PER_WEEK>>`, `<<FOCUS_RATIO>>`, `<<PRIMARY_STACK>>`, `<<EXECUTION_ENVIRONMENT>>` e `<<LANGUAGE>>` a partir da seção `Observações para Adaptação Autodidata`.

---

# 🚨 Regras Absolutas

## 1. Qualidade acadêmica

O material gerado deve ter nível:
- pós-graduação técnica;
- Mestrado profissional;
- research engineering;
- senior/principal engineer training.

NUNCA gerar:
- conteúdo superficial;
- tutorial de iniciante;
- “hello world” inútil;
- explicações infantis;
- fluff;
- motivação genérica.

---

## 2. Fontes permitidas

Prioridade máxima:
- papers originais;
- documentação oficial;
- repositórios oficiais;
- artigos técnicos oficiais.

Fontes permitidas:
- arxiv.org
- paperswithcode.com
- huggingface.co
- pytorch.org
- tensorflow.org
- openai.com
- anthropic.com
- mistral.ai
- llama.meta.com
- docs.vllm.ai
- ray.io
- kubernetes.io
- docs.aws.amazon.com
- learn.microsoft.com
- developer.nvidia.com
- github oficial dos projetos

NUNCA usar:
- blogs genéricos;
- Medium aleatório;
- cursos genéricos;
- YouTube genérico;
- conteúdo motivacional;
- sites de “resumo”.

---

## 3. Profundidade obrigatória

Sempre incluir:
- teoria;
- implementação;
- arquitetura;
- tradeoffs;
- limitações;
- scaling;
- avaliação;
- benchmarks;
- failure modes;
- deployment;
- custo computacional.

---

# 🎯 Objetivo pedagógico

O aluno deve terminar o programa sendo capaz de:

- entender internals de transformers;
- treinar/fine-tunar modelos;
- implementar pipelines RAG;
- construir agentes;
- operar sistemas LLM em produção;
- otimizar inferência;
- trabalhar com embeddings;
- construir sistemas multimodais;
- ler papers modernos;
- reproduzir resultados;
- avaliar modelos;
- projetar arquitetura de GenAI em escala;
- discutir tecnicamente como um research/ML engineer.

---

# 📂 Estrutura do workspace

Use esta estrutura de entrada e saída.

Entrada obrigatória, já existente ou preenchida pelo usuário:

```txt
kit-estudo-especializacao/
└── curriculum-source/
    └── curriculum.md
```

Saída gerada pelo agente:

```txt
<<PROGRAM_NAME>>/
├── README.md
├── curriculum.md
├── study-plan.md
├── weekly-roadmap.md
├── glossary.md
├── concept-map.md
├── grading-rubric.md
├── mistake-log.md
├── flashcards/
├── papers/
├── projects/
├── assessments/
├── capstone/
├── modules/
│   ├── week-01/
│   ├── week-02/
│   ├── week-03/
│   └── ...
└── notes-template.md
````

---

# 📌 README.md

Deve conter:

* visão geral do programa;
* duração;
* carga horária;
* stack usada;
* objetivos finais;
* metodologia;
* como estudar;
* workflow semanal;
* definição de sucesso;
* roadmap macro;
* milestones.

---

# 📌 curriculum.md

Deve:

* reproduzir a grade original;
* reorganizar em módulos;
* identificar dependências;
* marcar:

  * fundamentos;
  * intermediário;
  * avançado;
  * research-level.

---

# 📌 study-plan.md

Gerar cronograma completo baseado em:

* `<<PROGRAM_DURATION>>`
* `<<HOURS_PER_WEEK>>`
* `<<FOCUS_RATIO>>`

Cada semana deve possuir:

* teoria;
* leitura;
* implementação;
* lab;
* mini-projeto;
* flashcards;
* revisão;
* assessment.

---

# 📌 weekly-roadmap.md

Mapa macro de semanas:

| Semana | Tema | Complexidade | Deliverable |
| ------ | ---- | ------------ | ----------- |

---

# 📌 glossary.md

Glossário técnico avançado:

* transformers;
* attention;
* KV cache;
* RLHF;
* PEFT;
* MoE;
* speculative decoding;
* quantization;
* tensor parallelism;
* etc.

Cada termo:

* definição;
* fórmula/conceito;
* aplicação;
* pitfalls;
* referência oficial/paper.

---

# 📌 concept-map.md

Gerar diagramas Mermaid:

* relações entre conceitos;
* fluxo de sistemas;
* arquitetura de treinamento;
* serving pipeline;
* RAG pipeline;
* multimodal pipeline.

---

# 📌 papers/

Criar:

* `weekly-papers.md`
* `paper-review-template.md`
* `paper-reading-guide.md`

Cada semana:

* 2–5 papers obrigatórios;
* prioridade:

  * seminal;
  * foundational;
  * SOTA relevante.

Cada paper:

* resumo;
* contribuição;
* limitações;
* conceitos-chave;
* relação com o módulo.

---

# 📌 modules/week-XX/

Cada semana deve conter:

```txt
week-XX/
├── theory.md
├── readings.md
├── lab-guided.md
├── lab-speedrun.md
├── exercises.md
├── mini-project.md
├── assessment.md
├── flashcards.md
├── code/
└── assets/
```

---

# 📌 theory.md

Explicação técnica aprofundada:

* matemática;
* arquitetura;
* engenharia;
* tradeoffs;
* exemplos;
* diagrams;
* benchmarks;
* implementação.

---

# 📌 readings.md

Lista de:

* papers;
* docs;
* RFCs;
* repos;
* benchmarks.

---

# 📌 lab-guided.md

Lab didático completo:

* explicação;
* por quê;
* troubleshooting;
* profiling;
* debugging;
* interpretação de resultados.

---

# 📌 lab-speedrun.md

Versão condensada:

* comandos;
* checkpoints;
* expected outputs.

---

# 📌 exercises.md

Exercícios reais:

* implementação;
* debugging;
* arquitetura;
* análise;
* otimização;
* comparação.

Evitar perguntas triviais.

---

# 📌 mini-project.md

Mini projeto semanal:

* aplicável;
* realista;
* incremental;
* alinhado ao tema da semana.

---

# 📌 assessment.md

Avaliação técnica:

* perguntas abertas;
* design questions;
* debugging;
* architecture review;
* tradeoff analysis.

NÃO usar apenas múltipla escolha.

---

# 📌 flashcards/

Gerar:

* active recall;
* fórmulas;
* limites;
* conceitos;
* arquitetura;
* pitfalls.

Formato compatível com Anki.

---

# 📌 projects/

Projetos maiores intermediários:

* RAG system;
* fine-tuning pipeline;
* evaluation framework;
* multimodal retrieval;
* inference optimization;
* agentic workflows;
* LLM observability.

---

# 📌 capstone/

Projeto final equivalente a pós-graduação.

Criar:

* `proposal.md`
* `milestones.md`
* `technical-spec.md`
* `evaluation-rubric.md`
* `presentation-template.md`
* `final-report-template.md`

O capstone deve exigir:

* arquitetura;
* implementação;
* avaliação;
* benchmarking;
* documentação;
* defesa técnica.

---

# 📌 grading-rubric.md

Rubrica formal:

* iniciante;
* intermediário;
* avançado;
* research-ready.

Critérios:

* profundidade;
* clareza;
* engenharia;
* otimização;
* análise crítica;
* reprodução;
* benchmarking.

---

# 📌 mistake-log.md

Template:

* conceito errado;
* causa raiz;
* correção;
* paper relacionado;
* revisão futura.

---

# 📌 notes-template.md

Template para notas técnicas:

* conceitos;
* fórmulas;
* insights;
* bugs;
* benchmarks;
* arquitetura;
* paper notes.

---

# 🔥 Geração incremental obrigatória

NÃO gerar o curso inteiro de uma vez.

Fluxo correto:

## Passo 1

Gerar apenas:

* README
* curriculum
* study-plan
* weekly-roadmap
* glossary
* concept-map

## Passo 2

Quando solicitado:
“Generate Week 01”

Gerar somente:

* `week-01/*`

## Passo 3

Continuar incrementalmente:

* Week 02
* Week 03
* etc.

---

# 📈 Requisitos técnicos obrigatórios

Sempre que aplicável incluir:

* PyTorch;
* Hugging Face;
* tokenizers;
* PEFT;
* LoRA;
* quantization;
* vLLM;
* Triton;
* Ray;
* LangChain/LangGraph;
* vector databases;
* evaluation frameworks;
* inference optimization;
* observability;
* distributed training;
* multimodal tooling.

---

# 🧠 Nível esperado das semanas avançadas

Semanas avançadas devem incluir:

* scaling laws;
* RLHF;
* DPO;
* synthetic data;
* efficient serving;
* speculative decoding;
* MoE;
* long-context models;
* multimodal alignment;
* LLM systems engineering;
* distributed systems;
* inference infra.

---

# 🚀 Workflow de execução

1. Ler `kit-estudo-especializacao/curriculum-source/curriculum.md`
2. Extrair a grade oficial, módulos, semanas, leituras, avaliações e material bruto
3. Resolver as variáveis obrigatórias e opcionais preenchidas no próprio `curriculum.md`
4. Estruturar programa
5. Identificar dependências
6. Criar roadmap
7. Criar glossário
8. Criar concept-map
9. Esperar comando:

   * “Generate Week 01”

Antes de gerar qualquer arquivo, confirme internamente:

- se o arquivo de entrada existe;
- se a seção `Observações para Adaptação Autodidata` foi preenchida;
- se ainda há placeholders obrigatórios sem valor;
- se o nome da pasta de saída `<<PROGRAM_NAME>>/` foi resolvido.

Após isso:

- gerar apenas a etapa solicitada;
- nunca sobrescrever `kit-estudo-especializacao/curriculum-source/curriculum.md`;
- copiar a grade original para o `<<PROGRAM_NAME>>/curriculum.md` gerado, reorganizando-a e anotando dependências.

---

# ✅ Critério de sucesso

O material final deve parecer:

* uma mistura de:

  * CMU;
  * Stanford CS324;
  * Berkeley;
  * HuggingFace engineering;
  * OpenAI engineering;
  * systems engineering training.

E NÃO:

* bootcamp superficial;
* curso de influencer;
* tutorial introdutório.

```
```
