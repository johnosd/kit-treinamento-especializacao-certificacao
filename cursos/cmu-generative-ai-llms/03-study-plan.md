# 03 — Study Plan — 48 Semanas

Plano autodidata de 12 meses baseado no certificado CMU e nos complementos públicos de LLMs. Carga sugerida: **10-15h/semana**. Proporção: **60% engenharia / 40% teoria**.

---

## Rotina Semanal

| Bloco | Tempo | Evidência |
|---|---:|---|
| Papers e teoria | 3-5h | notas com contribuição, limitação, fórmula e crítica |
| Implementação | 4-6h | notebook/script reproduzível |
| Avaliação/sistemas | 2-3h | benchmark, profiling, eval ou design review |
| Active recall | 1h | flashcards e mistake log |

---

## Fase 1 — Pré-Requisitos e Language Modeling

### Semana 01 — Diagnóstico Técnico e Setup

- **Teoria:** revisar ML, NLP, PyTorch, probabilidade e autograd.
- **Leitura:** syllabus CMU 2025, PyTorch basics, Hugging Face quicktour.
- **Implementação:** ambiente Python/PyTorch, GPU check, repositório e template de experimento.
- **Lab:** reproduzir pipeline mínimo de tokenização e tensorização.
- **Mini-projeto:** diagnóstico de gaps e plano de remediação.
- **Assessment:** explicar cross-entropy, softmax, perplexity e next-token prediction.

### Semana 02 — Language Modeling

- **Teoria:** distribuições sobre sequências, n-grams, neural LMs, perplexity.
- **Leitura:** Jurafsky & Martin LM chapter.
- **Implementação:** LM simples ou avaliação de LM pequeno.
- **Lab:** calcular perplexity e analisar erros.
- **Mini-projeto:** relatório de baseline.
- **Assessment:** limitações de perplexity.

### Semana 03 — Embeddings e Tokenization

- **Teoria:** subwords, BPE, WordPiece, unigram, vocabulary tradeoffs.
- **Leitura:** Hugging Face tokenizers docs.
- **Implementação:** treinar tokenizer pequeno e comparar fragmentação.
- **Lab:** analisar impacto por idioma/domínio.
- **Mini-projeto:** tokenizer report.
- **Assessment:** custo e viés de tokenização.

### Semana 04 — PyTorch Deep Learning Refresher

- **Teoria:** tensors, autograd, modules, optimizers, dataloaders.
- **Leitura:** PyTorch tutorials.
- **Implementação:** treino de rede pequena com logging.
- **Lab:** debugging de shapes e gradients.
- **Mini-projeto:** training loop limpo.
- **Assessment:** explicar backward pass e optimizer step.

---

## Fase 2 — Transformers, Dados e Avaliação

### Semanas 05-06 — Transformer Core

- **Teoria:** self-attention, masks, MHA, layer norm, residuals, positional encoding.
- **Leitura:** Attention Is All You Need.
- **Implementação:** self-attention e bloco decoder em PyTorch.
- **Lab:** visualizar atenção e custo O(n²).
- **Mini-projeto:** Transformer mínimo com testes.
- **Assessment:** tradeoffs arquiteturais.

### Semanas 07-08 — Pretraining Objectives e Arquiteturas

- **Teoria:** causal LM, masked LM, seq2seq, BERT/T5/GPT.
- **Leitura:** BERT, T5, GPT-3.
- **Implementação:** inferência com modelos Hugging Face.
- **Lab:** comparar objetivos em tarefas downstream.
- **Mini-projeto:** architecture comparison memo.
- **Assessment:** escolher arquitetura por tarefa.

### Semanas 09-10 — Pretraining Data

- **Teoria:** web data, filtering, dedup, contamination, data governance.
- **Leitura:** Documenting C4; ClueWeb22; data commons.
- **Implementação:** pipeline pequeno de limpeza e deduplicação.
- **Lab:** datasheet for dataset.
- **Mini-projeto:** pretraining-data audit.
- **Assessment:** riscos de dados em LLMs.

### Semanas 11-12 — Evaluation Harness

- **Teoria:** automatic evals, benchmark design, HELM, BIG-Bench, human eval.
- **Leitura:** HELM, BIG-Bench, GEM.
- **Implementação:** harness de avaliação para prompts/modelos.
- **Lab:** contaminação e robustez.
- **Mini-projeto:** model card.
- **Assessment:** por que benchmark único é fraco.

---

## Fase 3 — Adaptation, RAG, Tool Use e Alignment

### Semanas 13-14 — Prompting e In-Context Learning

- **Teoria:** zero/few-shot, CoT, structured outputs, prompt sensitivity.
- **Leitura:** Chain-of-Thought, in-context learning papers.
- **Implementação:** prompt benchmark com versões.
- **Lab:** avaliação humana e automática.
- **Mini-projeto:** prompt eval report.
- **Assessment:** quando prompting falha.

### Semanas 15-16 — Fine-Tuning, PEFT e LoRA

- **Teoria:** full fine-tuning, adapters, LoRA, QLoRA, catastrophic forgetting.
- **Leitura:** LoRA, QLoRA, PEFT docs.
- **Implementação:** PEFT pequeno ou simulação com modelo reduzido.
- **Lab:** comparar prompting vs PEFT.
- **Mini-projeto:** adaptation decision memo.
- **Assessment:** custo/benefício de fine-tuning.

### Semanas 17-18 — Tool Use e RAG

- **Teoria:** retrieval, dense retrievers, reranking, grounding, Toolformer.
- **Leitura:** RAG, Self-RAG, Toolformer.
- **Implementação:** RAG com corpus local e tool simples.
- **Lab:** retrieval precision, answer quality, citation checks.
- **Mini-projeto:** RAG/tool-use system.
- **Assessment:** diagnosticar falha de retrieval vs geração.

### Semanas 19-20 — Alignment, RLHF e DPO

- **Teoria:** preference data, reward models, PPO, DPO, instruction tuning.
- **Leitura:** InstructGPT, DPO.
- **Implementação:** experimento pequeno com preference scoring ou estudo reprodutível.
- **Lab:** rubrica de preferência e análise de viés.
- **Mini-projeto:** alignment risk memo.
- **Assessment:** RLHF vs DPO vs SFT.

---

## Fase 4 — Scaling, Safety e Efficient Inference

### Semanas 21-22 — Scaling Laws

- **Teoria:** scaling laws, Chinchilla, compute/data/model tradeoffs.
- **Leitura:** Kaplan scaling laws, Chinchilla.
- **Implementação:** simulação/ajuste de curvas em dados sintéticos ou públicos.
- **Lab:** compute-optimal reasoning.
- **Mini-projeto:** scaling memo.
- **Assessment:** limites de extrapolação.

### Semanas 23-24 — Optimization and Parallel Training

- **Teoria:** Adam, mixed precision, data/model/pipeline parallelism, GPipe, DeepSpeed.
- **Leitura:** GPipe, DeepSpeed, Megatron-LM.
- **Implementação:** profiling de treino pequeno.
- **Lab:** gradient accumulation, checkpointing.
- **Mini-projeto:** distributed training design.
- **Assessment:** gargalos de memória/comunicação.

### Semanas 25-26 — Interpretability, Bias and Attacks

- **Teoria:** interpretability, red-teaming, extraction, benchmark leakage, bias.
- **Leitura:** red-teaming, extraction attacks, interpretability readings.
- **Implementação:** avaliação adversarial e leakage checklist.
- **Lab:** prompt injection e safety eval.
- **Mini-projeto:** threat model.
- **Assessment:** segurança vs usabilidade.

### Semanas 27-28 — Efficient Inference, Long Context and Sparse Models

- **Teoria:** KV cache, FlashAttention, PagedAttention, speculative decoding, long context, MoE.
- **Leitura:** FlashAttention, PagedAttention, Switch Transformer.
- **Implementação:** benchmark de geração e memória.
- **Lab:** análise de latência/throughput.
- **Mini-projeto:** inference optimization report.
- **Assessment:** quando quantization ou MoE compensa.

---

## Fase 5 — LLM Systems

### Semanas 29-30 — Serving Architecture

- **Teoria:** SLOs, batching, routing, rate limits, caching, autoscaling.
- **Leitura:** vLLM docs, Ray Serve docs.
- **Implementação:** servidor local ou simulado de inferência.
- **Lab:** medir latência p50/p95 e throughput.
- **Mini-projeto:** serving design doc.
- **Assessment:** tradeoffs batch vs latency.

### Semanas 31-32 — Embedding and Retrieval Systems

- **Teoria:** vector DBs, HNSW/IVF, reranking, freshness, corpus drift.
- **Leitura:** FAISS, vector DB docs.
- **Implementação:** índice vetorial e avaliação.
- **Lab:** recall@k e latency.
- **Mini-projeto:** retrieval service.
- **Assessment:** métricas de retrieval.

### Semanas 33-34 — Efficient Adaptation and Compression

- **Teoria:** quantization, distillation, pruning, LoRA/QLoRA em produção.
- **Leitura:** QLoRA, PyTorch quantization.
- **Implementação:** comparação de precisão/custo.
- **Lab:** memory footprint report.
- **Mini-projeto:** compression decision memo.
- **Assessment:** regressões de qualidade por compressão.

### Semanas 35-36 — Observability and Online Maintenance

- **Teoria:** evals contínuos, logging, drift, feedback loops, governance.
- **Leitura:** OpenAI evals, ML observability references.
- **Implementação:** logging schema e dashboard simples.
- **Lab:** runbook de rollback e incident response.
- **Mini-projeto:** LLM ops runbook.
- **Assessment:** monitorar qualidade sem violar privacidade.

---

## Fase 6 — Multimodal Machine Learning

### Semanas 37-38 — Multimodal Representation

- **Teoria:** joint embeddings, contrastive learning, CLIP.
- **Leitura:** Multimodal ML survey, CLIP.
- **Implementação:** retrieval imagem-texto com modelo pré-treinado.
- **Lab:** avaliar similaridade e falhas.
- **Mini-projeto:** multimodal embedding report.
- **Assessment:** alignment vs correlation.

### Semanas 39-40 — Translation and Alignment

- **Teoria:** image captioning, cross-modal mapping, attention.
- **Leitura:** Show Attend and Tell, BLIP-2.
- **Implementação:** captioning ou VLM inference.
- **Lab:** avaliação qualitativa e quantitativa.
- **Mini-projeto:** alignment eval.
- **Assessment:** hallucination multimodal.

### Semanas 41-42 — Fusion and Co-Learning

- **Teoria:** early/late fusion, missing modalities, co-learning.
- **Leitura:** multimodal fusion references.
- **Implementação:** modelo de fusão simples com ablação.
- **Lab:** medir contribuição por modalidade.
- **Mini-projeto:** ablation report.
- **Assessment:** robustez a modalidade ausente.

### Semanas 43-44 — Multimodal Applications

- **Teoria:** affect recognition, video captioning, cross-modal retrieval, VLM safety.
- **Leitura:** VLM papers recentes.
- **Implementação:** protótipo multimodal.
- **Lab:** model card multimodal.
- **Mini-projeto:** aplicação multimodal avaliada.
- **Assessment:** riscos éticos e operacionais.

---

## Fase 7 — Capstone

### Semana 45 — Proposal

- **Teoria:** pergunta de pesquisa/aplicação, baseline, métrica e escopo.
- **Implementação:** proposta técnica.
- **Assessment:** design review.

### Semana 46 — Implementation

- **Teoria:** execução controlada, experiment tracking, avaliação.
- **Implementação:** sistema mínimo completo.
- **Assessment:** debugging review.

### Semana 47 — Benchmark and Report

- **Teoria:** análise de resultados, custo, failure modes.
- **Implementação:** benchmark final e relatório.
- **Assessment:** crítica técnica.

### Semana 48 — Defense

- **Teoria:** síntese, defesa, limitações e trabalhos futuros.
- **Implementação:** demo e apresentação.
- **Assessment:** banca simulada.
