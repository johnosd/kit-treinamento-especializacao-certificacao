# 01 — CMU — Generative AI & Large Language Models

Kit autodidata de nível pós-graduação técnica baseado no certificado online **Generative AI & Large Language Models** da Carnegie Mellon University e nos complementos públicos do curso **Large Language Models: Methods and Applications / Fall 2025**.

Este kit não é material oficial da CMU. Ele é uma adaptação incremental para estudo autônomo, com foco em teoria, implementação, leitura de papers, engenharia de sistemas LLM, avaliação, deployment e raciocínio crítico.

---

## Ordem de Navegação

Use os arquivos nesta ordem:

| Ordem | Arquivo | Função |
|---:|---|---|
| 01 | `01-README.md` | visão geral, metodologia e milestones |
| 02 | `02-curriculum.md` | currículo reorganizado e dependências |
| 03 | `03-study-plan.md` | plano completo de 48 semanas |
| 04 | `04-weekly-roadmap.md` | mapa rápido semana a semana |
| 05 | `05-glossary.md` | glossário técnico avançado |
| 06 | `06-concept-map.md` | mapas Mermaid de conceitos e sistemas |

Convenção para próximas gerações:

```txt
modules/
├── 01-week-01/
├── 02-week-02/
├── 03-week-03/
└── ...
```

Dentro de cada semana, os arquivos também devem seguir ordem numérica:

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

---

## Visão Geral

| Campo | Valor |
|---|---|
| Programa de referência | CMU — Generative AI & Large Language Models |
| Instituição | Carnegie Mellon University — School of Computer Science |
| Tipo | Online Graduate Certificate |
| Duração oficial | 12 months |
| Plano autodidata | 48 semanas |
| Carga recomendada | 10-15h/semana |
| Proporção | 60% engineering / 40% theory |
| Idioma | pt-BR, com termos técnicos em inglês |
| Stack principal | Python, PyTorch, Hugging Face, tokenizers, PEFT/LoRA, vLLM, OpenAI APIs, vector databases, Ray/DeepSpeed basics |
| Ambiente | CPU local para labs pequenos, cloud GPU/A10g-class para treino, APIs comerciais para labs selecionados |

---

## Fontes Base

- Certificado CMU: <https://www.cmu.edu/online/generative-ai-llms>
- Syllabus 2025: <https://2025.cmu-llms.org/syllabus/>
- Schedule 2025: <https://2025.cmu-llms.org/schedule/>
- Assignments 2025: <https://2025.cmu-llms.org/assignments/>

Fonte local usada para esta geração:

```txt
kit-estudo-especializacao/curriculum-source/curriculum-cmu.md
```

---

## Objetivos Finais

Ao concluir o programa, você deve conseguir:

- explicar language modeling, Transformers, attention, tokenization e objetivos de pré-treinamento;
- preparar, filtrar, deduplicar e auditar dados de pré-treinamento;
- implementar componentes de Transformer em PyTorch;
- usar Hugging Face para inferência, fine-tuning e avaliação;
- construir RAG com retrieval, reranking, avaliação e análise de falhas;
- implementar tool use e workflows agentic com limites claros;
- avaliar LLMs com benchmarks, evals customizados, análise humana e model cards;
- aplicar PEFT/LoRA, entender RLHF/DPO e decidir entre prompting, RAG e fine-tuning;
- raciocinar sobre scaling laws, custo computacional, throughput, latência e memória;
- operar serving com KV cache, batching, quantization, speculative decoding e vLLM;
- projetar sistemas multimodais com representação, alinhamento, fusão e co-learning;
- defender tecnicamente um projeto de GenAI com benchmark, arquitetura, custo, riscos e limitações.

---

## Metodologia

O programa segue três camadas simultâneas:

1. **Teoria:** papers originais, matemática, arquitetura, objetivos de treino, avaliação e limitações.
2. **Implementação:** PyTorch, Hugging Face, tokenizers, PEFT, RAG, serving e experimentos reprodutíveis.
3. **Sistemas:** GPUs, memória, paralelismo, deployment, observability, custo, safety e operação.

Cada semana deve produzir evidência concreta: notebook, script, relatório, avaliação, mini-projeto ou design review.

---

## Workflow Semanal

| Bloco | Tempo | Saída |
|---|---:|---|
| Papers e teoria | 3-5h | notas técnicas com fórmulas, premissas e limitações |
| Implementação | 4-6h | código, notebook ou experimento reproduzível |
| Sistemas/avaliação | 2-3h | benchmark, profiling, evals ou análise de falhas |
| Revisão ativa | 1h | flashcards, mistake log e perguntas abertas |

---

## Definição de Sucesso

Uma semana está concluída quando você consegue:

- explicar o conceito sem depender de analogias vagas;
- implementar uma versão mínima ou reproduzir um pipeline oficial;
- medir qualidade, custo e limitação;
- apontar failure modes;
- relacionar o conteúdo ao projeto final;
- registrar decisões técnicas em notas auditáveis.

---

## Roadmap Macro

| Fase | Semanas | Tema | Milestone |
|---|---:|---|---|
| 1 | 1-4 | Pré-requisitos e fundamentos de LLMs | ambiente, matemática/NLP auditados, LM baseline |
| 2 | 5-12 | Transformers, dados, tokenization e avaliação | Transformer mínimo + data pipeline + evals |
| 3 | 13-20 | Prompting, PEFT, RAG, tool use e alignment | RAG/tool-use system avaliado |
| 4 | 21-28 | Scaling, training systems, inference e safety | benchmark de treino/inferência e design review |
| 5 | 29-36 | LLM systems | serving, embeddings, fine-tuning eficiente, observability |
| 6 | 37-44 | Multimodal ML | pipeline multimodal com avaliação |
| 7 | 45-48 | Capstone | defesa técnica research-engineering |

---

## Milestones

| Marco | Semana | Evidência |
|---|---:|---|
| Language model baseline | 4 | LM pequeno ou avaliação de LM existente |
| Transformer mínimo | 8 | implementação e teste de attention/decoder |
| Pretraining data pipeline | 10 | limpeza, deduplicação, tokenization e documentação |
| Evaluation harness | 12 | benchmark automatizado com métricas e model card |
| RAG/tool-use system | 18 | sistema com retrieval/tool calling e avaliação |
| Alignment decision memo | 20 | análise prompting vs RAG vs PEFT vs RLHF/DPO |
| Systems benchmark | 28 | profiling de memória, latência, throughput e custo |
| LLM serving design | 36 | arquitetura com vLLM/quantization/observability |
| Multimodal prototype | 44 | representação/fusão/alinhamento com eval |
| Capstone defense | 48 | relatório, demo, benchmark e defesa |

---

## Próximo Passo

Quando quiser gerar a primeira semana com arquivos também numerados, peça:

```txt
Generate Week 01
```
