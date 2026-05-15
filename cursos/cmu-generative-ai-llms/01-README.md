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

### Visão geral: 5 sessões por semana

Uma semana é composta de **4 a 5 sessões de 2–2.5h** cada. Nunca menos de 2h (não aquece), nunca mais de 3h seguidas (retorno marginal cai sensivelmente após esse ponto). Total: ~12h/semana.

```
Dia 1 │ Sessão 1: 01-theory.md                              [2.5h]
Dia 2 │ Sessão 2: 02-readings.md (papers obrigatórios)      [3h]
Dia 3 │ Sessão 3: 03-lab-guided.md + código                 [2.5h]
Dia 4 │ Sessão 4: 05-exercises.md (3 exercícios mínimos)    [2h]
Dia 5 │ Sessão 5: 07-assessment.md + protocolo de fechamento[2h]
```

---

### Sessão 1 — Teoria (2.5h)

**Abrir:** `modules/NN-week-NN/01-theory.md`

Leitura ativa — não passiva. Para cada seção principal:

1. Leia a seção inteira.
2. Feche o arquivo.
3. Escreva no papel (físico) a fórmula ou conceito central daquela seção — de memória.
4. Se não conseguir, releia. Compare.

**Ordem:** Contexto → Fundamentos formais → Arquitetura → Tradeoffs → Implementação de referência → Síntese.

Leia o código da **Implementação de referência** linha a linha. Para cada linha não óbvia, escreva no papel o que ela faz e *por que* aquela decisão foi tomada.

Ao final: abra `08-flashcards.md` e leia (apenas leia, sem active recall) os cards da categoria **Conceitos** para orientação do que vem pela frente.

**Sinal de sessão bem-feita:** você consegue escrever a fórmula central da semana e explicar a decisão de design principal sem consultar nada.

---

### Sessão 2 — Readings (2.5–3h)

**Abrir:** `modules/NN-week-NN/02-readings.md`

Leia as obrigatórias na ordem listada. Para cada paper:

- Leia com caneta/anotações digitais.
- Foque nas seções indicadas no roteiro (não leia o paper inteiro na primeira passagem).
- Após cada leitura, responda no papel as **perguntas de foco** listadas no `02-readings.md`. Se não conseguir responder uma pergunta, releia a seção relevante.

**Sinal de sessão bem-feita:** você consegue responder as perguntas de foco de cada reading sem consultar o paper.

---

### Sessão 3 — Lab Guiado (2.5h)

**Abrir em dois painéis:** `modules/NN-week-NN/03-lab-guided.md` (esquerda) + script de código (direita).

```bash
cd modules/NN-week-NN/code
pip install -r requirements.txt
python 01_environment_check.py
```

**Regra de ouro:** leia o passo do `03-lab-guided.md` antes de executar o código correspondente. Nunca execute sem ter lido a explicação — você está executando para confirmar um entendimento, não para descobrir o que acontece.

Se um passo produz `FAIL` ou output inesperado: **pare**. Não avance com resultado errado. Consulte a seção Troubleshooting do passo atual.

Ao final: preencha `assets/NN-lab-report.md` com os valores reais medidos. Sem números reais, o lab não está concluído.

Estude os cards de **Fórmulas** do `08-flashcards.md` ao final desta sessão.

---

### Sessão 4 — Exercícios (2h)

**Abrir:** `modules/NN-week-NN/05-exercises.md`

Selecione no mínimo 3 exercícios. O exercício de **debugging** é sempre obrigatório. Tente cada exercício sem consultar nada por 20–30 minutos. Se travado após 30 minutos, consulte a seção relevante do `01-theory.md` — mas não busque a solução diretamente.

Escreva o entregável no local especificado (`code/exercises/` ou `assets/`). Verifique os critérios de pass listados.

Ao final: estude os cards de **Arquitetura** e **Pitfalls** do `08-flashcards.md` em active recall (cubra o verso, responda, revele).

---

### Sessão 5 — Assessment + Fechamento (2h)

**Parte 1 — Assessment (1h15):**

```
Abrir: modules/NN-week-NN/07-assessment.md
```

Feche todos os outros arquivos. Configure um timer de **1 hora**. Responda todas as questões como exame real — sem consultar nada. Ao fim do timer, abra as rubricas e model answers. Para cada questão: aplique a rubrica, anote o nível (A+/A/B/C/F) e o que especificamente você acertou e errou.

**Parte 2 — Protocolo de fechamento da semana (45min):**

**① Lab report:** `assets/NN-lab-report.md` com todos os campos preenchidos com valores reais. Sem aproximações.

**② Gaps pessoais:** se ficou abaixo de A em ≥ 2 questões do assessment, registre o gap:
```
assets/gaps-pessoais.md
→ "SNN: [Q?] — gap em [tópico] — rever [seção do theory.md]"
```

**③ Flashcards — deck completo:** todos os cards da semana em active recall. Marque os que errou para revisão espaçada mais frequente. Se usa Anki, importe agora.

**④ Coverage matrix:**
```
Abrir: coverage-matrix.md
→ Confirmar que a linha da semana está ✓ coberto (ou ⚠ raso se você identificou gap)
```

**⑤ Mini-project:** confirmar que `assets/mini-project-report.md` existe com entregável mínimo. Se não, é débito técnico — complete antes de avançar.

---

### Regra de avanço

**Não passe para S+1 sem:**

- [ ] `assets/NN-lab-report.md` preenchido com métricas reais (não estimadas).
- [ ] Assessment com nota média ≥ B — você entende os fundamentos, mesmo que incompleto em detalhes.
- [ ] Todos os 20 flashcards revisados pelo menos uma vez em active recall.
- [ ] Mini-project com entregável mínimo funcionando.
- [ ] Linha da semana em `coverage-matrix.md` atualizada (não `⏳ pendente`).

Se não bateu o critério: **repita a sessão fraca**, não a semana toda.
Gap em teoria → refaça a Sessão 1. Gap no lab → refaça a Sessão 3. Gap em conceitos do assessment → releia a seção específica do `01-theory.md` e refaça as questões correspondentes.

---

### O que o estudo parece "por dentro"

Este kit não é MOOC — você não consome passivamente. Cada sessão produz um artefato:

| Sessão | Artefato produzido |
|---|---|
| Teoria | Fórmulas escritas à mão; síntese sem consulta |
| Readings | Respostas às perguntas de foco de cada paper |
| Lab | `assets/NN-lab-report.md` com números reais medidos |
| Exercícios | Código em `code/exercises/` + análise em `assets/` |
| Assessment | Rubrica auto-aplicada com nível por questão + gaps registrados |

Se você chegou ao fim da semana sem nenhum desses artefatos, você leu — mas não estudou.

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
