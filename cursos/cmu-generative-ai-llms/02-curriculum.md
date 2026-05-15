# 02 — Curriculum — CMU Generative AI & Large Language Models

Este arquivo reorganiza o currículo do certificado CMU em uma sequência autodidata de 12 meses. A fonte local usada foi `kit-estudo-especializacao/curriculum-source/curriculum-cmu.md`.

---

## Fontes Oficiais e Complementares

- CMU Generative AI & Large Language Models: <https://www.cmu.edu/online/generative-ai-llms>
- Syllabus público 2025: <https://2025.cmu-llms.org/syllabus/>
- Schedule público 2025: <https://2025.cmu-llms.org/schedule/>
- Assignments públicos 2025: <https://2025.cmu-llms.org/assignments/>

---

## Estrutura Oficial do Certificado

| Ordem | Curso | Código | Período publicado | Papel curricular |
|---:|---|---|---|---|
| 1 | Large Language Models: Methods and Applications | 11-967 | Fall 2026 | métodos, aplicações, avaliação, fine-tuning, RAG e alignment |
| 2 | Large Language Model Systems | 11-968 | Spring 2027 | treino, serving, fine-tuning eficiente, avaliação e operação em escala |
| 3 | Multimodal Machine Learning | 11-977 | Fall 2027 | representação, alinhamento, fusão e aplicações multimodais |

---

## Pré-Requisitos

### Obrigatórios para estudar com profundidade

- Machine Learning formal.
- NLP introdutório.
- Python fluente.
- PyTorch operacional.
- Álgebra linear, cálculo, otimização, probabilidade e estatística.
- Estruturas de dados, algoritmos, complexidade, sistemas operacionais e sistemas distribuídos.
- Familiaridade com GPU/cloud é recomendada para labs avançados.

### Diagnóstico inicial recomendado

Antes da Semana 01, valide:

- implementar uma regressão logística e um MLP simples;
- explicar matriz, tensor, gradiente, softmax e cross-entropy;
- usar PyTorch tensors, autograd, Dataset/DataLoader;
- explicar tokenization, embeddings e sequence modeling;
- usar shell, Git, ambientes Python e notebooks.

---

## Módulo 1 — Large Language Models: Methods and Applications

**Nível:** fundamentos até research-level  
**Dependências:** ML, NLP, Python, PyTorch, probabilidade e deep learning  
**Base oficial:** `11-967`; complemento público `11-667 / Fall 2025`

### 1. Building Blocks of Modern LLMs

**Nível:** fundamentos  
**Conteúdo:** language modeling, distributions over sequences, embeddings, neural LMs, perplexity, next-token prediction.  
**Entregável:** LM baseline e relatório de avaliação.

### 2. Transformer Architecture and Pretraining Objectives

**Nível:** fundamentos/intermediário  
**Conteúdo:** self-attention, multi-head attention, residuals, layer norm, positional encoding, encoder/decoder, causal masks, BERT/T5/GPT objectives.  
**Entregável:** implementação mínima de attention/decoder em PyTorch.

### 3. Pretraining Data Curation and Tokenization

**Nível:** intermediário  
**Conteúdo:** web-scale data, C4, ClueWeb, filtering, deduplication, diversity, contamination, BPE/tokenizers.  
**Entregável:** pipeline de limpeza/tokenização com datasheet.

### 4. Architecture Advances

**Nível:** intermediário/avançado  
**Conteúdo:** activation functions, normalization variants, grouped-query attention, RoPE, modern decoder-only refinements.  
**Entregável:** comparação controlada de variantes arquiteturais pequenas.

### 5. Evaluation of LLMs

**Nível:** intermediário/avançado  
**Conteúdo:** GEM, BIG-Bench, HELM, benchmark design, contamination, robustness, human evaluation.  
**Entregável:** evaluation harness com métricas automáticas e análise crítica.

### 6. In-Context Learning, Fine-Tuning and PEFT

**Nível:** avançado  
**Conteúdo:** prompting, few-shot learning, prompt tuning, adapters, LoRA, PEFT, task-oriented fine-tuning.  
**Entregável:** comparação prompting vs PEFT em tarefa pequena.

### 7. Reasoning, Human-AI Interaction and Alignment Behaviors

**Nível:** avançado/research-level  
**Conteúdo:** Chain-of-Thought, reasoning benchmarks, human-agent interaction, adversarial alignment, model behavior.  
**Entregável:** relatório de falhas e avaliação humana estruturada.

### 8. Tool Use and Retrieval-Augmented Generation

**Nível:** avançado  
**Conteúdo:** Toolformer, function/tool calling, dense retrieval, RAG, Self-RAG, trust and grounding.  
**Entregável:** sistema RAG/tool-use com avaliação de retrieval e resposta.

### 9. Scaling Laws, Optimization and Parallel Training

**Nível:** research-level  
**Conteúdo:** scaling laws, Chinchilla, Adam, GPipe, DeepSpeed, data/model/pipeline parallelism.  
**Entregável:** design memo de treino escalável e benchmark pequeno.

### 10. Interpretability, Safety, Bias and Attacks

**Nível:** research-level  
**Conteúdo:** interpretability methods, red-teaming, benchmark leakage, extraction attacks, bias and ethical issues.  
**Entregável:** threat model e safety evaluation.

### 11. RLHF, DPO and Efficient Inference

**Nível:** research-level  
**Conteúdo:** preference learning, RLHF, DPO, speculative decoding, FlashAttention, PagedAttention, KV cache.  
**Entregável:** análise alignment + benchmark de inferência.

### 12. Agents, Long Context, Sparse Models and Synthetic Data

**Nível:** research-level  
**Conteúdo:** agents, Chatbot Arena, long-context failure modes, MoE, Switch Transformer, MatFormer, synthetic data.  
**Entregável:** mini-project ou proposal de capstone.

---

## Módulo 2 — Large Language Model Systems

**Nível:** avançado/research-level  
**Dependências:** LLM methods, sistemas distribuídos, GPU, PyTorch, avaliação

### 13. Training Systems

**Conteúdo:** clusters GPU, memory hierarchy, mixed precision, checkpointing, gradient accumulation, parallel training.  
**Entregável:** profiling de treino pequeno e design de escala.

### 14. Serving Systems

**Conteúdo:** batching, KV cache, PagedAttention, vLLM, throughput/latency tradeoffs, SLOs.  
**Entregável:** benchmark de serving.

### 15. Efficient Fine-Tuning and Compression

**Conteúdo:** LoRA, QLoRA, quantization, pruning, distillation, adapters.  
**Entregável:** fine-tuning ou simulação reprodutível com restrições de hardware.

### 16. Embedding Storage and Retrieval Systems

**Conteúdo:** vector databases, ANN indexes, HNSW/IVF, reranking, freshness, corpus monitoring.  
**Entregável:** retrieval service com avaliação.

### 17. Online Maintenance and Observability

**Conteúdo:** drift, evals contínuos, logging, feedback loops, safety monitoring, rollback.  
**Entregável:** runbook operacional de LLM system.

---

## Módulo 3 — Multimodal Machine Learning

**Nível:** avançado/research-level  
**Dependências:** deep learning, representation learning, vision/NLP, optimization

### 18. Multimodal Representation

**Conteúdo:** joint embeddings, contrastive learning, CLIP, modality-specific encoders.  
**Entregável:** embedding multimodal e retrieval básico.

### 19. Translation and Alignment

**Conteúdo:** image captioning, text-to-image alignment, cross-modal matching, attention.  
**Entregável:** avaliação de alignment.

### 20. Fusion and Co-Learning

**Conteúdo:** early/late fusion, attention fusion, co-training, missing modalities.  
**Entregável:** pipeline com ablação por modalidade.

### 21. Multimodal Applications

**Conteúdo:** affect recognition, video captioning, cross-modal retrieval, VLMs.  
**Entregável:** protótipo multimodal com model card.

---

## Projeto Final

**Nível:** research-ready  
**Requisitos:**

- problema tecnicamente relevante;
- baseline forte;
- implementação real;
- avaliação quantitativa e qualitativa;
- análise de custo computacional;
- análise de failure modes;
- documentação reprodutível;
- defesa técnica.

---

## Mapa de Dependências

| Tópico | Depende de | Nível |
|---|---|---|
| Language modeling | probabilidade, NLP, Python | fundamentos |
| Transformers | deep learning, álgebra linear, attention | fundamentos/intermediário |
| Pretraining data | data engineering, NLP, tokenization | intermediário |
| Evaluation | estatística, benchmarks, métricas NLP | intermediário |
| PEFT / LoRA | PyTorch, Transformers, otimização | avançado |
| RAG / tool use | embeddings, retrieval, prompting | avançado |
| Scaling laws | estatística empírica, compute, optimization | research-level |
| Parallel training | GPU, distributed systems, PyTorch | research-level |
| RLHF / DPO | preferences, RL, alignment | research-level |
| Efficient inference | KV cache, batching, kernels, serving | research-level |
| MoE / sparse models | routing, distributed systems, evaluation | research-level |
| Multimodal learning | vision, NLP, representation learning | research-level |
