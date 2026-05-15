# Plano de Estudos Detalhado — CMU Generative AI & LLMs Kit

> 48 semanas × ~12h/semana ≈ 576h totais.
> Carga por camada é estimativa — ajuste conforme velocidade pessoal.
> **Regra de avanço:** não passe para S+1 sem: lab executado sem erros críticos + rubrica `07-assessment.md` ≥80% `✓` + deliverable registrado no `coverage-matrix.md`.

---

## Módulo 1 — LLMs Methods & Applications (S01–S16)

---

### S-01 — Building Blocks of Modern LLMs
> M1 | fundamentos | core | Map: 11-667 W01 | Dep: —

| Camada | Atividade | h |
|---|---|---|
| Teoria | Transformer architecture; self-attention; positional encoding; pre-training objectives (CLM, MLM) | 2.5h |
| Readings | Vaswani et al. 2017 (Attention is All You Need); Devlin et al. 2019 (BERT) | 3h |
| Lab | Implementar self-attention 1-layer em NumPy; comparar com `nn.MultiheadAttention` | 2.5h |
| Exercícios+Assess | Derivar gradiente da atenção à mão; rubrica `07-assessment.md` | 1.5h |
| Revisão | Flashcards: transformer components, attention formula, pre-training objectives | 0.5h |
| **Total** | | **~10h** |

**Deliverable:** Self-attention 1-layer (NumPy) vs `nn.MultiheadAttention` — output idêntico verificado.

---

### S-02 — Pre-training Data + Tokenization + Arch Advances
> M1 | fundamentos | core | Map: 11-667 W02 | Dep: S01

| Camada | Atividade | h |
|---|---|---|
| Teoria | BPE/WordPiece/SentencePiece; GQA; RoPE; RMSNorm vs LayerNorm; data curation pipelines | 2.5h |
| Readings | Kudo & Richardson 2018 (SentencePiece); Su et al. 2021 (RoPE); Ainslie et al. 2023 (GQA) | 3h |
| Lab | BPE tokenizer custom treinado em corpus de domínio; vocab size ablação | 2.5h |
| Exercícios+Assess | Comparar vocabulários BPE vs WordPiece; rubrica | 1.5h |
| Revisão | Flashcards: BPE algoritmo, RoPE formulação, GQA vs MHA | 0.5h |
| **Total** | | **~10h** |

**Deliverable:** BPE tokenizer custom em corpus domain com ablação de vocab size documentada.

---

### S-03 — Avaliação Automática + ICL + PEFT/LoRA
> M1 | intermediário | core | Map: 11-667 W03 | Dep: S01, S02

| Camada | Atividade | h |
|---|---|---|
| Teoria | BIG-Bench, HELM, MMLU; few-shot ICL; task-oriented fine-tuning; LoRA/PEFT teoria | 2.5h |
| Readings | Liang et al. 2022 (HELM); Hu et al. 2022 (LoRA); Brown et al. 2020 (GPT-3 ICL) | 3h |
| Lab | LoRA from scratch em PyTorch + HELM mini-evaluation em 2 benchmarks | 2.5h |
| Exercícios+Assess | Calcular trainable params LoRA vs full FT; rubrica | 1.5h |
| Revisão | Flashcards: LoRA rank/alpha, ICL template design, HELM scenarios | 0.5h |
| **Total** | | **~10h** |

**Deliverable:** LoRA from scratch + HELM mini-evaluation com tabela comparativa.

---

### S-04 — Reasoning in LLMs + Human-Agent Evaluation
> M1 | intermediário | core | Map: 11-667 W04 | Dep: S03

| Camada | Atividade | h |
|---|---|---|
| Teoria | Chain-of-thought; evaluation malpractices; contamination; human-agent interaction design | 2.5h |
| Readings | Wei et al. 2022 (CoT); Bowman et al. 2021 (GHC); papers dos guest lecturers | 3h |
| Lab | Análise de contamination metodológica em benchmark escolhido (MMLU ou similar) | 2.5h |
| Exercícios+Assess | Identificar ≥3 malpractices no benchmark analisado; rubrica | 1.5h |
| Revisão | Flashcards: CoT tipos, evaluation threats, contamination detection | 0.5h |
| **Total** | | **~10h** |

**Deliverable:** Relatório de evaluation malpractices em benchmark escolhido (≥3 categorias).

---

### S-05 — ICL Behaviors + Alignment + Tool Use
> M1 | intermediário | core | Map: 11-667 W05 | Dep: S03, S04

| Camada | Atividade | h |
|---|---|---|
| Teoria | ICL surprising behaviors (label flipping, format sensitivity); RLHF overview; Constitutional AI; tool use / function calling | 2.5h |
| Readings | Min et al. 2022 (Rethinking ICL); Ouyang et al. 2022 (InstructGPT); Schick et al. 2023 (Toolformer) | 3h |
| Lab | Tool-calling agent com HuggingFace em ≥5 cenários (search, calculator, code exec) | 2.5h |
| Exercícios+Assess | Ablação de format sensitivity em 3 prompts; rubrica | 1.5h |
| Revisão | Flashcards: ICL mechanics, Constitutional AI steps, tool use schema | 0.5h |
| **Total** | | **~10h** |

**Deliverable:** Tool-calling agent (≥5 cenários) com log de chamadas e success rate.

---

### S-06 — RAG + Scaling Laws
> M1 | intermediário | core | Map: 11-667 W06 | Dep: S03, S05

| Camada | Atividade | h |
|---|---|---|
| Teoria | RAG pipeline (retriever + reader); dense retrieval (DPR); Chinchilla scaling laws; compute-optimal training | 2.5h |
| Readings | Lewis et al. 2020 (RAG); Hoffmann et al. 2022 (Chinchilla); Karpukhin et al. 2020 (DPR) | 3h |
| Lab | RAG pipeline com FAISS + HuggingFace benchmarked em TriviaQA (EM + F1) | 3h |
| Exercícios+Assess | Plot: tokens/compute vs loss em 3 model sizes; rubrica | 1h |
| Revisão | Flashcards: RAG componentes, Chinchilla formula, FAISS index types | 0.5h |
| **Total** | | **~10h** |

**Deliverable:** RAG pipeline (FAISS + HF) benchmarked em TriviaQA — EM e F1 documentados.

---

### S-07 — Parallel Training (Optimiz.) + Interpretability
> M1 | avançado | core | Map: 11-667 W07 | Dep: S01, S06

| Camada | Atividade | h |
|---|---|---|
| Teoria | Gradient accumulation; mixed precision (BF16/FP16); gradient checkpointing; attention patterns; probing; ROME | 2.5h |
| Readings | Micikevicius et al. 2018 (Mixed Precision); Meng et al. 2022 (ROME); Elhage et al. 2021 (Mathematical Framework) | 3.5h |
| Lab | Training script com gradient accumulation + torch.profiler report (compute/memory breakdown) | 3h |
| Exercícios+Assess | Identificar induction heads via attention visualization; rubrica | 1.5h |
| Revisão | Flashcards: gradient accumulation, loss scaling, probing tasks | 0.5h |
| **Total** | | **~12h** |

**Deliverable:** Training script com gradient accumulation + profiling report (flops, memory, throughput).

---

### S-08 — Revisão M1 (S01–S07) + Lab de Integração
> M1 | fundamentos | bridge | Map: 11-667 W08 (break) | Dep: S01–S07

| Camada | Atividade | h |
|---|---|---|
| Revisão M1 | Rever flashcards S01–S07; identificar gaps pessoais via coverage-matrix | 3h |
| Lab integrado | LoRA + RAG pipeline integrado: LoRA-fine-tuned retriever + generation | 4h |
| Documento de gaps | Lista de tópicos ≤80% no assessment; plano de reforço | 1.5h |
| Exercícios+Assess | Rubrica de integração (todos os componentes funcionais end-to-end) | 3h |
| **Total** | | **~11.5h** |

**Deliverable:** LoRA + RAG pipeline integrado funcionando + documento de gaps pessoais.

---

### S-09 — Bias, Ethics & Safety
> M1 | intermediário | core | Map: 11-667 W09 | Dep: S05, S08

| Camada | Atividade | h |
|---|---|---|
| Teoria | Bias em LLMs (demographic, stereotypical); toxicity; red-teaming metodologia; safety benchmarks | 2.5h |
| Readings | Weidinger et al. 2022 (Taxonomy of Risks); Perez et al. 2022 (Red Teaming); Bommasani et al. 2022 (Foundation Models) | 3h |
| Lab | Red-team report em modelo aberto: ≥5 categorias (jailbreak, toxicity, bias, privacy, misinformation) | 3h |
| Exercícios+Assess | Classificar 10 falhas por categoria; rubrica | 1h |
| Revisão | Flashcards: bias types, red-team taxonomy, safety techniques | 0.5h |
| **Total** | | **~10h** |

**Deliverable:** Red-team report (≥5 categorias) em modelo aberto com exemplos reprodutíveis.

---

### S-10 — LLM Security + Benchmark Leakage + RecSys
> M1 | avançado | core | Map: 11-667 W10 | Dep: S04, S09

| Camada | Atividade | h |
|---|---|---|
| Teoria | Prompt injection; membership inference; benchmark contamination detection; LLMs para RecSys | 2.5h |
| Readings | Carlini et al. 2021 (Extracting Training Data); Shi et al. 2023 (Detecting Pretraining Data); Zou et al. 2023 (Universal Adversarial Attacks) | 3h |
| Lab | Membership inference probe + contamination methodology demo em dataset público | 3h |
| Exercícios+Assess | Aplicar perplexity ratio test em 2 benchmarks; rubrica | 1h |
| Revisão | Flashcards: membership inference, contamination tests, prompt injection types | 0.5h |
| **Total** | | **~10h** |

**Deliverable:** Membership inference probe + contamination methodology demo documentado.

---

### S-11 — RLHF + DPO
> M1 | avançado | core | Map: 11-667 W11 | Dep: S05, S09

| Camada | Atividade | h |
|---|---|---|
| Teoria | RLHF pipeline (SFT → RM → PPO); reward hacking; DPO derivação e equivalência com RLHF | 2.5h |
| Readings | Ouyang et al. 2022 (InstructGPT); Rafailov et al. 2023 (DPO); Stiennon et al. 2020 (Learning to Summarize) | 3.5h |
| Lab | DPO-tuned GPT-2 em preference dataset; win-rate vs SFT baseline | 3h |
| Exercícios+Assess | Derivar DPO loss a partir do RLHF objective; rubrica | 1.5h |
| Revisão | Flashcards: RLHF stages, PPO objective, DPO formula | 0.5h |
| **Total** | | **~11h** |

**Deliverable:** DPO-tuned GPT-2 com win-rate vs SFT baseline documentado.

---

### S-12 — Efficient Inference + LLM Agents
> M1 | avançado | core | Map: 11-667 W12 | Dep: S05, S07

| Camada | Atividade | h |
|---|---|---|
| Teoria | KV cache; continuous batching; speculative decoding; LLM agent loops (ReAct, Reflexion) | 2.5h |
| Readings | Sheng et al. 2023 (FlexGen); Yao et al. 2022 (ReAct); Leviathan et al. 2023 (Speculative Decoding) | 3h |
| Lab | vLLM benchmark: tokens/s; latência P50/P95 por batch size (1, 4, 16, 64) | 3h |
| Exercícios+Assess | Comparar speculative vs autoregressive em latência; rubrica | 1h |
| Revisão | Flashcards: KV cache memory formula, continuous batching, ReAct loop | 0.5h |
| **Total** | | **~10h** |

**Deliverable:** vLLM benchmark — tokens/s, latência P50/P95 por batch size documentados.

---

### S-13 — Long-Context + Sparse Pretraining / MoE
> M1 | avançado | core | Map: 11-667 W13 | Dep: S01, S07, S12

| Camada | Atividade | h |
|---|---|---|
| Teoria | Attention para long context (ALiBi, Longformer); position bias; MoE routing; load balancing | 2.5h |
| Readings | Press et al. 2022 (ALiBi); Fedus et al. 2021 (Switch Transformer); Child et al. 2019 (Sparse Transformer) | 3.5h |
| Lab | Position bias plot (performance vs position) + MoE router com load balancing loss | 3h |
| Exercícios+Assess | Implementar top-2 routing; medir load imbalance; rubrica | 1.5h |
| Revisão | Flashcards: ALiBi, MoE routing formula, load balancing coefficient | 0.5h |
| **Total** | | **~11h** |

**Deliverable:** Position bias plot + MoE router com load balancing implementado.

---

### S-14 — Synthetic Data Training
> M1 | research | core | Map: 11-667 W14 | Dep: S03, S11

| Camada | Atividade | h |
|---|---|---|
| Teoria | Data augmentation via LLMs; self-instruct; constitutional AI data; ablação synthetic vs real | 2.5h |
| Readings | Wang et al. 2022 (Self-Instruct); Gunasekar et al. 2023 (Phi-1); Xu et al. 2023 (WizardLM) | 3.5h |
| Lab | Pipeline de dados sintéticos (self-instruct style) + ablação perplexity synthetic vs real data | 3.5h |
| Exercícios+Assess | Analisar quality metrics dos dados gerados; rubrica | 1h |
| Revisão | Flashcards: self-instruct pipeline, deduplication, quality filtering | 0.5h |
| **Total** | | **~11h** |

**Deliverable:** Pipeline de dados sintéticos + ablação synthetic vs real (perplexity + downstream accuracy).

---

### S-15 — Mini-Project M1 (implementação + escrita)
> M1 | research | core | Map: 11-667 W15 | Dep: S01–S14

| Camada | Atividade | h |
|---|---|---|
| Implementação | Projeto M1: tema livre dentro de M1 (ex: novel PEFT method, RAG evaluation, DPO ablation) | 6h |
| Relatório | Technical report 4–6 páginas: motivação, método, experimentos, resultados, limitações | 4h |
| Revisão final M1 | Atualizar coverage-matrix.md; identificar gaps pendentes | 1.5h |
| **Total** | | **~11.5h** |

**Deliverable:** Technical report 4–6 págs + código reprodutível (GitHub ou Colab).

---

### S-16 — Avaliação Final M1 + Retrospectiva
> M1 | research | core | Map: 11-667 W16 | Dep: S01–S15

| Camada | Atividade | h |
|---|---|---|
| Autoavaliação | Preencher coverage-matrix M1 completa; verificar ≥80% `✓ coberto` | 2h |
| Exam simulado | Questões de implementação + conceituais cobrindo S01–S15 (autodidata) | 4h |
| Retrospectiva | Documentar: o que ficou raso, próximos gaps para M2, ajustes de ritmo | 2h |
| Revisão espaçada | Flashcards M1 completo + deck consolidado | 2h |
| **Total** | | **~10h** |

**Deliverable:** coverage-matrix M1 preenchida com ≥80% `✓ coberto`.

---

## Módulo 2 — LLM Systems (S17–S32)

---

### S-17 — Intro a LLM Systems + GPU Architecture
> M2 | fundamentos | supplemented | Map: 11-868 tópico 1 | Dep: S16

| Camada | Atividade | h |
|---|---|---|
| Teoria | GPU memory hierarchy (HBM, L2, SRAM); compute vs memory bound; arithmetic intensity; roofline model | 2.5h |
| Readings | NVIDIA H100 whitepaper; Patterson et al. 2022 (Carbon footprint); llmsystem.github.io intro | 3h |
| Lab | Profiling report com `torch.profiler`: compute vs memory bound por operação (GEMM, LayerNorm, Softmax) | 3h |
| Exercícios+Assess | Calcular FLOP/byte ratio para transformer layer; rubrica | 1h |
| Revisão | Flashcards: roofline model, HBM bandwidth, FLOP/byte ratio | 0.5h |
| **Total** | | **~10h** |

**Deliverable:** Profiling report: compute vs memory bound por operação com roofline analysis.

---

### S-18 — CUDA Kernels + Autograd Implementation
> M2 | intermediário | supplemented | Map: 11-868 tópico 2 | Dep: S17

| Camada | Atividade | h |
|---|---|---|
| Teoria | CUDA thread hierarchy (thread/block/grid/warp); shared memory; tiled GEMM; custom autograd Function | 2.5h |
| Readings | Kirk & Hwu cap. 1-4 (Programming Massively Parallel Processors); CUDA Programming Guide (thread model) | 3.5h |
| Lab | CUDA GEMM naive → tiled; speedup vs cuBLAS documentado; custom autograd backward | 3.5h |
| Exercícios+Assess | Analisar occupancy e bank conflicts; rubrica | 1h |
| Revisão | Flashcards: CUDA memory hierarchy, warp divergence, tiling pattern | 0.5h |
| **Total** | | **~11h** |

**Deliverable:** CUDA GEMM naive → tiled com speedup vs cuBLAS documentado em tabela.

---

### S-19 — DL Frameworks + Transformer Systems
> M2 | intermediário | supplemented | Map: 11-868 tópico 3 | Dep: S17, S18

| Camada | Atividade | h |
|---|---|---|
| Teoria | Computation graphs; eager vs lazy execution; JIT compilation; operator fusion; TorchScript/torch.compile | 2.5h |
| Readings | PyTorch internals (Chintala); TorchScript docs; torch.compile PEP | 3h |
| Lab | Fused LayerNorm kernel (Triton ou CUDA); benchmarked vs `nn.LayerNorm` — latência/throughput | 3.5h |
| Exercícios+Assess | Trace computation graph de transformer forward; rubrica | 1.5h |
| Revisão | Flashcards: operator fusion, torch.compile modes, JIT tracing vs scripting | 0.5h |
| **Total** | | **~11h** |

**Deliverable:** Fused LayerNorm kernel benchmarked vs `nn.LayerNorm` (latência + throughput).

---

### S-20 — Tokenização Systems + LLM Decoding
> M2 | intermediário | supplemented | Map: 11-868 tópico 4 | Dep: S02, S17

| Camada | Atividade | h |
|---|---|---|
| Teoria | Batched tokenization; padding strategies; greedy/beam/top-p/top-k decoding; KV cache basics; sampling temperature | 2.5h |
| Readings | HuggingFace Tokenizers docs; vLLM intro (Kwon et al. 2023 — seção decoding) | 3h |
| Lab | Batched decoding benchmark: tokens/s, latência, peak memory por estratégia (greedy, beam, top-p) | 3h |
| Exercícios+Assess | Medir impacto de padding vs dynamic batching; rubrica | 1.5h |
| Revisão | Flashcards: KV cache size formula, decoding strategies tradeoffs | 0.5h |
| **Total** | | **~10.5h** |

**Deliverable:** Batched decoding: tokens/s, latência, memória por estratégia documentados.

---

### S-21 — GPU Acceleration I — Batching + Memory
> M2 | avançado | supplemented | Map: 11-868 tópico 5 | Dep: S17, S20

| Camada | Atividade | h |
|---|---|---|
| Teoria | Continuous batching vs static batching; activation memory; recomputation (gradient checkpointing); memory footprint formula | 2.5h |
| Readings | Yu et al. 2022 (Orca — continuous batching); vLLM memory analysis (Kwon 2023); Rajbhandari 2019 (activation memory) | 3.5h |
| Lab | Continuous batching implementation: throughput vs static batching (5 batch sizes) | 3.5h |
| Exercícios+Assess | Calcular memory breakdown: weights + activations + KV cache; rubrica | 1h |
| Revisão | Flashcards: continuous batching, recomputation tradeoff, memory budget | 0.5h |
| **Total** | | **~11h** |

**Deliverable:** Continuous batching: throughput comparison vs static batching documentado.

---

### S-22 — GPU Acceleration II — Kernel Fusion + Triton
> M2 | avançado | supplemented | Map: 11-868 tópico 6 | Dep: S18, S21

| Camada | Atividade | h |
|---|---|---|
| Teoria | Operator fusion motivação; Triton programming model; fused softmax; fused attention pattern | 2.5h |
| Readings | Tillet et al. 2019 (Triton); Triton docs — kernel design; fused attention tutorial | 3.5h |
| Lab | Triton fused attention forward; latência/throughput vs PyTorch SDPA (`F.scaled_dot_product_attention`) | 4h |
| Exercícios+Assess | Profile memory I/O do kernel vs unfused; rubrica | 1h |
| Revisão | Flashcards: Triton program model, tiling strategy, SRAM budget | 0.5h |
| **Total** | | **~11.5h** |

**Deliverable:** Triton fused attention forward — latência/throughput vs PyTorch SDPA.

---

### S-23 — Distributed Training I — Pipeline Parallelism
> M2 | avançado | supplemented | Map: 11-868 tópico 7 | Dep: S17, S22

| Camada | Atividade | h |
|---|---|---|
| Teoria | Pipeline parallelism; GPipe; micro-batching; bubble overhead; 1F1B scheduling | 2.5h |
| Readings | Huang et al. 2019 (GPipe); Narayanan et al. 2021 (1F1B); Narayanan et al. 2021 (Megatron-LM) | 3.5h |
| Lab | Pipeline 2-stage simulation; bubble fraction medida; vs data parallel (throughput + memory) | 3.5h |
| Exercícios+Assess | Calcular bubble overhead para P stages M micro-batches; rubrica | 1h |
| Revisão | Flashcards: GPipe schedule, 1F1B, bubble fraction formula | 0.5h |
| **Total** | | **~11h** |

**Deliverable:** Pipeline 2-stage — bubble fraction medida vs data parallel documentado.

---

### S-24 — Distributed Training II — Tensor Parallelism
> M2 | avançado | supplemented | Map: 11-868 tópico 8 | Dep: S23

| Camada | Atividade | h |
|---|---|---|
| Teoria | Tensor parallelism (Megatron); column/row split de linear layers; all-reduce; sequence parallelism | 2.5h |
| Readings | Shoeybi et al. 2019 (Megatron-LM); Korthikanti et al. 2022 (Sequence Parallelism) | 3h |
| Lab | Column-parallel linear implementado; overhead de all-reduce medido (2 GPUs simulado ou real) | 4h |
| Exercícios+Assess | Derivar communication volume para TP degree N; rubrica | 1h |
| Revisão | Flashcards: column vs row split, all-reduce vs reduce-scatter, TP tradeoffs | 0.5h |
| **Total** | | **~11h** |

**Deliverable:** Column-parallel linear — overhead de all-reduce medido por TP degree.

---

### S-25 — Distributed Training III — ZeRO + FSDP
> M2 | avançado | supplemented | Map: 11-868 tópico 9 | Dep: S23, S24

| Camada | Atividade | h |
|---|---|---|
| Teoria | ZeRO Stage 1/2/3; memory formula por stage; FSDP; mixed precision com ZeRO | 2.5h |
| Readings | Rajbhandari et al. 2020 (ZeRO); PyTorch FSDP docs; Zhao et al. 2023 (PyTorch FSDP paper) | 3.5h |
| Lab | FSDP training: peak memory/GPU e throughput vs DDP (ZeRO Stage 1, 2, 3) | 4h |
| Exercícios+Assess | Calcular peak memory para 7B model com ZeRO-3; rubrica | 1h |
| Revisão | Flashcards: ZeRO stages, memory formula, FSDP sharding strategy | 0.5h |
| **Total** | | **~11.5h** |

**Deliverable:** FSDP training: peak memory/GPU + throughput vs DDP por ZeRO stage.

---

### S-26 — Quantization I — PTQ + INT8
> M2 | avançado | supplemented | Map: 11-868 tópico 10 | Dep: S17, S25

| Camada | Atividade | h |
|---|---|---|
| Teoria | Uniform quantization (absmax, zero-point); outlier problem; LLM.int8() mixed-precision; quantization error analysis | 2.5h |
| Readings | Dettmers et al. 2022 (LLM.int8()); Frantar et al. 2022 (GPTQ) | 3.5h |
| Lab | INT8 quantization benchmark: perplexity, memória, latência vs FP16 em GPT-2 Large ou LLaMA-2-7B | 4h |
| Exercícios+Assess | Visualizar distribuição de activations (outlier detection); rubrica | 1h |
| Revisão | Flashcards: absmax, zero-point, mixed-precision trigger | 0.5h |
| **Total** | | **~11.5h** |

**Deliverable:** INT8 benchmark: PPL, memória, latência vs FP16 documentados.

---

### S-27 — Quantization II + QLoRA
> M2 | avançado | supplemented | Map: 11-868 tópico 11 | Dep: S26

| Camada | Atividade | h |
|---|---|---|
| Teoria | GPTQ (second-order Hessian); AWQ (activation-aware); NF4 data type; QLoRA: NF4 + double quantization + LoRA | 2.5h |
| Readings | Frantar et al. 2022 (GPTQ); Lin et al. 2023 (AWQ); Dettmers et al. 2023 (QLoRA) | 3.5h |
| Lab | QLoRA fine-tune (NF4 + r=16): tabela perplexity / memória / tempo vs full FT vs LoRA FP16 | 4h |
| Exercícios+Assess | Comparar AWQ vs GPTQ em latência e accuracy; rubrica | 1h |
| Revisão | Flashcards: NF4 format, double quantization, QLoRA memory savings | 0.5h |
| **Total** | | **~11.5h** |

**Deliverable:** QLoRA fine-tune: tabela comparativa perplexity / memória / tempo vs baselines.

---

### S-28 — Mixture-of-Experts Systems
> M2 | research | supplemented | Map: 11-868 tópico 12 | Dep: S13, S25

| Camada | Atividade | h |
|---|---|---|
| Teoria | Top-K routing; load balancing loss (auxiliary loss); expert parallelism; capacity factor; token dropping | 2.5h |
| Readings | Fedus et al. 2021 (Switch Transformer); Jiang et al. 2024 (Mixtral); Lepikhin et al. 2021 (GShard) | 3.5h |
| Lab | MoE FFN (top-2 routing) + routing analysis plot (distribuição por expert, load imbalance metric) | 4h |
| Exercícios+Assess | Medir expert utilization vs uniform; rubrica | 1h |
| Revisão | Flashcards: top-k routing, auxiliary loss, capacity factor, expert collapse | 0.5h |
| **Total** | | **~11.5h** |

**Deliverable:** MoE FFN + routing analysis plot (distribuição por expert ao longo do treinamento).

---

### S-29 — FlashAttention I & II
> M2 | avançado | supplemented | Map: 11-868 tópico 13 | Dep: S22, S21

| Camada | Atividade | h |
|---|---|---|
| Teoria | FlashAttention IO analysis; tiling; online softmax; FA2 improvements (parallelism, work partitioning) | 2.5h |
| Readings | Dao et al. 2022 (FlashAttention); Dao 2023 (FlashAttention-2); Dao et al. 2022 (FlashAttention math) | 3.5h |
| Lab | Triton FA2 kernel (ou reprodução do benchmark): IO analysis + speedup vs seq length (128→8192) | 4.5h |
| Exercícios+Assess | Calcular HBM access reduction por tiling; rubrica | 1h |
| Revisão | Flashcards: tiling pattern, online softmax, FA2 vs FA1 improvements | 0.5h |
| **Total** | | **~12h** |

**Deliverable:** FlashAttention benchmark — IO analysis + speedup vs seq length documentado.

---

### S-30 — LLM Serving — vLLM + PagedAttention
> M2 | avançado | supplemented | Map: 11-868 tópico 14 | Dep: S20, S21, S29

| Camada | Atividade | h |
|---|---|---|
| Teoria | PagedAttention; KV block manager; paged memory; vLLM scheduler; preemption | 2.5h |
| Readings | Kwon et al. 2023 (vLLM / PagedAttention); vLLM docs (architecture); Agrawal et al. 2024 (Sarathi-Serve) | 3.5h |
| Lab | vLLM benchmark: throughput vs batch size + request rate; P50/P95 latência; comparação vs HF generate | 4h |
| Exercícios+Assess | Analisar block fragmentation em trace de requests; rubrica | 1h |
| Revisão | Flashcards: PagedAttention, block table, fragmentation, preemption | 0.5h |
| **Total** | | **~11.5h** |

**Deliverable:** vLLM benchmark: throughput vs batch size + P50/P95 latência documentados.

---

### S-31 — KV Cache Opt + Disagg. Serving + SGLang
> M2 | research | supplemented | Map: 11-868 tópico 15 | Dep: S29, S30

| Camada | Atividade | h |
|---|---|---|
| Teoria | GQA/MQA; prefill-decode disaggregation; chunked prefill; SGLang RadixAttention; structured outputs | 2.5h |
| Readings | Ainslie et al. 2023 (GQA); Zheng et al. 2024 (SGLang); Patel et al. 2024 (Splitwise disaggregation) | 3.5h |
| Lab | SGLang structured JSON pipeline + GQA memory savings vs MHA benchmark | 4h |
| Exercícios+Assess | Calcular KV cache memory savings GQA(G=4) vs MHA; rubrica | 1h |
| Revisão | Flashcards: GQA heads formula, disaggregated serving, SGLang RadixAttention | 0.5h |
| **Total** | | **~11.5h** |

**Deliverable:** SGLang structured JSON pipeline + GQA memory savings documentados.

---

### S-32 — RLHF Systems + Projeto Final M2
> M2 | research | supplemented | Map: 11-868 tópico 16 | Dep: S11, S25, S31

| Camada | Atividade | h |
|---|---|---|
| Teoria | RLHF at scale: actor/critic deployment; reference model memory; online RL infrastructure | 2h |
| Readings | Hu et al. 2024 (OpenRLHF); Zheng et al. 2023 (RLHF survey systems perspective) | 2.5h |
| Projeto M2 | Mini RLHF pipeline (reward model + PPO) + relatório técnico do projeto M2 | 5h |
| Retrospectiva M2 | coverage-matrix M2 completa; ≥80% `✓ coberto`; gaps para M3 | 2h |
| **Total** | | **~11.5h** |

**Deliverable:** Mini RLHF pipeline (RM + PPO) + coverage-matrix M2 com ≥80% `✓ coberto`.

---

## Módulo 3 — Multimodal Machine Learning (S33–S48)

---

### S-33 — Multimodal ML: Challenges + Unimodal Foundations
> M3 | fundamentos | supplemented | Map: 11-777 intro | Dep: S32

| Camada | Atividade | h |
|---|---|---|
| Teoria | 6 desafios de multimodal ML (Morency): representation, alignment, reasoning, generation, transference, quantification; encoders: ViT, BERT, wav2vec | 2.5h |
| Readings | Morency & Liang ACL 2017 tutorial; Dosovitskiy et al. 2020 (ViT); cmu-mmml.github.io overview | 3h |
| Lab | Embedding space UMAP: text, image, audio para mesmo conceito (ex: "dog") — separação vs mixing | 3h |
| Exercícios+Assess | Classificar 5 tasks multimodais nos 6 desafios; rubrica | 1h |
| Revisão | Flashcards: 6 challenges, ViT patch embedding, modality gap | 0.5h |
| **Total** | | **~10h** |

**Deliverable:** UMAP embedding space: text, image, audio para mesmo conceito visualizado.

---

### S-34 — Representation I — Multimodal Embeddings + CLIP
> M3 | intermediário | supplemented | Map: 11-777 repr. I | Dep: S33

| Camada | Atividade | h |
|---|---|---|
| Teoria | Contrastive learning; InfoNCE loss; CLIP architecture (dual encoder); zero-shot transfer | 2.5h |
| Readings | Radford et al. 2021 (CLIP); Chen et al. 2020 (SimCLR); Oord et al. 2018 (CPC/InfoNCE) | 3.5h |
| Lab | CLIP fine-tuned em domain dataset (ex: medical images ou satellite); zero-shot accuracy antes/depois | 3.5h |
| Exercícios+Assess | Implementar InfoNCE loss; análise de hard negatives; rubrica | 1h |
| Revisão | Flashcards: InfoNCE, temperature scaling, modality alignment | 0.5h |
| **Total** | | **~11h** |

**Deliverable:** CLIP fine-tuned em domain dataset com zero-shot accuracy antes/depois documentado.

---

### S-35 — Representation II — VLMs (BLIP, LLaVA)
> M3 | intermediário | supplemented | Map: 11-777 repr. II | Dep: S34

| Camada | Atividade | h |
|---|---|---|
| Teoria | BLIP: ITC + ITM + LM losses; Q-Former; LLaVA: projection layer + instruction tuning; InstructBLIP | 2.5h |
| Readings | Li et al. 2022 (BLIP); Liu et al. 2023 (LLaVA); Dai et al. 2023 (InstructBLIP) | 3.5h |
| Lab | LLaVA failure analysis: ≥3 categorias de erro (spatial reasoning, OCR, counting, hallucination) documentadas com exemplos | 3.5h |
| Exercícios+Assess | Comparar ITC vs cosine similarity em 100 pairs; rubrica | 1h |
| Revisão | Flashcards: Q-Former, LLaVA projection, ITC/ITM losses | 0.5h |
| **Total** | | **~11h** |

**Deliverable:** LLaVA failure analysis: ≥3 categorias de erro documentadas com exemplos reprodutíveis.

---

### S-36 — Alignment I — Cross-Modal Attention + Contrastive
> M3 | intermediário | supplemented | Map: 11-777 align. I | Dep: S34, S35

| Camada | Atividade | h |
|---|---|---|
| Teoria | Cross-attention para alignment; hard negative mining; contrastive vs generative alignment; retrieval metrics | 2.5h |
| Readings | cmu-mmml.github.io leituras de alignment; Faghri et al. 2018 (VSE++); Li et al. 2021 (ALIGN) | 3h |
| Lab | Cross-modal retrieval demo (image→text, text→image); precision@K chart (K=1,5,10) | 3.5h |
| Exercícios+Assess | Implementar hard negative mining; medir impact em R@1; rubrica | 1.5h |
| Revisão | Flashcards: hard negative mining, R@K metrics, contrastive vs generative | 0.5h |
| **Total** | | **~11h** |

**Deliverable:** Cross-modal retrieval demo + precision@K chart (text↔image).

---

### S-37 — Alignment II — Multimodal Transformers
> M3 | avançado | supplemented | Map: 11-777 align. II | Dep: S36

| Camada | Atividade | h |
|---|---|---|
| Teoria | Fusion positions: early/mid/late; ViLBERT dual-stream; Perceiver cross-attention; ablação de fusion | 2.5h |
| Readings | Lu et al. 2019 (ViLBERT); Jaegle et al. 2021 (Perceiver); Kim et al. 2021 (ViLT) | 3.5h |
| Lab | Ablação: late fusion vs cross-attention em VQA mini-set (VQA v2 subset, 1000 perguntas) | 4h |
| Exercícios+Assess | Comparar parâmetros e latência de cada fusion strategy; rubrica | 1h |
| Revisão | Flashcards: fusion positions, Perceiver attention, ViLBERT streams | 0.5h |
| **Total** | | **~11.5h** |

**Deliverable:** Ablação late fusion vs cross-attention em VQA mini-set com tabela de resultados.

---

### S-38 — Reasoning I — Multimodal Reasoning + Visual CoT
> M3 | avançado | supplemented | Map: 11-777 reason. I | Dep: S35, S37

| Camada | Atividade | h |
|---|---|---|
| Teoria | Visual question answering; spatial reasoning gaps; visual chain-of-thought; program synthesis para VQA | 2.5h |
| Readings | Hudson & Manning 2019 (GQA); Bisk et al. 2020 (PIQA); Lu et al. 2022 (ScienceQA — visual CoT) | 3.5h |
| Lab | Spatial reasoning benchmark (GQA subset, 500 questions); categorização de erros em ≥4 tipos | 3.5h |
| Exercícios+Assess | Analisar CoT traces: onde o modelo falha; rubrica | 1h |
| Revisão | Flashcards: GQA dataset, spatial reasoning gaps, visual CoT patterns | 0.5h |
| **Total** | | **~11h** |

**Deliverable:** Spatial reasoning benchmark (GQA subset) + categorização de erros por tipo.

---

### S-39 — Reasoning II — Neuro-Symbolic + Graph Multimodal
> M3 | avançado | supplemented | Map: 11-777 reason. II | Dep: S38

| Camada | Atividade | h |
|---|---|---|
| Teoria | Scene graphs; object detection + relation extraction; GNN para multimodal; neuro-symbolic integration | 2.5h |
| Readings | Johnson et al. 2018 (scene graph survey); Marino et al. 2019 (OK-VQA); Li et al. 2019 (GNN VQA) | 3.5h |
| Lab | Scene graph + GNN-based reasoning demo em COCO (object detection + relation prediction) | 4h |
| Exercícios+Assess | Comparar GNN-based vs pure attention em reasoning accuracy; rubrica | 1h |
| Revisão | Flashcards: scene graph structure, GNN message passing, neuro-symbolic | 0.5h |
| **Total** | | **~11.5h** |

**Deliverable:** Scene graph + GNN-based reasoning demo em COCO com métricas de relação.

---

### S-40 — Generation I — Text-to-Image + Diffusion
> M3 | avançado | supplemented | Map: 11-777 gen. I | Dep: S34, S37

| Camada | Atividade | h |
|---|---|---|
| Teoria | DDPM; forward/reverse process; DDIM; latent diffusion; CFG (classifier-free guidance); CLIP conditioning | 2.5h |
| Readings | Ho et al. 2020 (DDPM); Song et al. 2020 (DDIM); Rombach et al. 2022 (Stable Diffusion / LDM) | 3.5h |
| Lab | Guidance scale vs quality/diversity tradeoff com Stable Diffusion (FID proxy, CLIP score) | 4h |
| Exercícios+Assess | Derivar reverse diffusion step; visualizar noise schedule; rubrica | 1h |
| Revisão | Flashcards: DDPM forward/reverse, CFG formula, latent diffusion pipeline | 0.5h |
| **Total** | | **~11.5h** |

**Deliverable:** Guidance scale vs quality/diversity tradeoff (FID proxy + CLIP score documentados).

---

### S-41 — Generation II — Captioning + Cross-Modal Retrieval
> M3 | avançado | supplemented | Map: 11-777 gen. II | Dep: S35, S40

| Camada | Atividade | h |
|---|---|---|
| Teoria | Encoder-decoder captioning; COCO evaluation (BLEU-4, CIDEr, METEOR, SPICE); cross-modal retrieval metrics | 2.5h |
| Readings | Li et al. 2023 (BLIP-2); Chen et al. 2015 (COCO captions); Fang et al. 2022 (EVA-CLIP) | 3.5h |
| Lab | BLIP-2 fine-tuned em domínio; COCO captioning metrics; retrieval R@1/R@5/R@10 | 4h |
| Exercícios+Assess | Analisar CIDEr vs BLEU-4: onde divergem; rubrica | 1h |
| Revisão | Flashcards: CIDEr formula, BLIP-2 Q-Former, R@K interpretation | 0.5h |
| **Total** | | **~11.5h** |

**Deliverable:** BLIP-2 fine-tuned + COCO metrics + retrieval R@1/R@5/R@10 documentados.

---

### S-42 — Transference — Co-learning + Zero/Few-Shot
> M3 | avançado | supplemented | Map: 11-777 transf. | Dep: S34, S38

| Camada | Atividade | h |
|---|---|---|
| Teoria | Co-learning: transfer between modalities; zero-shot vs few-shot multimodal; multi-task learning | 2.5h |
| Readings | Wang et al. 2022 (co-learning survey); Zoph et al. 2020 (transfer NLP→vision); CLIP zero-shot analysis | 3h |
| Lab | Zero-shot vs few-shot accuracy em 3 domínios (medical, satellite, artwork) — comparação CLIP vs fine-tuned | 4h |
| Exercícios+Assess | Analisar domain gap entre domínios; rubrica | 1h |
| Revisão | Flashcards: co-learning types, few-shot multimodal, negative transfer | 0.5h |
| **Total** | | **~11h** |

**Deliverable:** Zero-shot vs few-shot accuracy em 3 domínios com análise de domain gap.

---

### S-43 — Quantification — Auto-Encoders + Deep CCA
> M3 | research | supplemented | Map: 11-777 quant. | Dep: S33, S37

| Camada | Atividade | h |
|---|---|---|
| Teoria | MVAE; shared vs private representations; Deep CCA; canonical correlation; mutual information estimation | 2.5h |
| Readings | Wu & Goodman 2018 (MVAE); Andrew et al. 2013 (Deep CCA); Federici et al. 2020 (shared representations) | 3.5h |
| Lab | MVAE latent space visualization (UMAP) + cross-modal generation (text→image) | 4.5h |
| Exercícios+Assess | Calcular CCA correlation entre CLIP text e image embeddings; rubrica | 1h |
| Revisão | Flashcards: MVAE ELBO, Deep CCA, shared vs private repr. | 0.5h |
| **Total** | | **~12h** |

**Deliverable:** MVAE latent space visualization + cross-modal generation demo.

---

### S-44 — Fusion — Tensor Fusion + Multi-Kernel + Attention
> M3 | research | supplemented | Map: 11-777 fusion | Dep: S33, S37, S43

| Camada | Atividade | h |
|---|---|---|
| Teoria | Tensor fusion network (TFN); Tucker decomposition para eficiência; multi-kernel learning; gated fusion | 2.5h |
| Readings | Zadeh et al. 2017 (TFN); Liu et al. 2018 (Low-rank MFN); Liang et al. 2019 (Multimodal Transformer) | 3.5h |
| Lab | TFN vs late fusion ablação em CMU-MOSI (sentiment accuracy + latência + #params) | 4.5h |
| Exercícios+Assess | Analisar trilinear interaction term; rubrica | 1h |
| Revisão | Flashcards: TFN outer product, Tucker decomp, gated fusion | 0.5h |
| **Total** | | **~12h** |

**Deliverable:** TFN vs late fusion ablação em CMU-MOSI (accuracy + latência documentados).

---

### S-45 — Applications I — Affect Recognition + Grounding
> M3 | research | supplemented | Map: 11-777 app. I | Dep: S37, S44

| Camada | Atividade | h |
|---|---|---|
| Teoria | Multimodal affect recognition; CMU-MOSI/MOSEI dataset; language grounding; referring expression | 2.5h |
| Readings | Zadeh et al. 2018 (CMU-MOSI); Yu et al. 2020 (MDETR — modulated detection); Morency lab publications | 3.5h |
| Lab | Multimodal affect system em CMU-MOSI: ablação all-modalities vs unimodal (audio/video/text) | 4.5h |
| Exercícios+Assess | Analisar which modality contribui mais por arousal/valence; rubrica | 1h |
| Revisão | Flashcards: CMU-MOSI labels, grounding formulation, affect dimensions | 0.5h |
| **Total** | | **~12h** |

**Deliverable:** Multimodal affect system + ablação all-modalities vs unimodal com análise por modalidade.

---

### S-46 — Applications II — VLN + Embodied AI
> M3 | research | supplemented | Map: 11-777 app. II | Dep: S38, S42

| Camada | Atividade | h |
|---|---|---|
| Teoria | Vision-Language Navigation (VLN); R2R dataset; instruction following; embodied question answering; CLAW lab | 2.5h |
| Readings | Anderson et al. 2018 (R2R); Bisk et al. 2020 (PIQA embodied); Shridhar et al. 2020 (ALFRED) | 3.5h |
| Lab | VLN navigation success rate + failure analysis em R2R val set (≥3 failure categories) | 4.5h |
| Exercícios+Assess | Analisar erros de instruction grounding vs navigation errors; rubrica | 1h |
| Revisão | Flashcards: R2R metrics (SR, SPL), embodied AI loop, VLN failure modes | 0.5h |
| **Total** | | **~12h** |

**Deliverable:** VLN navigation success rate + failure analysis em R2R val (≥3 categorias).

---

### S-47 — Frontier — Multimodal LLMs (GPT-4V, Gemini, Idefics)
> M3 | research | supplemented | Map: 11-777 frontier | Dep: S35, S42, S45

| Camada | Atividade | h |
|---|---|---|
| Teoria | Frontier VLMs: arquitetura GPT-4V, Gemini 1.5 Pro (long context), Idefics, Phi-3-vision; interleaved VLMs | 2.5h |
| Readings | GPT-4V system card; Gemini Team 2023 (tech report); Laurençon et al. 2023 (Idefics) | 3.5h |
| Lab | Comparative benchmark: LLaVA vs Idefics vs Phi-3-vision em 3 tasks (captioning, VQA, OCR) | 4.5h |
| Exercícios+Assess | Analisar scaling behavior cross-model; rubrica | 1h |
| Revisão | Flashcards: GPT-4V capabilities, Gemini modalities, interleaved generation | 0.5h |
| **Total** | | **~12h** |

**Deliverable:** Comparative benchmark: LLaVA vs Idefics vs Phi-3-vision (captioning + VQA + OCR).

---

### S-48 — Capstone + Retrospectiva do Kit
> M3 | research | bridge | Map: — | Dep: S33–S47

| Camada | Atividade | h |
|---|---|---|
| Capstone | Sistema vision-language ponta a ponta: CLIP retriever + LLaVA/BLIP-2 generator + evaluation (CIDEr, R@K) | 6h |
| Slides técnicos | Apresentação 15min cobrindo: motivação, arquitetura, experimentos, resultados, limitações, próximos passos | 2.5h |
| Retrospectiva final | coverage-matrix M3 + kit completo: ≥80% `✓ coberto`; documento de next steps pessoais | 2h |
| Revisão espaçada | Deck consolidado M3 + revisão cross-módulo (flash-linking M1↔M2↔M3 concepts) | 1.5h |
| **Total** | | **~12h** |

**Deliverable:** Pipeline vision-language ponta a ponta + slides técnicos (15 min) + coverage-matrix completa.

---

## Resumo de carga por módulo

| Módulo | Semanas | Carga estimada |
|---|---|---|
| M1 — LLMs Methods & Applications | S01–S16 | ~171h |
| M2 — LLM Systems | S17–S32 | ~181h |
| M3 — Multimodal Machine Learning | S33–S48 | ~186h |
| **Total** | **48 semanas** | **~538h** |

> *Nota: carga abaixo das 576h nominais porque as primeiras semanas de M1 são mais leves (fundamentos). Semanas de M2/M3 e research ficam próximas de 12h.*
