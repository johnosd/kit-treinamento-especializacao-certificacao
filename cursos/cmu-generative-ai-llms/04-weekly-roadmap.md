# Roadmap Semanal — CMU Generative AI & LLMs Kit

> Tabela macro: mapeamento de todas as 48 semanas do kit ao syllabus original.
> `core` = 1:1 com syllabus publicado | `supplemented` = suplementado via Gap Supplementation Rule | `bridge` = semana extra de síntese/revisão

| Semana | Módulo | Tema | Complexidade | Deliverable | Mapeia syllabus original | Tipo |
|---:|---|---|---|---|---|---|
| 01 | M1 | Building Blocks of Modern LLMs | fundamentos | Self-attention 1-layer (NumPy) vs `nn.MultiheadAttention` | 11-667 W01 | core |
| 02 | M1 | Pre-training Data + Tokenization + Arch Advances | fundamentos | BPE tokenizer custom em corpus domain | 11-667 W02 | core |
| 03 | M1 | Avaliação Automática + ICL + PEFT/LoRA | intermediário | LoRA from scratch + HELM mini-evaluation | 11-667 W03 | core |
| 04 | M1 | Reasoning in LLMs + Human-Agent Evaluation | intermediário | Relatório de evaluation malpractices em benchmark escolhido | 11-667 W04 | core |
| 05 | M1 | ICL Behaviors + Alignment + Tool Use | intermediário | Tool-calling agent (≥5 cenários) com HuggingFace | 11-667 W05 | core |
| 06 | M1 | RAG + Scaling Laws | intermediário | RAG pipeline (FAISS + HF) benchmarked em TriviaQA | 11-667 W06 | core |
| 07 | M1 | Parallel Training (Optim.) + Interpretability | avançado | Training script com gradient accumulation + profiling report | 11-667 W07 | core |
| 08 | M1 | Revisão M1 (S01–S07) + Lab de integração | fundamentos | Lab: LoRA + RAG pipeline integrado + documento de gaps pessoais | 11-667 W08 (break) | bridge |
| 09 | M1 | Bias, Ethics & Safety | intermediário | Red-team report (≥5 categorias) em modelo aberto | 11-667 W09 | core |
| 10 | M1 | LLM Security + Benchmark Leakage + RecSys | avançado | Membership inference probe + contamination methodology demo | 11-667 W10 | core |
| 11 | M1 | RLHF + DPO | avançado | DPO-tuned GPT-2 com win-rate vs SFT baseline | 11-667 W11 | core |
| 12 | M1 | Efficient Inference + LLM Agents | avançado | vLLM benchmark: tokens/s; latência P50/P95 por batch size | 11-667 W12 | core |
| 13 | M1 | Long-Context + Sparse Pretraining / MoE | avançado | Position bias plot + MoE router com load balancing | 11-667 W13 | core |
| 14 | M1 | Synthetic Data Training | research | Pipeline de dados sintéticos + ablação synthetic vs real | 11-667 W14 | core |
| 15 | M1 | Mini-Project M1 (implementação + escrita) | research | Relatório técnico 4–6 págs + código reprodutível | 11-667 W15 | core |
| 16 | M1 | Avaliação Final M1 + Retrospectiva | research | coverage-matrix M1 preenchida; ≥80% `✓ coberto` | 11-667 W16 | core |
| 17 | M2 | Intro a LLM Systems + GPU Architecture | fundamentos | Profiling report: compute vs memory bound por operação | 11-868 tópico 1 | supplemented |
| 18 | M2 | CUDA Kernels + Autograd Implementation | intermediário | CUDA GEMM naive → tiled; speedup vs cuBLAS documentado | 11-868 tópico 2 | supplemented |
| 19 | M2 | DL Frameworks + Transformer Systems | intermediário | Fused LayerNorm kernel; benchmarked vs `nn.LayerNorm` | 11-868 tópico 3 | supplemented |
| 20 | M2 | Tokenização Systems + LLM Decoding | intermediário | Batched decoding: tokens/s, latência, memória por estratégia | 11-868 tópico 4 | supplemented |
| 21 | M2 | GPU Acceleration I — Batching + Memory | avançado | Continuous batching: throughput vs static batching | 11-868 tópico 5 | supplemented |
| 22 | M2 | GPU Acceleration II — Kernel Fusion + Triton | avançado | Triton fused attention forward; latência/throughput vs PyTorch SDPA | 11-868 tópico 6 | supplemented |
| 23 | M2 | Distributed Training I — Pipeline Parallelism | avançado | Pipeline 2-stage; bubble fraction medida; vs data parallel | 11-868 tópico 7 | supplemented |
| 24 | M2 | Distributed Training II — Tensor Parallelism | avançado | Column-parallel linear; overhead de all-reduce medido | 11-868 tópico 8 | supplemented |
| 25 | M2 | Distributed Training III — ZeRO + FSDP | avançado | FSDP training: peak memory/GPU; throughput vs DDP | 11-868 tópico 9 | supplemented |
| 26 | M2 | Quantization I — PTQ + INT8 | avançado | INT8 benchmark: PPL, memória, latência vs FP16 | 11-868 tópico 10 | supplemented |
| 27 | M2 | Quantization II + QLoRA | avançado | QLoRA fine-tune: tabela perplexity / memória / tempo vs full FT | 11-868 tópico 11 | supplemented |
| 28 | M2 | Mixture-of-Experts Systems | research | MoE FFN + routing analysis plot (distribuição por expert) | 11-868 tópico 12 | supplemented |
| 29 | M2 | FlashAttention I & II | avançado | Triton FA2 kernel; IO analysis; speedup vs seq length | 11-868 tópico 13 | supplemented |
| 30 | M2 | LLM Serving — vLLM + PagedAttention | avançado | vLLM benchmark: throughput vs batch size; P50/P95 | 11-868 tópico 14 | supplemented |
| 31 | M2 | KV Cache Opt + Disagg. Serving + SGLang | research | SGLang structured JSON pipeline; GQA memory savings | 11-868 tópico 15 | supplemented |
| 32 | M2 | RLHF Systems + Projeto Final M2 | research | Mini RLHF pipeline (reward model + PPO) + projeto M2 | 11-868 tópico 16 | supplemented |
| 33 | M3 | Multimodal ML: Challenges + Unimodal Foundations | fundamentos | Embedding space (UMAP): text, image, audio para mesmo conceito | 11-777 intro | supplemented |
| 34 | M3 | Representation I — Multimodal Embeddings + CLIP | intermediário | CLIP fine-tuned em domain dataset; zero-shot accuracy | 11-777 repr. I | supplemented |
| 35 | M3 | Representation II — VLMs (BLIP, LLaVA) | intermediário | LLaVA failure analysis: ≥3 categorias de erro documentadas | 11-777 repr. II | supplemented |
| 36 | M3 | Alignment I — Cross-Modal Attention + Contrastive | intermediário | Cross-modal retrieval demo; precision@K chart | 11-777 align. I | supplemented |
| 37 | M3 | Alignment II — Multimodal Transformers | avançado | Ablação: late fusion vs cross-attention em VQA mini-set | 11-777 align. II | supplemented |
| 38 | M3 | Reasoning I — Multimodal Reasoning + Visual CoT | avançado | Spatial reasoning benchmark (GQA subset); categorização de erros | 11-777 reason. I | supplemented |
| 39 | M3 | Reasoning II — Neuro-Symbolic + Graph Multimodal | avançado | Scene graph + GNN-based reasoning demo em COCO | 11-777 reason. II | supplemented |
| 40 | M3 | Generation I — Text-to-Image + Diffusion | avançado | Guidance scale vs quality/diversity tradeoff (Stable Diffusion) | 11-777 gen. I | supplemented |
| 41 | M3 | Generation II — Captioning + Cross-Modal Retrieval | avançado | BLIP-2 fine-tuned; COCO captioning metrics; retrieval R@1/R@5/R@10 | 11-777 gen. II | supplemented |
| 42 | M3 | Transference — Co-learning + Zero/Few-Shot | avançado | Zero-shot vs few-shot accuracy em 3 domínios | 11-777 transf. | supplemented |
| 43 | M3 | Quantification — Auto-Encoders + Deep CCA | research | MVAE latent space visualization + cross-modal generation | 11-777 quant. | supplemented |
| 44 | M3 | Fusion — Tensor Fusion + Multi-Kernel + Attention | research | TFN vs late fusion ablação em CMU-MOSI (accuracy + latência) | 11-777 fusion | supplemented |
| 45 | M3 | Applications I — Affect Recognition + Grounding | research | Multimodal affect system; ablação all-modalities vs unimodal | 11-777 app. I | supplemented |
| 46 | M3 | Applications II — VLN + Embodied AI | research | VLN navigation success rate + failure analysis em R2R val | 11-777 app. II | supplemented |
| 47 | M3 | Frontier — Multimodal LLMs (GPT-4V, Gemini) | research | Comparative benchmark: LLaVA vs Idefics vs Phi-3-vision | 11-777 frontier | supplemented |
| 48 | M3 | Capstone + Retrospectiva do Kit | research | Pipeline vision-language ponta a ponta + slides técnicos (15 min) | — | bridge |
