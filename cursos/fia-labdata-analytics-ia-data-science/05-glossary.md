# Glossário Técnico Avançado

Cada termo inclui definição operacional, conceito/fórmula, aplicação, pitfalls e referência primária/oficial.

---

## A

### A/B Test

- **Definição:** experimento controlado que compara variantes para estimar efeito sobre uma métrica.
- **Conceito:** diferença estimada entre grupos, geralmente com intervalo de confiança e teste de hipótese.
- **Aplicação:** avaliar mudança de modelo, prompt, ranking, interface ou política.
- **Pitfalls:** amostra insuficiente, peeking, múltiplas comparações, métrica proxy ruim.
- **Referência:** SciPy stats: <https://docs.scipy.org/doc/scipy/reference/stats.html>

### Attention

- **Definição:** mecanismo que pondera representações de tokens conforme sua relevância contextual.
- **Conceito:** `Attention(Q,K,V)=softmax(QK^T/sqrt(d_k))V`.
- **Aplicação:** base dos Transformers e de LLMs modernos.
- **Pitfalls:** custo quadrático em sequência, interpretação ingênua de pesos, limite de contexto.
- **Referência:** Attention Is All You Need: <https://arxiv.org/abs/1706.03762>

### AutoML

- **Definição:** automação parcial da escolha de modelos, hiperparâmetros e pipelines.
- **Conceito:** busca sobre espaço de modelos sujeita a budget e função objetivo.
- **Aplicação:** baseline competitivo, exploração rápida e comparação inicial.
- **Pitfalls:** leakage, overfitting ao validation set, custo alto, baixa explicabilidade.
- **Referência:** Auto-sklearn: <https://automl.github.io/auto-sklearn/master/>

---

## B

### Backpropagation

- **Definição:** algoritmo para calcular gradientes em redes neurais por regra da cadeia.
- **Conceito:** propaga derivadas da loss em relação aos parâmetros camada a camada.
- **Aplicação:** treinamento de MLP, CNN, RNN e Transformers.
- **Pitfalls:** vanishing/exploding gradients, instabilidade numérica, bugs silenciosos de shape.
- **Referência:** Deep Learning Book: <https://www.deeplearningbook.org/>

### Bagging

- **Definição:** ensemble que treina modelos em amostras bootstrap e agrega predições.
- **Conceito:** reduz variância média quando modelos têm erros parcialmente descorrelacionados.
- **Aplicação:** Random Forest.
- **Pitfalls:** custo maior, menos interpretabilidade, não corrige viés alto sozinho.
- **Referência:** Random Forests: <https://link.springer.com/article/10.1023/A:1010933404324>

### Boosting

- **Definição:** ensemble sequencial que combina learners fracos para reduzir erro.
- **Conceito:** modelos sucessivos focam resíduos/gradientes dos anteriores.
- **Aplicação:** XGBoost, LightGBM, CatBoost em dados tabulares.
- **Pitfalls:** overfitting, tuning sensível, leakage em validação.
- **Referência:** XGBoost paper: <https://arxiv.org/abs/1603.02754>

---

## C

### Calibration

- **Definição:** alinhamento entre probabilidade prevista e frequência observada.
- **Conceito:** entre previsões com score 0,8, cerca de 80% deveriam ser positivas.
- **Aplicação:** risco de crédito, churn, saúde, decisão baseada em threshold.
- **Pitfalls:** AUC alta não garante calibração; reamostragem pode distorcer probabilidades.
- **Referência:** scikit-learn calibration: <https://scikit-learn.org/stable/modules/calibration.html>

### Chain of Thought

- **Definição:** técnica de prompting que induz decomposição explícita de raciocínio.
- **Conceito:** exemplos demonstram passos intermediários para tarefas complexas.
- **Aplicação:** raciocínio matemático, planejamento, análise multi-etapa.
- **Pitfalls:** pode gerar justificativas plausíveis mas falsas; nem sempre deve ser exposto ao usuário final.
- **Referência:** Chain-of-Thought Prompting: <https://arxiv.org/abs/2201.11903>

### Chunking

- **Definição:** divisão de documentos em unidades recuperáveis para RAG.
- **Conceito:** balanceia contexto semântico, tamanho do embedding e limite de tokens.
- **Aplicação:** indexação de documentos, busca vetorial, grounded generation.
- **Pitfalls:** chunks pequenos perdem contexto; grandes reduzem precisão; overlap excessivo aumenta custo.
- **Referência:** LangChain text splitters: <https://python.langchain.com/docs/concepts/text_splitters/>

### Confusion Matrix

- **Definição:** tabela de acertos e erros por classe prevista versus classe real.
- **Conceito:** TP, FP, TN, FN.
- **Aplicação:** classificação binária/multiclasse, análise de threshold.
- **Pitfalls:** acurácia pode ser enganosa em classes desbalanceadas.
- **Referência:** scikit-learn confusion matrix: <https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html>

### Cross-Validation

- **Definição:** validação por múltiplas divisões treino/teste para estimar generalização.
- **Conceito:** média e dispersão de métricas em folds.
- **Aplicação:** seleção de modelos e hiperparâmetros.
- **Pitfalls:** usar KFold comum em séries temporais, vazamento por preprocessamento fora do pipeline.
- **Referência:** scikit-learn cross-validation: <https://scikit-learn.org/stable/modules/cross_validation.html>

---

## D

### Data Leakage

- **Definição:** uso indevido de informação indisponível no momento real da predição.
- **Conceito:** variável, agregação, split ou preprocessamento carrega sinal do futuro/target.
- **Aplicação:** auditoria de pipelines supervisionados.
- **Pitfalls:** métricas excelentes em validação e desempenho ruim em produção.
- **Referência:** scikit-learn common pitfalls: <https://scikit-learn.org/stable/common_pitfalls.html>

### DBSCAN

- **Definição:** algoritmo de clustering baseado em densidade.
- **Conceito:** usa `eps` e `min_samples` para formar regiões densas e marcar ruído.
- **Aplicação:** clusters com formas não convexas e detecção de outliers.
- **Pitfalls:** sensível à escala e hiperparâmetros; difícil em alta dimensão.
- **Referência:** scikit-learn DBSCAN: <https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html>

### DPO

- **Definição:** Direct Preference Optimization, método de alinhamento por preferências sem RL explícito.
- **Conceito:** otimiza política para preferir respostas escolhidas sobre rejeitadas.
- **Aplicação:** alinhamento de LLMs com dados de preferência.
- **Pitfalls:** qualidade do dataset de preferências domina resultado; pode reduzir diversidade.
- **Referência:** DPO paper: <https://arxiv.org/abs/2305.18290>

### Drift

- **Definição:** mudança na distribuição de dados, relação entrada-saída ou qualidade do modelo ao longo do tempo.
- **Conceito:** data drift, concept drift e prediction drift.
- **Aplicação:** monitoramento de modelos em produção.
- **Pitfalls:** detectar drift não implica queda de valor; falso positivo gera retraining desnecessário.
- **Referência:** Evidently docs: <https://docs.evidentlyai.com/>

---

## E

### Embedding

- **Definição:** representação vetorial densa de item, token, texto, imagem ou entidade.
- **Conceito:** proximidade vetorial aproxima similaridade semântica ou estatística.
- **Aplicação:** NLP, RAG, recomendação, busca semântica.
- **Pitfalls:** viés, anisotropia, drift de modelo, avaliação superficial por cosine similarity.
- **Referência:** OpenAI embeddings docs: <https://platform.openai.com/docs/guides/embeddings>

### Explainability

- **Definição:** técnicas para explicar comportamento de modelos global ou localmente.
- **Conceito:** importância, atribuição, aproximação local, contrafactual.
- **Aplicação:** auditoria, confiança operacional, comunicação e compliance.
- **Pitfalls:** explicação não é causalidade; métodos podem ser instáveis.
- **Referência:** SHAP docs: <https://shap.readthedocs.io/>

---

## F

### Feature Engineering

- **Definição:** criação, transformação e seleção de variáveis para melhorar sinal preditivo.
- **Conceito:** codificação, agregação, normalização, interações e features temporais.
- **Aplicação:** dados tabulares, séries temporais e modelos supervisionados.
- **Pitfalls:** leakage, explosão dimensional, features frágeis em produção.
- **Referência:** scikit-learn preprocessing: <https://scikit-learn.org/stable/modules/preprocessing.html>

### Fine-Tuning

- **Definição:** ajuste de pesos de modelo pré-treinado em dados específicos.
- **Conceito:** atualiza parâmetros para aproximar distribuição/tarefa alvo.
- **Aplicação:** adaptação de LLMs, visão e NLP.
- **Pitfalls:** custo, overfitting, catastrophic forgetting, governança de dados.
- **Referência:** Hugging Face fine-tuning: <https://huggingface.co/docs/transformers/training>

---

## G

### GAN

- **Definição:** Generative Adversarial Network, arquitetura com gerador e discriminador em competição.
- **Conceito:** jogo minimax entre geração e discriminação.
- **Aplicação:** geração de imagens, dados sintéticos e tradução de domínio.
- **Pitfalls:** mode collapse, instabilidade, avaliação difícil.
- **Referência:** GAN paper: <https://arxiv.org/abs/1406.2661>

### GradCAM

- **Definição:** técnica de visualização que destaca regiões relevantes para decisão de CNN.
- **Conceito:** usa gradientes nas camadas convolucionais para mapa de ativação.
- **Aplicação:** interpretabilidade em visão computacional.
- **Pitfalls:** mapas podem ser imprecisos; não provam causalidade.
- **Referência:** Grad-CAM paper: <https://arxiv.org/abs/1610.02391>

---

## K

### K-Means

- **Definição:** algoritmo de clustering que minimiza soma de distâncias a centroides.
- **Conceito:** alterna atribuição de pontos e atualização de centroides.
- **Aplicação:** segmentação exploratória.
- **Pitfalls:** assume clusters aproximadamente esféricos; sensível à escala e inicialização.
- **Referência:** scikit-learn KMeans: <https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html>

### KV Cache

- **Definição:** cache de keys e values usados em decoding autoregressivo de Transformers.
- **Conceito:** evita recalcular atenção para tokens anteriores durante geração.
- **Aplicação:** serving eficiente de LLMs.
- **Pitfalls:** consumo de memória cresce com batch, camadas e contexto.
- **Referência:** vLLM PagedAttention: <https://docs.vllm.ai/>

---

## L

### LoRA

- **Definição:** Low-Rank Adaptation, técnica PEFT que injeta matrizes de baixo posto em camadas do modelo.
- **Conceito:** congela pesos principais e treina adaptações de baixa dimensão.
- **Aplicação:** fine-tuning barato de LLMs e modelos de visão.
- **Pitfalls:** escolha de rank, módulos-alvo e dataset afeta muito o resultado.
- **Referência:** LoRA paper: <https://arxiv.org/abs/2106.09685>

### LSTM

- **Definição:** Long Short-Term Memory, RNN com gates para controlar memória temporal.
- **Conceito:** input, forget e output gates regulam cell state.
- **Aplicação:** séries, texto e sequências antes da dominância de Transformers.
- **Pitfalls:** treino lento, paralelização limitada, dificuldade com contexto longo.
- **Referência:** LSTM paper: <https://www.bioinf.jku.at/publications/older/2604.pdf>

---

## M

### MLOps

- **Definição:** práticas para desenvolver, versionar, implantar e monitorar sistemas de ML.
- **Conceito:** ciclo de vida de dados, código, modelo, avaliação, deploy e observabilidade.
- **Aplicação:** produção de modelos confiáveis.
- **Pitfalls:** tratar modelo como artefato isolado; ignorar dados e feedback loops.
- **Referência:** Google MLOps: <https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning>

### MoE

- **Definição:** Mixture of Experts, arquitetura que roteia entradas para subconjuntos de especialistas.
- **Conceito:** ativa parte dos parâmetros por token, aumentando capacidade sem custo proporcional total.
- **Aplicação:** LLMs escaláveis.
- **Pitfalls:** roteamento instável, balanceamento de carga, comunicação distribuída.
- **Referência:** Switch Transformers: <https://arxiv.org/abs/2101.03961>

---

## P

### PEFT

- **Definição:** Parameter-Efficient Fine-Tuning, família de técnicas que ajusta poucos parâmetros.
- **Conceito:** adapters, LoRA, prefix/prompt tuning.
- **Aplicação:** adaptação econômica de modelos grandes.
- **Pitfalls:** limita capacidade de adaptação; comparação injusta com full fine-tuning.
- **Referência:** Hugging Face PEFT: <https://huggingface.co/docs/peft/>

### Positional Encoding

- **Definição:** informação adicionada aos tokens para codificar posição na sequência.
- **Conceito:** embeddings posicionais fixos ou aprendidos.
- **Aplicação:** Transformers sem recorrência.
- **Pitfalls:** extrapolação de contexto e incompatibilidade entre esquemas.
- **Referência:** Attention Is All You Need: <https://arxiv.org/abs/1706.03762>

### Prompt Engineering

- **Definição:** desenho sistemático de instruções, contexto e formatos para modelos generativos.
- **Conceito:** controla tarefa, restrições, exemplos, tom, formato e critérios.
- **Aplicação:** sumarização, extração, código, classificação, agentes.
- **Pitfalls:** prompts frágeis, overfitting ao conjunto de avaliação, prompt injection.
- **Referência:** OpenAI prompt engineering: <https://platform.openai.com/docs/guides/prompt-engineering>

---

## Q

### Quantization

- **Definição:** redução de precisão numérica de pesos/ativações para diminuir memória e acelerar inferência.
- **Conceito:** FP32 para FP16/BF16/INT8/INT4, com ou sem calibração.
- **Aplicação:** serving de modelos grandes em hardware limitado.
- **Pitfalls:** perda de qualidade, incompatibilidade de kernel, avaliação incompleta.
- **Referência:** PyTorch quantization: <https://pytorch.org/docs/stable/quantization.html>

---

## R

### RAG

- **Definição:** Retrieval-Augmented Generation, técnica que combina recuperação de contexto com geração.
- **Conceito:** pergunta -> retrieval -> contexto -> geração -> resposta grounded.
- **Aplicação:** QA sobre documentos, assistentes internos, suporte técnico.
- **Pitfalls:** chunking ruim, embeddings inadequados, contexto irrelevante, falsa citação.
- **Referência:** RAG paper: <https://arxiv.org/abs/2005.11401>

### Random Forest

- **Definição:** ensemble de árvores treinadas com bagging e seleção aleatória de features.
- **Conceito:** reduz variância agregando árvores descorrelacionadas.
- **Aplicação:** baseline forte para dados tabulares.
- **Pitfalls:** extrapola mal em regressão, modelos grandes e explicabilidade limitada.
- **Referência:** scikit-learn RandomForest: <https://scikit-learn.org/stable/modules/ensemble.html#forests-of-randomized-trees>

### RLHF

- **Definição:** Reinforcement Learning from Human Feedback, alinhamento por preferências humanas.
- **Conceito:** treina reward model e otimiza política para maximizar recompensa.
- **Aplicação:** ajuste de LLMs conversacionais.
- **Pitfalls:** reward hacking, viés de anotadores, custo e instabilidade.
- **Referência:** InstructGPT: <https://arxiv.org/abs/2203.02155>

---

## S

### Self-Attention

- **Definição:** attention em que queries, keys e values vêm da mesma sequência.
- **Conceito:** cada token agrega informação contextual dos demais tokens.
- **Aplicação:** encoder e decoder Transformers.
- **Pitfalls:** custo quadrático e sensibilidade a contexto irrelevante.
- **Referência:** Attention Is All You Need: <https://arxiv.org/abs/1706.03762>

### SHAP

- **Definição:** método de explicabilidade baseado em valores de Shapley.
- **Conceito:** atribui contribuição média marginal de cada feature à predição.
- **Aplicação:** explicações locais e globais.
- **Pitfalls:** custo computacional, correlação entre features e interpretação causal indevida.
- **Referência:** SHAP paper: <https://arxiv.org/abs/1705.07874>

### Speculative Decoding

- **Definição:** técnica de inferência que usa modelo menor para propor tokens e modelo maior para verificar.
- **Conceito:** acelera geração mantendo distribuição do modelo alvo sob aceitação correta.
- **Aplicação:** serving de LLMs com menor latência.
- **Pitfalls:** ganho depende da taxa de aceitação e overhead de verificação.
- **Referência:** Speculative Decoding: <https://arxiv.org/abs/2211.17192>

### Stable Diffusion

- **Definição:** modelo generativo de imagem baseado em difusão latente.
- **Conceito:** denoising iterativo em espaço latente condicionado por texto.
- **Aplicação:** geração e edição de imagens.
- **Pitfalls:** vieses, direitos autorais, prompt sensitivity, custo de inferência.
- **Referência:** Latent Diffusion Models: <https://arxiv.org/abs/2112.10752>

---

## T

### Tensor Parallelism

- **Definição:** divisão de tensores/operações de um modelo entre múltiplos dispositivos.
- **Conceito:** particiona matrizes e reduz resultados via comunicação coletiva.
- **Aplicação:** treino e serving de modelos grandes.
- **Pitfalls:** overhead de comunicação, balanceamento e complexidade operacional.
- **Referência:** Megatron-LM: <https://arxiv.org/abs/1909.08053>

### Tokenization

- **Definição:** conversão de texto em unidades discretas processadas por modelo.
- **Conceito:** BPE, WordPiece, unigram e vocabulários subword.
- **Aplicação:** NLP e LLMs.
- **Pitfalls:** custo por token, fragmentação de palavras, idiomas sub-representados.
- **Referência:** Hugging Face tokenizers: <https://huggingface.co/docs/tokenizers/>

### Transformer

- **Definição:** arquitetura neural baseada em attention, feed-forward networks, residual connections e normalização.
- **Conceito:** processa sequências por self-attention paralelizável.
- **Aplicação:** LLMs, tradução, visão, multimodal.
- **Pitfalls:** custo quadrático, necessidade de escala, opacidade e dependência de dados.
- **Referência:** Attention Is All You Need: <https://arxiv.org/abs/1706.03762>

---

## V

### Vector Database

- **Definição:** sistema otimizado para armazenar e buscar vetores por similaridade.
- **Conceito:** ANN indexes como HNSW/IVF aproximam nearest neighbors.
- **Aplicação:** RAG, recomendação e busca semântica.
- **Pitfalls:** métricas incorretas, atualização de embeddings, recall baixo e avaliação fraca.
- **Referência:** FAISS: <https://faiss.ai/>

### vLLM

- **Definição:** engine de serving de LLMs otimizada para throughput e memória.
- **Conceito:** PagedAttention gerencia KV cache de forma eficiente.
- **Aplicação:** inferência de LLMs open source em produção.
- **Pitfalls:** compatibilidade de modelos, memória de GPU, tradeoff throughput/latência.
- **Referência:** vLLM docs: <https://docs.vllm.ai/>
