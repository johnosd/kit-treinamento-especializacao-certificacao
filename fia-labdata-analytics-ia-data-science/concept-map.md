# Concept Map

Diagramas Mermaid para navegar pelas relações centrais do programa.

---

## 1. Relações Entre Conceitos

```mermaid
flowchart TD
    Data[Dados] --> Structured[Dados Estruturados]
    Data --> Unstructured[Dados Não Estruturados]
    Structured --> EDA[EDA]
    Structured --> Supervised[Aprendizado Supervisionado]
    Structured --> Unsupervised[Aprendizado Não Supervisionado]
    EDA --> FeatureEngineering[Feature Engineering]
    FeatureEngineering --> Regression[Regressão]
    FeatureEngineering --> Classification[Classificação]
    FeatureEngineering --> TimeSeries[Séries Temporais]
    Supervised --> Regression
    Supervised --> Classification
    Unsupervised --> Clustering[Clustering]
    Regression --> Validation[Validação]
    Classification --> Validation
    TimeSeries --> TemporalValidation[Validação Temporal]
    Clustering --> ClusterAnalysis[Análise de Segmentos]
    Validation --> Explainability[Explicabilidade]
    Explainability --> MLOps[MLOps]
    TemporalValidation --> MLOps
    ClusterAnalysis --> BusinessAction[Ação de Negócio]
    MLOps --> Monitoring[Monitoramento]
```

---

## 2. Arquitetura de Treinamento ML

```mermaid
flowchart LR
    Raw[Dados brutos] --> Ingest[Ingestão]
    Ingest --> Validate[Validação de schema e qualidade]
    Validate --> Split[Split treino/validação/teste]
    Split --> Transform[Preprocessamento em Pipeline]
    Transform --> Train[Treinamento]
    Train --> Tune[Tuning]
    Tune --> Eval[Avaliação]
    Eval --> Explain[Explicabilidade]
    Explain --> Registry[Model Registry]
    Registry --> Deploy[Deploy]
    Deploy --> Monitor[Monitoramento]
    Monitor --> Drift[Drift e degradação]
    Drift --> Retrain[Retreinamento controlado]
    Retrain --> Train
```

---

## 3. Serving Pipeline

```mermaid
sequenceDiagram
    participant User as Usuário/Sistema
    participant API as API de Predição
    participant FE as Feature Pipeline
    participant Model as Modelo
    participant Obs as Observability
    participant Store as Logs/Feature Store

    User->>API: request
    API->>FE: valida e transforma entrada
    FE->>Model: features
    Model->>API: predição + score
    API->>Obs: latência, erro, payload resumido
    API->>Store: predição, versão, features permitidas
    API->>User: resposta
    Obs->>Store: métricas agregadas
```

---

## 4. RAG Pipeline

```mermaid
flowchart TD
    Docs[Documentos] --> Parse[Parsing e limpeza]
    Parse --> Chunk[Chunking]
    Chunk --> Embed[Embeddings]
    Embed --> Index[Vector Index]
    Query[Pergunta] --> QueryEmbed[Embedding da pergunta]
    QueryEmbed --> Retrieve[Retrieval]
    Index --> Retrieve
    Retrieve --> Rerank[Reranking opcional]
    Rerank --> Context[Contexto selecionado]
    Context --> Prompt[Prompt com instruções e citações]
    Query --> Prompt
    Prompt --> LLM[LLM]
    LLM --> Answer[Resposta grounded]
    Answer --> Eval[Avaliação: factualidade, cobertura, citação]
    Eval --> Logs[Logs e melhoria do corpus]
```

---

## 5. Agentic Workflow

```mermaid
flowchart TD
    Goal[Objetivo] --> Planner[Planejador]
    Planner --> State[Estado/Memória]
    State --> ToolSelect[Seleção de ferramenta]
    ToolSelect --> ToolCall[Tool Calling]
    ToolCall --> Observation[Observação]
    Observation --> Critic[Crítico/Avaliador]
    Critic -->|suficiente| Final[Resposta/ação final]
    Critic -->|insuficiente| Planner
    ToolCall --> Guardrails[Guardrails]
    Guardrails --> Logs[Logs e auditoria]
    Final --> Logs
```

---

## 6. Multimodal Pipeline

```mermaid
flowchart LR
    Text[Texto] --> TextEncoder[Text Encoder]
    Image[Imagem] --> VisionEncoder[Vision Encoder]
    Audio[Áudio] --> AudioEncoder[Audio Encoder]
    TextEncoder --> Fusion[Fusão multimodal]
    VisionEncoder --> Fusion
    AudioEncoder --> Fusion
    Fusion --> Reasoning[Raciocínio/Modelo generativo]
    Reasoning --> OutputText[Texto]
    Reasoning --> OutputImage[Imagem]
    Reasoning --> Action[Ação/Ferramenta]
    OutputText --> Eval[Avaliação]
    OutputImage --> Eval
    Action --> Eval
```

---

## 7. Capstone Architecture

```mermaid
flowchart TD
    Problem[Problema de negócio] --> Metrics[Métricas técnicas e de negócio]
    Metrics --> DataPlan[Plano de dados]
    DataPlan --> Baseline[Baseline simples]
    Baseline --> Advanced[Modelo avançado]
    Advanced --> Evaluation[Avaliação e benchmark]
    Evaluation --> Architecture[Arquitetura de produção]
    Architecture --> Risk[Riscos, ética e failure modes]
    Risk --> Cost[Custo computacional e operacional]
    Cost --> Defense[Defesa técnica]
```
