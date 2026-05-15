# CMU — Generative AI & Large Language Models
## Kit Autodidata

> **Aviso de não-oficialidade:** Este kit é material autodidata produzido por IA a partir de fontes públicas. Não é afiliado, endossado, revisado ou aprovado pela Carnegie Mellon University. Todo conteúdo original pertence à CMU e seus professores. Para o programa oficial, consulte [cmu.edu/online/gai-llm](https://www.cmu.edu/online/gai-llm/).

---

## Sobre o programa de referência

O **Online Graduate Certificate in Generative AI & Large Language Models** da Carnegie Mellon University (School of Computer Science / Language Technologies Institute) é um programa de 12 meses composto por três cursos graduados sequenciais: **LLMs Methods & Applications (11-967)** → **LLM Systems (11-968)** → **Multimodal Machine Learning (11-977)**. O programa é leccionado por professores do LTI incluindo Daphne Ippolito, Fernando Diaz, Lei Li, LP Morency, Yonatan Bisk e Graham Neubig. Custo oficial: US$25.452.

O programa cobre o stack completo de LLMs verticalmente: fundamentos algorítmicos → infraestrutura de sistemas distribuídos → multimodalidade. Público-alvo declarado: engenheiros e cientistas com background sólido em CS e ML que buscam compreensão técnica profunda, não introdução a APIs.

Fontes primárias: [cmu.edu/online/gai-llm](https://www.cmu.edu/online/gai-llm/) | [2025.cmu-llms.org](https://2025.cmu-llms.org/) | [llmsystem.github.io](https://llmsystem.github.io/) | [cmu-mmml.github.io](https://cmu-mmml.github.io/)

---

## Filosofia pedagógica

**Engineering-heavy com orientação a research engineering**, organizado em stack vertical de três cursos. Evidências: (1) 11-967: 4/6 assignments exigem implementação PyTorch/HuggingFace — Assignment #2 constrói transformer do zero, #3 implementa RAG com tool use, #4 otimiza eficiência de treinamento; bibliografia ≈80% papers arXiv/ACL/NeurIPS + ≈15% docs oficiais, <5% livro-texto. (2) 11-968: inteiramente dedicado a GPU programming e distributed systems — sem cases empresariais; leituras incluem DeepSpeed/ZeRO, FlashAttention, PagedAttention, SGLang. (3) 11-977: único com formalismo matemático denso (CCA, tensor fusion, mutual information) — research-heavy dentro do trio. Sequência didática: implementação antes da teoria formal. Avaliação: implementação (40%) + exames (40%) + mini-project (20%). Zero business cases. Perfil de egresso: research engineer / LLM systems engineer.

---

## Parâmetros do kit

| Parâmetro | Valor |
|---|---|
| Duração total | 48 semanas (3 módulos × 16 semanas) |
| Carga semanal alvo | ~12h (faixa: 10–14h por complexidade) |
| Carga total estimada | ~576h |
| Proporção teoria/engenharia | 40% teoria + readings / 60% lab + engenharia |
| Stack | Python 3.11+, PyTorch 2.x, HuggingFace Transformers, CUDA/Triton, vLLM |
| Ambiente de execução | Cloud GPU recomendado (Colab Pro+, AWS `g4dn.xlarge`, Lambda Cloud A10); labs leves rodam em CPU |
| Idioma de saída | pt-BR (texto explicativo) + English (código, termos técnicos, papers) |
| Background assumido | ML fundamentals; álgebra linear; probabilidade; Python fluente; PyTorch básico |

---

## Objetivos finais

Ao concluir o kit, o aluno será capaz de:

1. Implementar e treinar modelos de linguagem neurais do zero em PyTorch, incluindo tokenização, arquitetura transformer e objectives de pré-treinamento.
2. Realizar fine-tuning e inferência com modelos pré-treinados (BERT, T5, GPT, LLaMA) via HuggingFace.
3. Aplicar PEFT/LoRA, RLHF e DPO a tarefas concretas com comparação quantitativa a baselines.
4. Construir pipelines RAG com retrieval denso (FAISS) e tool use.
5. Ler e criticar papers modernos de LLMs com vocabulário técnico preciso (contribuição, limitações, reprodutibilidade).
6. Projetar e implementar sistemas de treinamento distribuído (pipeline, tensor e data parallelism; ZeRO).
7. Otimizar serving com FlashAttention, vLLM/PagedAttention, quantização INT8/INT4 e speculative decoding.
8. Descrever formalmente os 6 desafios de multimodal ML e implementar pipelines vision-language (CLIP, BLIP, LLaVA).
9. Avaliar modelos em benchmarks reconhecidos (HELM, BIG-Bench, Chatbot Arena, COCO captioning).
10. Defender escolhas arquiteturais e de sistema com o vocabulário técnico de um LTI/CMU graduate.

---

## Metodologia: 4 camadas por semana

| Camada | Arquivos | Propósito |
|---|---|---|
| **1. Teoria** | `01-theory.md` | Conceitos formais, matemática, derivações — nível de lecture/paper |
| **2. Leituras** | `02-readings.md` | Papers, docs e lecture notes anotados; roteiro de leitura estruturado |
| **3. Engenharia** | `03-lab-guided.md` + `04-lab-speedrun.md` | Implementação guiada + re-execução autônoma sem scaffolding |
| **4. Produção intelectual** | `05-exercises.md` + `06-mini-project.md` + `07-assessment.md` + `08-flashcards.md` | Exercícios técnicos, entrega incremental, autoavaliação, retenção espaçada |

---

## Workflow semanal

```
Início da semana:
  01-theory.md          → leitura ativa + anotações (2h)
  02-readings.md        → papers com roteiro de anotação (3h)

Meio da semana:
  03-lab-guided.md      → implementação passo a passo (2.5h)
  04-lab-speedrun.md    → re-execução autônoma (1.5h)

Final da semana:
  05-exercises.md       → exercícios técnicos (1h)
  06-mini-project.md    → entrega incremental do projeto (1h)
  07-assessment.md      → rubrica de autoavaliação
  08-flashcards.md      → revisão espaçada (0.5h)
```

**Regra de avanço (não avance para S+1 sem):**
- [ ] Lab `03-` + `04-` executado sem erros críticos.
- [ ] Rubrica `07-assessment.md` preenchida com ≥80% dos critérios `✓`.
- [ ] Deliverable da semana registrado no `coverage-matrix.md`.
- [ ] Flashcards `08-` adicionados ao deck de revisão espaçada.

---

## Roadmap macro

| Módulo | Semanas | Conteúdo | Milestone |
|---|---|---|---|
| M1 — LLMs Methods & Applications (11-967) | S01–S16 | Transformer → Fine-tuning → RAG → RLHF → Agents | **S16:** Transformer do zero + RAG funcional + mini-project M1 |
| M2 — LLM Systems (11-968) | S17–S32 | GPU programming → Distributed training → Serving → Quantização | **S32:** Pipeline distribuído + vLLM serving + projeto M2 |
| M3 — Multimodal ML (11-977) | S33–S48 | Unimodal repr. → Alignment → Generation → Embodied AI | **S48:** Capstone sistema vision-language ponta a ponta |

Detalhamento semana a semana: → [03-study-plan.md](03-study-plan.md)
Tabela de mapeamento ao syllabus: → [04-weekly-roadmap.md](04-weekly-roadmap.md)
Rastreabilidade de cobertura: → [coverage-matrix.md](coverage-matrix.md)
Glossário técnico: → [05-glossary.md](05-glossary.md)
Mapas conceituais: → [06-concept-map.md](06-concept-map.md)
