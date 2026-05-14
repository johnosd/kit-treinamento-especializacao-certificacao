# 06 — Concept Map

## 1. Trilha Curricular

```mermaid
flowchart TD
    Prereq[ML + NLP + PyTorch + Math] --> LM[Language Modeling]
    LM --> Token[Tokenization + Embeddings]
    Token --> Transformer[Transformer]
    Transformer --> Pretrain[Pretraining Objectives]
    Pretrain --> Data[Pretraining Data Curation]
    Data --> Eval[Evaluation Harness]
    Transformer --> Prompt[Prompting + ICL]
    Prompt --> PEFT[Fine-tuning + PEFT/LoRA]
    Prompt --> RAG[RAG]
    RAG --> Tools[Tool Use]
    PEFT --> Alignment[RLHF + DPO]
    Transformer --> Scaling[Scaling Laws]
    Scaling --> TrainSys[Parallel Training Systems]
    TrainSys --> Serving[LLM Serving]
    Serving --> Efficient[Efficient Inference]
    Efficient --> Ops[Observability + Online Maintenance]
    Transformer --> Multi[Multimodal Learning]
    Multi --> Capstone[Capstone]
    Ops --> Capstone
    Alignment --> Capstone
```

---

## 2. Transformer Internals

```mermaid
flowchart LR
    Tokens[Tokens] --> Embed[Token Embeddings]
    Embed --> Pos[Positional Encoding / RoPE]
    Pos --> Blocks[Transformer Blocks]
    Blocks --> Attn[Multi-Head Self-Attention]
    Attn --> MLP[Feed-forward / MLP]
    MLP --> Norm[LayerNorm + Residuals]
    Norm --> Logits[Logits]
    Logits --> Softmax[Softmax]
    Softmax --> Decode[Decoding]
```

---

## 3. Pretraining Data Pipeline

```mermaid
flowchart TD
    Web[Raw Web / Corpora] --> Extract[Extraction]
    Extract --> Filter[Quality Filtering]
    Filter --> Dedup[Deduplication]
    Dedup --> Safety[PII/Safety Filtering]
    Safety --> Mix[Data Mixture]
    Mix --> Tokenize[Tokenization]
    Tokenize --> Shards[Training Shards]
    Shards --> Docs[Datasheet + Provenance]
```

---

## 4. RAG Pipeline

```mermaid
flowchart TD
    Docs[Documents] --> Chunk[Chunking]
    Chunk --> Embed[Embeddings]
    Embed --> Index[Vector Index]
    Query[User Query] --> QEmbed[Query Embedding]
    QEmbed --> Retrieve[Retrieve Top-k]
    Index --> Retrieve
    Retrieve --> Rerank[Rerank]
    Rerank --> Context[Grounding Context]
    Context --> Prompt[Prompt Assembly]
    Query --> Prompt
    Prompt --> LLM[LLM]
    LLM --> Answer[Answer + Citations]
    Answer --> Eval[Faithfulness / Relevance / Coverage]
    Eval --> Logs[Observability]
```

---

## 5. LLM Serving Pipeline

```mermaid
sequenceDiagram
    participant Client
    participant Router
    participant Queue
    participant Engine as vLLM/Serving Engine
    participant GPU
    participant Obs as Observability

    Client->>Router: request
    Router->>Queue: admission + priority
    Queue->>Engine: dynamic batch
    Engine->>GPU: prefill + decode
    GPU->>Engine: tokens
    Engine->>Obs: latency, tokens, errors, cost
    Engine->>Client: streamed response
```

---

## 6. Alignment Flow

```mermaid
flowchart TD
    Base[Base LM] --> SFT[Supervised Fine-Tuning]
    SFT --> Pref[Preference Data]
    Pref --> Reward[Reward Model]
    Reward --> RLHF[RLHF / PPO]
    Pref --> DPO[DPO]
    RLHF --> Eval[Human + Automatic Eval]
    DPO --> Eval
    Eval --> Safety[Safety + Red Team]
    Safety --> Deploy[Deployment Decision]
```

---

## 7. Multimodal Learning

```mermaid
flowchart LR
    Text[Text] --> TextEnc[Text Encoder]
    Image[Image] --> VisionEnc[Vision Encoder]
    Audio[Audio] --> AudioEnc[Audio Encoder]
    TextEnc --> Align[Shared Representation / Alignment]
    VisionEnc --> Align
    AudioEnc --> Align
    Align --> Fusion[Fusion]
    Fusion --> Tasks[Captioning / Retrieval / QA / Classification]
    Tasks --> Eval[Task + Robustness Eval]
```

---

## 8. Capstone System

```mermaid
flowchart TD
    Problem[Research/Application Question] --> Baseline[Strong Baseline]
    Baseline --> Method[Method / System]
    Method --> Eval[Evaluation Harness]
    Eval --> Bench[Benchmark]
    Bench --> Cost[Cost + Latency + Memory]
    Cost --> Risks[Failure Modes + Safety]
    Risks --> Report[Final Report]
    Report --> Defense[Technical Defense]
```
