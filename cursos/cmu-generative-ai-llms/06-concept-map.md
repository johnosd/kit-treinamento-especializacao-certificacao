# Mapas Conceituais — CMU Generative AI & LLMs Kit

> 5 diagramas Mermaid cobrindo o stack completo do programa.

---

## Diagrama 1 — Certificate Program Stack (macro)

```mermaid
flowchart TD
    subgraph M1["M1 — LLMs Methods & Applications (S01–S16)"]
        A1[Transformer Architecture] --> A2[Pre-training CLM/MLM]
        A2 --> A3[Fine-tuning / Instruction Tuning]
        A3 --> A4[RLHF / DPO]
        A4 --> A5[PEFT / LoRA]
        A2 --> A6[ICL / CoT / Tool Use]
        A6 --> A7[RAG Pipeline]
        A3 --> A8[Evaluation: HELM / BIG-Bench]
        A4 --> A9[Safety & Alignment]
        A2 --> A10[Scaling Laws]
    end

    subgraph M2["M2 — LLM Systems (S17–S32)"]
        B1[GPU Architecture / Roofline] --> B2[CUDA Kernels / Autograd]
        B2 --> B3[Operator Fusion / Triton]
        B3 --> B4[FlashAttention I & II]
        B1 --> B5[Continuous Batching / KV Cache]
        B5 --> B6[PagedAttention / vLLM]
        B1 --> B7[Pipeline Parallelism]
        B7 --> B8[Tensor Parallelism]
        B8 --> B9[ZeRO / FSDP]
        B5 --> B10[Quantization INT8/INT4]
        B10 --> B11[QLoRA]
        B9 --> B12[MoE Systems]
        B6 --> B13[SGLang / Disagg. Serving]
        B4 --> B6
    end

    subgraph M3["M3 — Multimodal ML (S33–S48)"]
        C1[6 Challenges Framework] --> C2[Unimodal Encoders: ViT / BERT / wav2vec]
        C2 --> C3[Contrastive: CLIP / InfoNCE]
        C3 --> C4[VLMs: BLIP / LLaVA]
        C4 --> C5[Cross-Modal Alignment]
        C5 --> C6[Multimodal Transformers: ViLBERT / Perceiver]
        C6 --> C7[Visual Reasoning / CoT]
        C2 --> C8[Diffusion: DDPM / Stable Diffusion]
        C8 --> C9[Captioning / Retrieval: BLIP-2]
        C6 --> C10[Tensor Fusion / Deep CCA]
        C10 --> C11[Affect Recognition / VLN]
        C4 --> C12[Frontier VLMs: GPT-4V / Gemini]
    end

    M1 -->|"Algoritmos base para"| M2
    M1 -->|"ICL / tool use para"| M3
    M2 -->|"Serving infra para"| M3
    M3 --> CAP[Capstone: Vision-Language Pipeline S48]
```

---

## Diagrama 2 — LLM Training Pipeline

```mermaid
flowchart LR
    RAW["Raw Text Corpus\n(Common Crawl, Books, Code)"]
    --> FILTER["Data Curation\n(dedup, filter, quality)"]
    --> TOK["Tokenization\n(BPE / SentencePiece)"]
    --> PRETRAIN

    subgraph PRETRAIN["Pre-training (CLM)"]
        direction TB
        EMB["Token + Positional\nEmbedding (RoPE)"] --> LAYERS
        subgraph LAYERS["Transformer Layers × N"]
            direction LR
            ATTN["MHA / GQA\n(FlashAttention)"] --> FFN["FFN\n(SwiGLU)"]
        end
        LAYERS --> PROJ["LM Head\n(linear + softmax)"]
    end

    PRETRAIN --> SFT["SFT\n(Instruction Tuning)"]
    SFT --> RM["Reward Model\nTraining"]
    RM --> PPO["PPO / DPO\n(Alignment)"]
    PPO --> DEPLOY["Deployed Model"]

    PEFT["LoRA / QLoRA\n(optional adapter)"] -.-> SFT
    EVAL["HELM / BIG-Bench\nEvaluation"] -.-> DEPLOY
```

---

## Diagrama 3 — LLM Systems Stack (Serving)

```mermaid
flowchart TB
    subgraph CLIENT["Client Layer"]
        REQ["Incoming Requests\n(variable seq_len)"]
    end

    subgraph SCHED["Scheduler (vLLM)"]
        CB["Continuous Batching\n(Orca-style)"]
        PRIO["Request Prioritization\n+ Preemption"]
    end

    subgraph MEM["Memory Management"]
        PA["PagedAttention\n(KV block table)"]
        KVPOOL["Physical KV Cache\n(block pool)"]
    end

    subgraph COMPUTE["Compute Layer"]
        ATTN2["FlashAttention\n(IO-aware tiling)"]
        QUANT["INT8/INT4 Weights\n(GPTQ / AWQ)"]
        GQA2["GQA/MQA\n(reduced KV heads)"]
        SPEC["Speculative Decoding\n(draft model)"]
    end

    subgraph DIST["Distributed (large models)"]
        TP["Tensor Parallelism\n(Megatron split)"]
        PP2["Pipeline Parallelism\n(layer stages)"]
        ZeRO2["ZeRO / FSDP\n(param sharding)"]
    end

    subgraph FRONTEND["Frontend Layer"]
        SGLANG["SGLang\n(RadixAttention +\nstructured generation)"]
        DISAGG["Disaggregated Serving\n(prefill ↔ decode split)"]
    end

    REQ --> SCHED
    CB --> PA
    PRIO --> KVPOOL
    PA --> ATTN2
    ATTN2 --> QUANT
    QUANT --> GQA2
    GQA2 --> SPEC
    SPEC --> TP
    TP --> PP2
    PP2 --> ZeRO2
    SGLANG --> CB
    DISAGG --> SCHED
```

---

## Diagrama 4 — RAG Pipeline

```mermaid
flowchart LR
    subgraph OFFLINE["Offline: Index Construction"]
        DOCS["Document Corpus"] --> CHUNK["Chunking\n(overlap, size)"]
        CHUNK --> EMBED["Dense Encoder\n(DPR / BGE / E5)"]
        EMBED --> INDEX["FAISS Index\n(IVF + HNSW)"]
    end

    subgraph ONLINE["Online: Query-time"]
        Q["User Query"] --> QENC["Query Encoder\n(same encoder)"]
        QENC --> RETR["Top-K Retrieval\n(ANN search)"]
        INDEX --> RETR
        RETR --> RERANK["Re-ranker\n(cross-encoder, optional)"]
        RERANK --> CTX["Context Assembly\n(prompt + retrieved docs)"]
        CTX --> GEN["Generator LLM\n(decoder-only)"]
        GEN --> ANS["Answer"]
    end

    Q -.-> GEN

    subgraph PITFALLS["Known Failure Modes"]
        P1["Lost in the Middle\n(positional bias in context)"]
        P2["Retrieval Quality\n(garbage in, garbage out)"]
        P3["Hallucination\n(model ignores context)"]
    end

    ANS -.-> PITFALLS
```

---

## Diagrama 5 — Multimodal Architecture (Vision-Language)

```mermaid
flowchart TB
    subgraph ENCODERS["Unimodal Encoders"]
        IMG["Image\n→ ViT (patch embeddings)"]
        TXT["Text\n→ Tokenizer + Embedding"]
        AUD["Audio (optional)\n→ wav2vec / Whisper"]
    end

    subgraph ALIGN["Alignment Module"]
        direction LR
        CLIP2["Contrastive Alignment\n(CLIP / InfoNCE)\n→ shared embedding space"]
        QFORM["Q-Former (BLIP-2)\n→ learnable queries\nbridging vision↔LLM"]
        PROJ["Linear Projection\n(LLaVA)\n→ direct visual tokens"]
    end

    subgraph FUSION["Fusion Strategy"]
        EF["Early Fusion\n(concatenate before attention)"]
        CF["Cross-Attention\n(ViLBERT / Perceiver)"]
        LF["Late Fusion\n(combine predictions)"]
        TF["Tensor Fusion\n(TFN outer product)"]
    end

    subgraph LLM2["Language Model Backbone"]
        DEC["Decoder-only LLM\n(LLaMA / Mistral)"]
    end

    subgraph TASKS["Downstream Tasks"]
        VQA2["Visual QA"]
        CAP["Image Captioning"]
        RET["Cross-Modal Retrieval"]
        GEN2["Text-to-Image Generation\n(Diffusion)"]
        VLN2["Vision-Language Navigation"]
        AFF["Affect Recognition"]
    end

    IMG --> ALIGN
    TXT --> ALIGN
    AUD --> ALIGN
    CLIP2 --> FUSION
    QFORM --> DEC
    PROJ --> DEC
    FUSION --> DEC
    DEC --> TASKS

    subgraph TRAINING["Training Objectives"]
        ITC["ITC: Image-Text Contrastive"]
        ITM["ITM: Image-Text Matching"]
        LMO["LM: Causal Language Modeling"]
        DDPM2["Diffusion: Noise Prediction"]
    end

    ALIGN -.-> TRAINING
    DEC -.-> TRAINING
```
