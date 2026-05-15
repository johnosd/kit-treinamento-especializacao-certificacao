# Matriz de Cobertura — CMU Generative AI & LLMs Kit

> Gerado pelo Coordenador. Atualizado pelo Revisor de Fidelidade (`10-revisor-fidelidade.md`) após cada semana.
>
> **Estados:** `⏳ pendente` | `✓ coberto` | `+ suplementado` | `⚠ raso` | `✗ ausente`
>
> **Fonte M1:** 11-667 Fall 2025 — https://2025.cmu-llms.org/schedule/
> **Fonte M2:** 11-868 Spring 2025 — https://llmsystem.github.io/llmsystem2025spring/ (`supplemented`: sem schedule semanal publicado)
> **Fonte M3:** 11-777 — https://cmu-mmml.github.io/ (`supplemented`: tópicos derivados do 6-challenge framework)

---

## Módulo 1 — LLMs Methods & Applications (11-967)

| Semana orig. | Tópicos oficiais (11-667) | Deliverables originais | Semana kit | Coberto? | Supl.? | Nota |
|---:|---|---|---:|---|---|---|
| W01 | Building blocks of modern LLMs; Transformer architecture; pre-training objectives | Assignment #0 due | 01 | ✓ coberto | — | Revisão 2026-05-15 → [09-coverage.md](modules/01-week-01/09-coverage.md) |
| W02 | Pre-training data curation; tokenization; arch advances (GQA, RoPE, LayerNorm) | Assignment #1 released | 02 | ⏳ pendente | — | — |
| W03 | Automatic evaluation (BIG-Bench, HELM); ICL; task-oriented finetuning; PEFT | Assignment #1 due | 03 | ⏳ pendente | — | — |
| W04 | Reasoning in translation models (guest); eval in human-agent interaction (guest) | Assignment #2 released | 04 | ⏳ pendente | — | Guest lectures não replicáveis; suplementar com papers dos convidados |
| W05 | ICL surprising behaviors; model alignment; tool use in LLMs | — | 05 | ⏳ pendente | — | — |
| W06 | RAG (guest: Akari Asai); scaling laws; Chinchilla | — | 06 | ⏳ pendente | — | — |
| W07 | Scaling up — optimization & parallel training; interpretability methods | Assignment #2 due; #3 released | 07 | ⏳ pendente | — | — |
| W08 | Fall break (sem aula) | — | 08 | ⏳ pendente | + | Bridge: revisão + lab de integração (suplementado) |
| W09 | Midterm exam (10/21); bias and ethical issues | Assignment #3 due | 09 | ⏳ pendente | — | Exame substituído por avaliação autodidata equivalente |
| W10 | Attacking LLM systems + benchmark leakage; LLMs for RecSys (guest) | Assignment #4 released | 10 | ⏳ pendente | — | — |
| W11 | Democracy Day (sem aula); RLHF | Assignment #4 due | 11 | ⏳ pendente | — | — |
| W12 | Efficient inference methods; chatbots and LLM agents | Mini-project released | 12 | ⏳ pendente | — | — |
| W13 | Long-context models; efficient pretraining with sparse models (MoE) | — | 13 | ⏳ pendente | — | — |
| W14 | Training with synthetic data | — | 14 | ⏳ pendente | — | — |
| W15 | Mini-project presentations | Mini-project due (12/07) | 15 | ⏳ pendente | — | — |
| W16 | Final exam (12/09) | Final exam | 16 | ⏳ pendente | — | Exam substituído por avaliação autodidata |

---

## Módulo 2 — LLM Systems (11-968)

> **Nota de suplementação:** 11-868 não publica schedule semanal detalhado. Tópicos derivados de https://llmsystem.github.io/llmsystem2025spring/ e organizados pelo Coordenador.
> **Fonte de suplementação:** llmsystem.github.io/llmsystem2025spring/ + Megatron-LM / DeepSpeed / vLLM documentação oficial.

| Tópico orig. (11-868) | Tópicos derivados | Deliverables orig. | Semana kit | Coberto? | Supl.? | Nota |
|---|---|---|---:|---|---|---|
| Introduction to LLMs + GPU basics | GPU memory hierarchy; compute vs memory bound; FLOP/byte ratio | HW1 (parcial) | 17 | ⏳ pendente | + | Supl. de llmsystem.github.io + NVIDIA GPU guide |
| GPU programming + autograd | CUDA thread hierarchy; tiled GEMM; custom autograd Function | HW1 | 18 | ⏳ pendente | + | Supl. Kirk & Hwu + CUDA prog. guide |
| DL frameworks + transformer systems | Computation graphs; JIT; fused kernels | HW1 | 19 | ⏳ pendente | + | Supl. PyTorch internals + TorchScript |
| Tokenization + decoding strategies | Batched tokenization; greedy/beam/top-p; KV cache basics | HW2 (parcial) | 20 | ⏳ pendente | + | Supl. HF Tokenizers + vLLM intro |
| GPU acceleration I | Continuous batching; activation memory; recomputation | HW2 | 21 | ⏳ pendente | + | Supl. Orca paper + vLLM memory analysis |
| GPU acceleration II | Operator fusion; Triton programming; fused softmax/attention | HW2 | 22 | ⏳ pendente | + | Supl. Triton paper + docs |
| Distributed training I | Pipeline parallelism (GPipe); micro-batching; bubble overhead | HW3 (parcial) | 23 | ⏳ pendente | + | Supl. GPipe + 1F1B paper |
| Distributed training II | Tensor parallelism (Megatron); column/row split; all-reduce | HW3 | 24 | ⏳ pendente | + | Supl. Megatron-LM |
| Distributed training III | ZeRO (Z1/Z2/Z3); memory formula; FSDP | HW3 | 25 | ⏳ pendente | + | Supl. ZeRO paper + PyTorch FSDP |
| Model quantization I | Uniform quantization; absmax; LLM.int8() | HW4 (parcial) | 26 | ⏳ pendente | + | Supl. LLM.int8() + GPTQ |
| Model quantization II + PEFT | GPTQ; AWQ; QLoRA (NF4 + LoRA) | HW4 | 27 | ⏳ pendente | + | Supl. QLoRA paper + AWQ |
| MoE systems | Top-K routing; load balancing; expert parallelism | HW4 | 28 | ⏳ pendente | + | Supl. Switch Transformer + Mixtral |
| Attention optimization | FlashAttention tiling; HBM access formula; FA2 | HW5 (parcial) | 29 | ⏳ pendente | + | Supl. FlashAttention 1 & 2 papers |
| LLM serving | vLLM; PagedAttention; KV block manager | HW5 | 30 | ⏳ pendente | + | Supl. vLLM paper + docs |
| KV opt + disaggregated serving | GQA/MQA; prefill-decode split; SGLang | Project | 31 | ⏳ pendente | + | Supl. GQA paper + SGLang docs |
| RLHF systems | RLHF at scale; actor/critic deployment; online RL | Project final | 32 | ⏳ pendente | + | Supl. OpenRLHF + RLHF systems papers |

---

## Módulo 3 — Multimodal Machine Learning (11-977)

> **Nota de suplementação:** 11-777 não publica schedule semana-a-semana público com o mesmo nível de detalhe. Tópicos derivados do 6-challenge framework publicado em https://cmu-mmml.github.io/.
> **Fonte de suplementação primária:** cmu-mmml.github.io + Stanford CS324 + Berkeley CS294.

| Tópico orig. (11-777) | Tópicos derivados | Deliverable orig. | Semana kit | Coberto? | Supl.? | Nota |
|---|---|---|---:|---|---|---|
| Intro + Challenges Framework | 6 desafios; unimodal encoders (ViT, BERT, wav2vec) | — | 33 | ⏳ pendente | + | Supl. Morency ACL 2017 tutorial + ViT paper |
| Representation I | Contrastive learning; InfoNCE; CLIP architecture | HW (parcial) | 34 | ⏳ pendente | + | Supl. CLIP (Radford 2021) + SimCLR |
| Representation II | BLIP; LLaVA; InstructBLIP; projection layers | HW | 35 | ⏳ pendente | + | Supl. BLIP (Li 2022) + LLaVA paper |
| Alignment I | Cross-attention; hard negative mining; contrastive vs generative | HW | 36 | ⏳ pendente | + | Supl. cmu-mmml.github.io leituras |
| Alignment II | Multimodal transformers; Perceiver; ViLBERT; fusion positions | HW | 37 | ⏳ pendente | + | Supl. ViLBERT + Perceiver |
| Reasoning I | Visual QA; spatial reasoning gaps; visual CoT | Project (parcial) | 38 | ⏳ pendente | + | Supl. PIQA (Bisk 2020) + GQA dataset |
| Reasoning II | Scene graphs; GNN multimodal; neuro-symbolic | Project | 39 | ⏳ pendente | + | Supl. scene graph survey + GNN papers |
| Generation I | Diffusion models (DDPM, DDIM); latent diffusion; CFG | Project | 40 | ⏳ pendente | + | Supl. DDPM (Ho 2020) + Stable Diffusion |
| Generation II | Encoder-decoder captioning; COCO metrics; cross-modal retrieval | Project | 41 | ⏳ pendente | + | Supl. BLIP-2 + COCO captioning papers |
| Transference | Co-learning; zero/few-shot multimodal; multi-task | Project | 42 | ⏳ pendente | + | Supl. co-learning survey + CLIP zero-shot |
| Quantification | Multimodal VAE; Deep CCA; shared vs private repr. | Project | 43 | ⏳ pendente | + | Supl. MVAE + Deep CCA paper |
| Fusion methods | Tensor fusion; Tucker decomp.; multi-kernel; gated fusion | Project | 44 | ⏳ pendente | + | Supl. TFN (Zadeh) + low-rank fusion |
| Applications I | Affect recognition; language grounding; CMU-MOSI/MOSEI | Project | 45 | ⏳ pendente | + | Supl. Morency lab publications |
| Applications II | VLN; R2R; embodied agents; CLAW lab (Bisk) | Project | 46 | ⏳ pendente | + | Supl. R2R paper + PIQA + Bisk publications |
| Frontier | Multimodal LLMs (GPT-4V, Gemini, Idefics); interleaved VLMs | Project | 47 | ⏳ pendente | + | Supl. GPT-4V system card + Gemini tech report |
| Capstone | Sistema vision-language ponta a ponta | Capstone | 48 | ⏳ pendente | + | Bridge: síntese de todo M3 |
