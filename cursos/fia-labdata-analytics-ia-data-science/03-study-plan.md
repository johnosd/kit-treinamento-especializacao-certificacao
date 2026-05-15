# Study Plan — 64 Semanas

Plano autodidata baseado na duração oficial de 16 meses e na carga oficial de 360 horas. A grade pública não fornece semanas oficiais; portanto, este cronograma é uma decomposição pedagógica inferida e alinhada à matriz FIA/Labdata.

**Carga recomendada:** 8-12h/semana  
**Proporção:** 65% engenharia / 35% teoria  
**Stack:** Python, Google Colab, pandas, scikit-learn, TensorFlow/Keras, PyTorch, Hugging Face, XGBoost, LightGBM, CatBoost, SHAP/LIME, MLflow, LLM APIs, RAG tooling  

---

## Rotina Semanal Padrão

| Atividade | Tempo | Evidência |
|---|---:|---|
| Teoria | 2h | notas com fórmulas, premissas e limitações |
| Leitura técnica/papers/docs | 1-2h | resumo crítico e perguntas |
| Implementação | 3-4h | notebook ou módulo Python reproduzível |
| Lab/mini-projeto | 2-3h | entrega incremental |
| Flashcards/revisão | 45-60min | 10-20 cards e mistake log |
| Assessment | 30-60min | respostas abertas, análise de tradeoffs e debugging |

---

## Fase 1 — Fundamentos, Python, Estatística e EDA

### Semana 01 — Ciência de Dados, Analytics e IA

- **Teoria:** diferença entre análise, modelagem, ML, DL e GenAI; ciclo de vida de problemas orientados a dados.
- **Leitura:** documentação scikit-learn sobre model selection; TensorFlow overview; PyTorch overview.
- **Implementação:** montar ambiente Colab/local, versionar notebooks e criar estrutura de projetos.
- **Lab:** mapa de um problema real: objetivo, dados, métrica, baseline, riscos.
- **Mini-projeto:** especificação de um problema de negócio para análise preditiva.
- **Flashcards:** vocabulário central de Data Science e IA.
- **Revisão:** identificar gaps em estatística, Python e álgebra.
- **Assessment:** explicar por que acurácia, correlação e causalidade não são equivalentes.

### Semana 02 — Python para Análise

- **Teoria:** objetos, funções, módulos, ambientes e reprodutibilidade.
- **Leitura:** documentação Python, pandas e NumPy.
- **Implementação:** funções utilitárias para ingestão e validação simples de dados.
- **Lab:** notebook com leitura, schema report e validações.
- **Mini-projeto:** carregar 3 formatos de dados e padronizar schema.
- **Flashcards:** tipos, funções, listas, vetores, DataFrames.
- **Revisão:** erros comuns de indexação e mutabilidade.
- **Assessment:** debugar pipeline com tipos inconsistentes.

### Semana 03 — Estatística Descritiva

- **Teoria:** população, amostra, variáveis, distribuição, medidas de posição e dispersão.
- **Leitura:** SciPy stats docs e scikit-learn preprocessing.
- **Implementação:** gerar perfil estatístico de dataset tabular.
- **Lab:** relatório de distribuição, outliers e missingness.
- **Mini-projeto:** construir data quality report.
- **Flashcards:** média, mediana, moda, quartis, variância, desvio padrão.
- **Revisão:** sensibilidade a outliers.
- **Assessment:** escolher estatísticas robustas para dados assimétricos.

### Semana 04 — Estatística Inferencial

- **Teoria:** amostragem, estimadores, intervalo de confiança, teste de hipótese e p-valor.
- **Leitura:** SciPy hypothesis tests; statsmodels documentation.
- **Implementação:** simular amostras e intervalos de confiança.
- **Lab:** teste A/B simples com diagnóstico de premissas.
- **Mini-projeto:** avaliar diferença entre grupos em dataset real.
- **Flashcards:** erro tipo I/II, p-valor, poder, IC.
- **Revisão:** confundir significância estatística com relevância prática.
- **Assessment:** justificar teste estatístico e premissas.

### Semana 05 — Estruturação de Dados

- **Teoria:** schema, chaves, granularidade, joins, leakage por agregação.
- **Leitura:** pandas merge/groupby docs.
- **Implementação:** pipeline de limpeza, tipagem, joins e agregações.
- **Lab:** reproduzir left/right/inner/full join e validar cardinalidade.
- **Mini-projeto:** construir dataset analítico único.
- **Flashcards:** chaves, cardinalidade, join, grain.
- **Revisão:** checar duplicidade e explosão de linhas.
- **Assessment:** diagnosticar erro de join que infla target.

### Semana 06 — EDA Univariada e Bivariada

- **Teoria:** exploração sistemática e relação entre variáveis.
- **Leitura:** pandas profiling alternatives; scikit-learn inspection.
- **Implementação:** funções de EDA para variáveis numéricas e categóricas.
- **Lab:** matriz de associação e análise bivariada.
- **Mini-projeto:** relatório técnico de EDA.
- **Flashcards:** outlier, missingness, associação, correlação.
- **Revisão:** diferença entre correlação e dependência.
- **Assessment:** propor transformação para distribuição problemática.

### Semana 07 — Visualização de Dados

- **Teoria:** codificação visual, comparação, distribuição, composição e tendência.
- **Leitura:** matplotlib/seaborn docs.
- **Implementação:** biblioteca local de gráficos reutilizáveis.
- **Lab:** dashboard estático com narrativas técnicas.
- **Mini-projeto:** visualizações para decisão executiva.
- **Flashcards:** histograma, boxplot, barras, linha, heatmap.
- **Revisão:** evitar gráfico decorativo sem pergunta analítica.
- **Assessment:** escolher gráfico para 5 perguntas distintas.

### Semana 08 — Assessment de Fundamentos

- **Teoria:** revisão integradora.
- **Leitura:** refazer notas e lacunas.
- **Implementação:** pipeline completo de ingestão, limpeza e EDA.
- **Lab:** análise exploratória reprodutível de dataset novo.
- **Mini-projeto:** relatório final da fase 1.
- **Flashcards:** consolidar 80-120 cards.
- **Revisão:** mistake log.
- **Assessment:** defesa oral/escrita da análise.

---

## Fase 2 — Regressão, Árvores, Ensembles e Validação

### Semanas 09-10 — Regressão Linear

- **Teoria:** mínimos quadrados, coeficientes, resíduos, inferência, colinearidade.
- **Leitura:** statsmodels OLS; scikit-learn LinearRegression.
- **Implementação:** regressão do zero e com biblioteca.
- **Lab:** diagnóstico de resíduos, VIF e seleção.
- **Mini-projeto:** modelo de projeção com análise de negócio.
- **Assessment:** interpretar coeficientes e riscos de causalidade indevida.

### Semanas 11-12 — Validação e Métricas de Regressão

- **Teoria:** holdout, cross-validation, nested CV, MAE, MSE, RMSE, MAPE, R².
- **Leitura:** scikit-learn model evaluation.
- **Implementação:** framework de avaliação com split reproduzível.
- **Lab:** comparar métricas sob outliers.
- **Mini-projeto:** relatório de benchmark regressivo.
- **Assessment:** escolher métrica para cenários de negócio.

### Semanas 13-14 — Árvores de Regressão

- **Teoria:** splits, impurity, bias-variance, hiperparâmetros.
- **Leitura:** scikit-learn DecisionTreeRegressor.
- **Implementação:** árvore com grid/random search.
- **Lab:** visualizar árvore, profundidade e overfitting.
- **Mini-projeto:** baseline árvore versus regressão linear.
- **Assessment:** explicar instabilidade e regularização de árvores.

### Semanas 15-16 — Random Forest e Bagging

- **Teoria:** bootstrap, agregação, decorrelação e feature importance.
- **Leitura:** Breiman Random Forests; scikit-learn ensembles.
- **Implementação:** Random Forest com validação.
- **Lab:** analisar importância e estabilidade.
- **Mini-projeto:** benchmark RF versus árvore única.
- **Assessment:** quando RF melhora e quando complica operação.

### Semanas 17-18 — Boosting

- **Teoria:** boosting sequencial, gradiente funcional, regularização.
- **Leitura:** XGBoost, LightGBM e CatBoost docs.
- **Implementação:** treino e tuning de boosting.
- **Lab:** comparação XGBoost/LightGBM/CatBoost.
- **Mini-projeto:** leaderboard interno com baseline honesto.
- **Assessment:** discutir overfitting, leakage e custo.

### Semanas 19-20 — Explicabilidade e Diagnóstico

- **Teoria:** interpretabilidade global/local, SHAP, LIME, PDP, ICE.
- **Leitura:** SHAP docs, LIME paper/repo.
- **Implementação:** relatório interpretável para modelo supervisionado.
- **Lab:** explicar previsões locais e detectar comportamento espúrio.
- **Mini-projeto:** model card de regressão.
- **Assessment:** quando explicabilidade engana.

---

## Fase 3 — Séries Temporais, Classificação e Segmentação

### Semanas 21-24 — Séries Temporais

- **Teoria:** estacionariedade, autocorrelação, AR/MA/ARMA/ARIMA/SARIMA, validação temporal.
- **Leitura:** statsmodels time series docs.
- **Implementação:** forecasting baseline, ARIMA/SARIMA e features temporais.
- **Lab:** backtesting sem leakage.
- **Mini-projeto:** previsão com benchmark temporal.
- **Assessment:** justificar split temporal e horizonte.

### Semanas 25-27 — Classificação

- **Teoria:** probabilidade, regressão logística, árvores, métricas e calibração.
- **Leitura:** scikit-learn classification metrics e calibration.
- **Implementação:** pipeline de classificação com threshold tuning.
- **Lab:** matriz de confusão, ROC, PR curve, KS e calibração.
- **Mini-projeto:** classificador com custo de erro assimétrico.
- **Assessment:** explicar por que AUC não define política de decisão.

### Semana 28 — Segmentação

- **Teoria:** distância, padronização, hierárquico, k-means, k-medoids, DBSCAN.
- **Leitura:** scikit-learn clustering.
- **Implementação:** clustering com validação exploratória.
- **Lab:** dendrograma, silhouette e análise de clusters.
- **Mini-projeto:** segmentação acionável para negócio.
- **Assessment:** diferenciar cluster estatístico de persona útil.

---

## Fase 4 — AutoML, MLOps e Projeto Estruturado

### Semanas 29-30 — AutoML

- **Teoria:** busca automatizada, espaço de modelos, risco de leakage e validação.
- **Leitura:** Auto-sklearn/FLAML ou framework escolhido.
- **Implementação:** AutoML comparado a baseline manual.
- **Lab:** budget de busca e análise de resultados.
- **Mini-projeto:** relatório de quando AutoML ajuda.
- **Assessment:** limites de AutoML em produção.

### Semanas 31-32 — MLOps

- **Teoria:** lifecycle, versionamento, data/model drift, deployment, observability.
- **Leitura:** MLflow docs; Evidently docs; Kubernetes basics se aplicável.
- **Implementação:** tracking de experimentos e model registry local.
- **Lab:** monitoramento simples de drift e qualidade.
- **Mini-projeto:** pipeline ML versionado.
- **Assessment:** plano de rollback e monitoramento.

### Semanas 33-34 — Projeto Dados Estruturados

- **Teoria:** integração de modelagem, engenharia e comunicação.
- **Leitura:** revisar docs das bibliotecas usadas.
- **Implementação:** projeto completo de dados estruturados.
- **Lab:** benchmark, explicabilidade, monitoring stub.
- **Mini-projeto:** entrega do Projeto 1.
- **Assessment:** defesa técnica com tradeoffs.

---

## Fase 5 — Deep Learning, CNNs, RNNs e NLP Clássico

### Semanas 35-36 — Perceptron, MLP e Otimização

- **Teoria:** tensores, forward pass, loss, gradiente, backpropagation.
- **Leitura:** Deep Learning Book; PyTorch/TensorFlow tutorials oficiais.
- **Implementação:** MLP do zero e em framework.
- **Lab:** overfitting, regularização e curvas de treino.
- **Mini-projeto:** classificador neural simples.
- **Assessment:** explicar backpropagation sem biblioteca.

### Semanas 37-38 — TensorFlow/Keras e PyTorch

- **Teoria:** modelos, camadas, otimizadores, losses e datasets.
- **Leitura:** TensorFlow/Keras e PyTorch official docs.
- **Implementação:** mesmo modelo em Keras e PyTorch.
- **Lab:** profiling básico, seed, determinismo e checkpoints.
- **Mini-projeto:** template de treino reproduzível.
- **Assessment:** comparar abstrações e riscos.

### Semanas 39-40 — CNNs

- **Teoria:** convolução, pooling, invariância, regularização, transfer learning.
- **Leitura:** papers clássicos de CNN/ResNet e docs Keras/PyTorch.
- **Implementação:** CNN para classificação de imagem.
- **Lab:** augmentation, dropout, early stopping e GradCAM.
- **Mini-projeto:** classificador visual interpretável.
- **Assessment:** explicar por que CNN generaliza melhor que MLP em imagem.

### Semanas 41-42 — RNNs e LSTMs

- **Teoria:** sequência, estado oculto, LSTM gates, vanishing/exploding gradients.
- **Leitura:** LSTM paper e docs de recurrent layers.
- **Implementação:** RNN/LSTM para sequência temporal ou texto.
- **Lab:** comparação com baseline não neural.
- **Mini-projeto:** previsão/sequência com LSTM.
- **Assessment:** quando RNN é inferior a Transformer.

### Semanas 43-44 — NLP Clássico e Embeddings

- **Teoria:** tokenização, Word2Vec, embeddings, similaridade e representação.
- **Leitura:** Word2Vec paper; Hugging Face tokenizers docs.
- **Implementação:** pipeline NLP com embeddings clássicos.
- **Lab:** análise de sentimento ou classificação textual.
- **Mini-projeto:** baseline NLP antes de LLM.
- **Assessment:** tradeoffs entre bag-of-words, Word2Vec e Transformer.

---

## Fase 6 — IA Generativa, Transformers, GPT e Prompts

### Semanas 45-46 — Generative Models

- **Teoria:** discriminativo versus generativo, GAN, DCGAN, diffusion.
- **Leitura:** GAN, DCGAN, DDPM/Stable Diffusion references.
- **Implementação:** experimento pequeno com modelo generativo.
- **Lab:** comparar estabilidade, modo colapso e qualidade.
- **Mini-projeto:** geração de dados sintéticos ou imagem.
- **Assessment:** quando dado sintético degrada modelo.

### Semanas 47-48 — Transformer Internals

- **Teoria:** self-attention, multi-head attention, positional encoding, scaling.
- **Leitura:** Attention Is All You Need; Hugging Face Transformers docs.
- **Implementação:** attention simplificado em PyTorch.
- **Lab:** visualizar pesos de attention e custo O(n²).
- **Mini-projeto:** notebook explicando Transformer.
- **Assessment:** limites de contexto e custo computacional.

### Semanas 49-50 — GPT, Tokenization e Inference

- **Teoria:** decoder-only, tokenization, sampling, temperature, top-k/top-p, KV cache.
- **Leitura:** OpenAI docs, Hugging Face generation docs, vLLM docs.
- **Implementação:** inferência com API e modelo open source pequeno.
- **Lab:** medir latência, custo, qualidade e variação.
- **Mini-projeto:** harness de prompts com logging.
- **Assessment:** explicar por que decoding muda comportamento.

### Semanas 51-52 — Prompt Engineering e Avaliação

- **Teoria:** prompt patterns, structured outputs, evals, adversarial prompts, hallucination.
- **Leitura:** OpenAI guides, Anthropic docs, avaliação BLEU/ROUGE/METEOR.
- **Implementação:** suite de avaliação de prompts.
- **Lab:** comparar zero/few-shot, schema e restrições.
- **Mini-projeto:** prompt benchmark com dataset pequeno.
- **Assessment:** por que avaliação automática pode falhar.

### Semanas 53-54 — Fine-Tuning, PEFT e Alignment

- **Teoria:** fine-tuning, LoRA, PEFT, RLHF, DPO, catastrophic forgetting.
- **Leitura:** LoRA, PEFT docs, RLHF/DPO papers.
- **Implementação:** fine-tuning leve quando ambiente permitir; caso contrário, estudo reprodutível com notebook.
- **Lab:** comparar prompting versus fine-tuning.
- **Mini-projeto:** plano técnico de adaptação de modelo.
- **Assessment:** decidir entre RAG, prompting e fine-tuning.

---

## Fase 7 — RAG, Agentes e Operação GenAI

### Semanas 55-56 — RAG

- **Teoria:** chunking, embeddings, vector search, reranking, grounding, citation quality.
- **Leitura:** Hugging Face, LangChain/LangGraph, vector database docs.
- **Implementação:** RAG baseline com corpus próprio.
- **Lab:** medir retrieval precision, answer quality e hallucination.
- **Mini-projeto:** RAG com avaliação.
- **Assessment:** diagnosticar resposta errada por retrieval ruim.

### Semanas 57-58 — Agentes e Tool Calling

- **Teoria:** agentes, planning, tools, memory, multi-agent risks.
- **Leitura:** OpenAI tools/function calling docs; LangGraph docs.
- **Implementação:** agente com ferramentas controladas.
- **Lab:** logs, limites, retries e segurança.
- **Mini-projeto:** agente para fluxo de análise de dados.
- **Assessment:** diferenciar workflow determinístico de agente.

### Semanas 59-60 — Serving, Observability e Custo

- **Teoria:** latency, throughput, batching, KV cache, quantization, vLLM, monitoring.
- **Leitura:** vLLM, PyTorch quantization, NVIDIA docs.
- **Implementação:** benchmark de inferência e custo.
- **Lab:** observabilidade de prompts, respostas, latência e erro.
- **Mini-projeto:** runbook de sistema GenAI.
- **Assessment:** plano de produção com failure modes.

---

## Fase 8 — Empreendedorismo Técnico e Capstone

### Semana 61 — Produto, Valor e Viabilidade

- **Teoria:** problema, usuário, métrica, ROI, risco e ética.
- **Leitura:** documentação de governança/risco de IA de fontes oficiais quando aplicável.
- **Implementação:** canvas técnico do capstone.
- **Lab:** análise de custo e viabilidade.
- **Mini-projeto:** proposta de capstone.
- **Assessment:** defender por que a solução precisa de IA.

### Semana 62 — Arquitetura do Capstone

- **Teoria:** arquitetura de dados, modelos, serving, segurança, avaliação.
- **Implementação:** technical spec e plano de experimentos.
- **Lab:** baseline mínimo.
- **Mini-projeto:** arquitetura revisável.
- **Assessment:** design review.

### Semana 63 — Implementação e Benchmark

- **Teoria:** validação de hipóteses, benchmark e documentação.
- **Implementação:** completar sistema e avaliação.
- **Lab:** testes de falha, custo, latência e qualidade.
- **Mini-projeto:** relatório técnico.
- **Assessment:** revisão crítica.

### Semana 64 — Defesa Técnica

- **Teoria:** síntese e comunicação.
- **Implementação:** refino final.
- **Lab:** apresentação e demo.
- **Mini-projeto:** entrega final.
- **Assessment:** defesa com perguntas sobre tradeoffs, limitações e próximos passos.
