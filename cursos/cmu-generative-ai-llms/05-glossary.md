# 05 — Glossário Técnico Avançado

## Attention

- **Definição:** mecanismo que pondera interações entre tokens por queries, keys e values.
- **Fórmula:** `softmax(QK^T / sqrt(d_k))V`.
- **Aplicação:** base dos Transformers.
- **Pitfalls:** custo quadrático, interpretação frágil de pesos, sensibilidade a contexto irrelevante.
- **Referência:** <https://arxiv.org/abs/1706.03762>

## Autoregressive Language Model

- **Definição:** modelo que fatoriza probabilidade de sequência como produto de próximos tokens.
- **Fórmula:** `P(x_1...x_n)=prod_t P(x_t | x_<t)`.
- **Aplicação:** GPT-like decoder-only LMs.
- **Pitfalls:** exposição a viés de dados, alucinação, decoding sensível.
- **Referência:** <https://arxiv.org/abs/2005.14165>

## BPE

- **Definição:** Byte Pair Encoding, tokenização por merges frequentes de subwords/bytes.
- **Conceito:** equilibra vocabulário e comprimento de sequência.
- **Aplicação:** tokenizers modernos.
- **Pitfalls:** fragmentação desigual por idioma/domínio.
- **Referência:** <https://huggingface.co/docs/tokenizers/>

## Benchmark Leakage

- **Definição:** contaminação de dados de avaliação no treino/pretraining.
- **Conceito:** avaliação perde validade quando o modelo viu exemplos ou equivalentes.
- **Aplicação:** auditoria de evals de LLM.
- **Pitfalls:** resultados inflados e decisões falsas de capacidade.
- **Referência:** <https://arxiv.org/abs/2211.09110>

## Chain-of-Thought

- **Definição:** prompting ou treino que induz passos intermediários de raciocínio.
- **Conceito:** exemplos demonstram decomposição de problemas.
- **Aplicação:** matemática, planejamento, raciocínio multi-etapa.
- **Pitfalls:** justificativas plausíveis mas incorretas; risco de expor raciocínio sensível.
- **Referência:** <https://arxiv.org/abs/2201.11903>

## Chinchilla Scaling

- **Definição:** resultado empírico sobre compute-optimal training que favorece mais dados para dado budget de compute.
- **Conceito:** tamanho de modelo e tokens devem escalar de forma balanceada.
- **Aplicação:** planejamento de pretraining.
- **Pitfalls:** extrapolação ingênua para regimes/dados diferentes.
- **Referência:** <https://arxiv.org/abs/2203.15556>

## Data Deduplication

- **Definição:** remoção de duplicatas exatas ou aproximadas em corpus.
- **Conceito:** reduz memorization e contaminação.
- **Aplicação:** preparação de dados de pré-treinamento.
- **Pitfalls:** remover diversidade legítima ou manter duplicatas semânticas.
- **Referência:** <https://arxiv.org/abs/2104.08758>

## DPO

- **Definição:** Direct Preference Optimization, método de alinhamento por pares de preferência.
- **Conceito:** otimiza diretamente a preferência por respostas escolhidas sobre rejeitadas.
- **Aplicação:** alternativa mais simples a RLHF/PPO em certos setups.
- **Pitfalls:** sensível à qualidade dos dados de preferência.
- **Referência:** <https://arxiv.org/abs/2305.18290>

## Embedding

- **Definição:** representação vetorial densa de texto, token, imagem ou entidade.
- **Conceito:** proximidade vetorial aproxima similaridade semântica.
- **Aplicação:** retrieval, RAG, clustering, multimodal alignment.
- **Pitfalls:** viés, anisotropia, drift, métrica inadequada.
- **Referência:** <https://platform.openai.com/docs/guides/embeddings>

## FlashAttention

- **Definição:** algoritmo/kernels para attention eficiente em memória.
- **Conceito:** reduz leituras/escritas de HBM com tiling e recomputação controlada.
- **Aplicação:** treino e inferência de Transformers.
- **Pitfalls:** compatibilidade de hardware/kernel e limites de integração.
- **Referência:** <https://arxiv.org/abs/2205.14135>

## Grouped-Query Attention

- **Definição:** variante que compartilha keys/values entre grupos de query heads.
- **Conceito:** reduz memória e custo de KV cache comparado a MHA.
- **Aplicação:** LLM serving eficiente.
- **Pitfalls:** tradeoff entre qualidade e eficiência.
- **Referência:** <https://arxiv.org/abs/2305.13245>

## HELM

- **Definição:** Holistic Evaluation of Language Models.
- **Conceito:** benchmark multi-métrica e multi-cenário para LMs.
- **Aplicação:** avaliação abrangente de LLMs.
- **Pitfalls:** cobertura ainda limitada frente a usos reais.
- **Referência:** <https://arxiv.org/abs/2211.09110>

## In-Context Learning

- **Definição:** capacidade de adaptar comportamento a exemplos/instruções no prompt sem atualizar pesos.
- **Conceito:** aprendizado aparente via contexto.
- **Aplicação:** few-shot prompting.
- **Pitfalls:** instabilidade, sensibilidade à ordem, custo de tokens.
- **Referência:** <https://arxiv.org/abs/2005.14165>

## KV Cache

- **Definição:** cache de keys e values para evitar recomputação em decoding autoregressivo.
- **Conceito:** memória cresce com camadas, batch, contexto e dimensão.
- **Aplicação:** serving de LLMs.
- **Pitfalls:** gargalo de memória em long context.
- **Referência:** <https://arxiv.org/abs/2309.06180>

## LoRA

- **Definição:** Low-Rank Adaptation, PEFT que treina matrizes de baixo posto.
- **Conceito:** congela pesos principais e aprende adaptações.
- **Aplicação:** fine-tuning eficiente.
- **Pitfalls:** escolha de rank e módulos-alvo afeta resultado.
- **Referência:** <https://arxiv.org/abs/2106.09685>

## MoE

- **Definição:** Mixture of Experts, arquitetura que roteia tokens para especialistas.
- **Conceito:** ativa fração dos parâmetros por token.
- **Aplicação:** escalar capacidade com custo computacional parcial.
- **Pitfalls:** roteamento, balanceamento de carga e comunicação distribuída.
- **Referência:** <https://arxiv.org/abs/2101.03961>

## PagedAttention

- **Definição:** mecanismo de gerenciamento de KV cache inspirado em paginação de memória.
- **Conceito:** melhora utilização de memória para serving.
- **Aplicação:** vLLM.
- **Pitfalls:** ganhos dependem do padrão de tráfego e sequência.
- **Referência:** <https://arxiv.org/abs/2309.06180>

## PEFT

- **Definição:** Parameter-Efficient Fine-Tuning.
- **Conceito:** adapta poucos parâmetros em vez do modelo inteiro.
- **Aplicação:** LoRA, adapters, prompt tuning.
- **Pitfalls:** pode limitar adaptação profunda.
- **Referência:** <https://huggingface.co/docs/peft/>

## Perplexity

- **Definição:** exponencial da cross-entropy média por token.
- **Fórmula:** `PPL = exp(-1/N * sum log p(x_t | x_<t))`.
- **Aplicação:** avaliação de language models.
- **Pitfalls:** não mede utilidade, factualidade ou alinhamento.
- **Referência:** <https://web.stanford.edu/~jurafsky/slp3/>

## Quantization

- **Definição:** redução de precisão numérica de pesos/ativações.
- **Conceito:** FP32/FP16/BF16 para INT8/INT4 etc.
- **Aplicação:** reduzir memória e acelerar inferência.
- **Pitfalls:** degradação de qualidade, kernels incompatíveis.
- **Referência:** <https://pytorch.org/docs/stable/quantization.html>

## RAG

- **Definição:** Retrieval-Augmented Generation.
- **Conceito:** recuperar contexto externo e condicionar geração.
- **Aplicação:** QA documental, assistentes corporativos, grounding.
- **Pitfalls:** retrieval ruim, contexto irrelevante, falsas citações.
- **Referência:** <https://arxiv.org/abs/2005.11401>

## RLHF

- **Definição:** Reinforcement Learning from Human Feedback.
- **Conceito:** treina reward model por preferência e otimiza política.
- **Aplicação:** instruction following e alinhamento.
- **Pitfalls:** reward hacking, viés de anotação, instabilidade.
- **Referência:** <https://arxiv.org/abs/2203.02155>

## RoPE

- **Definição:** Rotary Position Embeddings.
- **Conceito:** codifica posição por rotação em pares de dimensões.
- **Aplicação:** Transformers modernos e extensão de contexto.
- **Pitfalls:** extrapolação de contexto precisa cuidado.
- **Referência:** <https://arxiv.org/abs/2104.09864>

## Speculative Decoding

- **Definição:** método que usa modelo menor para propor tokens e modelo maior para verificar.
- **Conceito:** acelera decoding mantendo distribuição-alvo sob aceitação correta.
- **Aplicação:** reduzir latência de LLMs.
- **Pitfalls:** ganhos dependem da taxa de aceitação.
- **Referência:** <https://arxiv.org/abs/2211.17192>

## Tool Use

- **Definição:** LLM chama ferramentas externas para cálculo, busca, execução ou ação.
- **Conceito:** separa linguagem de capacidades determinísticas.
- **Aplicação:** agentes, RAG, workflows.
- **Pitfalls:** segurança, permissões, validação de outputs e loops.
- **Referência:** <https://arxiv.org/abs/2302.04761>

## Transformer

- **Definição:** arquitetura neural baseada em attention, MLPs, residual connections e normalization.
- **Conceito:** processa sequências por self-attention paralelizável.
- **Aplicação:** LLMs, VLMs, tradução, retrieval e multimodalidade.
- **Pitfalls:** custo de contexto, escala de dados, opacidade.
- **Referência:** <https://arxiv.org/abs/1706.03762>

## vLLM

- **Definição:** engine de serving para LLMs com PagedAttention.
- **Conceito:** melhora throughput e uso de KV cache.
- **Aplicação:** inferência open-source em escala.
- **Pitfalls:** tuning de batching, memória e compatibilidade.
- **Referência:** <https://docs.vllm.ai/>
