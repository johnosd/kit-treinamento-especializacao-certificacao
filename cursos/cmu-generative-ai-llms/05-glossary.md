# Glossário Técnico — CMU Generative AI & LLMs Kit

> 37 termos essenciais do stack completo: algoritmos → sistemas → multimodalidade.
> Cada termo: definição + conceito formal/fórmula + aplicação + pitfalls + referência autoritativa.

---

## 01 — Transformer

**Definição:** Arquitetura de rede neural baseada inteiramente em mecanismos de atenção, sem recorrência ou convoluções, que processa sequências em paralelo.

**Conceito formal:** Um bloco Transformer consiste em Multi-Head Self-Attention seguido de Feed-Forward Network (FFN), com residual connections e Layer Normalization:
```
h = LayerNorm(x + MHA(x))
y = LayerNorm(h + FFN(h))
```

**Aplicação:** Backbone de praticamente todos os LLMs modernos (GPT, BERT, LLaMA). Encoder-only (BERT), decoder-only (GPT), encoder-decoder (T5).

**Pitfalls:** Complexidade quadrática em sequência (`O(n²d)`); sem inductive bias de localidade → precisa de positional encoding explícito.

**Referência:** Vaswani et al. 2017. "Attention is All You Need." NeurIPS.

---

## 02 — Scaled Dot-Product Attention

**Definição:** Mecanismo de atenção que computa uma soma ponderada dos valores V, onde os pesos são derivados da compatibilidade entre queries Q e keys K.

**Conceito formal:**
```
Attention(Q, K, V) = softmax(QK^T / √d_k) · V
```
O fator `√d_k` evita que os dot products cresçam com a dimensionalidade, saturando o softmax.

**Aplicação:** Base de todos os mecanismos de atenção modernos. Causal masking (máscara triangular inferior) converte atenção em autorregressive.

**Pitfalls:** Sem causal masking, o modelo "vê o futuro" (leakage). Com d_k grande e sem scaling, gradients quase zero no softmax.

**Referência:** Vaswani et al. 2017. Seção 3.2.1.

---

## 03 — Multi-Head Attention (MHA)

**Definição:** Extensão da atenção que aplica h atenções independentes em paralelo sobre projeções lineares distintas de Q, K, V, concatenando os resultados.

**Conceito formal:**
```
MHA(Q, K, V) = Concat(head_1, ..., head_h) W_O
head_i = Attention(QW_i^Q, KW_i^K, VW_i^V)
```
Cada `W_i` tem dimensão `d_model/h`, mantendo custo total igual à atenção simples.

**Aplicação:** Permite ao modelo atender a informação de diferentes posições e representações ao mesmo tempo. Em LLMs modernos: 32–128 heads.

**Pitfalls:** KV cache cresce com n_heads × n_layers × seq_len → MQA/GQA para mitigar.

**Referência:** Vaswani et al. 2017; Shazeer 2019 (MQA).

---

## 04 — Grouped Query Attention (GQA)

**Definição:** Variante de MHA onde múltiplas query heads compartilham um único par (K, V), reduzindo o tamanho do KV cache sem degradação significativa.

**Conceito formal:** Com G grupos, cada grupo de `h/G` query heads compartilha 1 K head e 1 V head:
```
KV cache size = 2 × n_layers × G × d_kv × seq_len × dtype_bytes
```
MQA = GQA com G=1; MHA = GQA com G=n_heads.

**Aplicação:** Padrão em LLaMA-2 70B, Mistral, Gemma. Reduz KV cache em `n_heads/G` × sem custo significativo em qualidade.

**Pitfalls:** G muito pequeno (MQA) pode degradar quality em tasks de reasoning. Trade-off empírico: G ∈ {4, 8} é robusto.

**Referência:** Ainslie et al. 2023. "GQA: Training Generalized Multi-Query Transformer Models." EMNLP.

---

## 05 — Rotary Positional Embedding (RoPE)

**Definição:** Codificação posicional relativa que incorpora informação de posição diretamente na operação Q·K via rotação no espaço complexo.

**Conceito formal:** Para posição m, o embedding é rotacionado:
```
f(q, m) = q · e^(imθ)
```
A atenção entre posições m e n depende apenas de (m-n), tornando a relação naturalmente relativa. θ_d = 10000^(-2d/D).

**Aplicação:** LLaMA, Mistral, Falcon, Phi. Permite extrapolação de comprimento de contexto (YaRN, LongRoPE).

**Pitfalls:** Degradação ao extrapolar além do comprimento de treino sem ajuste de θ (RoPE scaling). `base` de 10000 padrão é inadequado para context > 8K sem ajuste.

**Referência:** Su et al. 2021. "RoFormer: Enhanced Transformer with Rotary Position Embedding." arXiv.

---

## 06 — Byte-Pair Encoding (BPE)

**Definição:** Algoritmo de tokenização baseado em compressão iterativa: inicializa com caracteres e progressivamente mescla os pares de tokens mais frequentes.

**Conceito formal:**
1. Inicializar vocabulário com caracteres únicos.
2. Contar frequência de todos os pares adjacentes.
3. Mesclar o par mais frequente como novo token.
4. Repetir até vocab_size desejado.

**Aplicação:** GPT-2/3/4 (tiktoken), LLaMA (SentencePiece BPE). Vocabulários típicos: 32K–128K tokens.

**Pitfalls:** Sem limite de frequência mínima → tokens raros no vocabulário desperdiçam capacidade. Performance sensível a espaços (espaço antes de palavra é tratado diferente).

**Referência:** Sennrich et al. 2016. "Neural Machine Translation of Rare Words with Subword Units." ACL.

---

## 07 — Pre-training (CLM / MLM)

**Definição:** Treinamento de self-supervised em corpus de texto massivo antes de qualquer fine-tuning supervisionado.

**Conceito formal:**
- **Causal LM (CLM):** `L = -Σ log P(x_t | x_{<t})` — prediz próximo token. Decoder-only.
- **Masked LM (MLM):** `L = -Σ_{t∈M} log P(x_t | x_{ctx})` — prediz tokens mascarados. Encoder-only (BERT: 15% masking).

**Aplicação:** CLM para modelos generativos (GPT, LLaMA). MLM para modelos de representação (BERT, RoBERTa). T5 usa span corruption (variante de MLM).

**Pitfalls:** CLM não vê contexto bidirecional → representações menos ricas para classification. MLM não funciona nativamente para geração.

**Referência:** Brown et al. 2020 (GPT-3); Devlin et al. 2019 (BERT).

---

## 08 — Fine-tuning / Instruction Tuning

**Definição:** Ajuste de pesos do modelo pré-treinado em dados supervisionados para uma tarefa específica (fine-tuning) ou para seguir instruções em linguagem natural (instruction tuning).

**Conceito formal:** Minimiza cross-entropy em pares (instrução, resposta):
```
L_SFT = -Σ log P_θ(y_t | x, y_{<t})
```
Instruction tuning é supervised fine-tuning (SFT) em formato instruction-response.

**Aplicação:** InstructGPT (Ouyang 2022), Alpaca, Llama-2-Chat. Base para RLHF.

**Pitfalls:** Catastrophic forgetting em domínios fora do fine-tuning set. Overfitting com poucos dados. "Superficial alignment" — modelo aprende formato mas não capacidade.

**Referência:** Ouyang et al. 2022. "Training language models to follow instructions with human feedback." NeurIPS.

---

## 09 — LoRA / PEFT

**Definição:** Parameter-Efficient Fine-Tuning: técnicas que ajustam apenas um subconjunto dos parâmetros, mantendo os pesos base congelados.

**Conceito formal (LoRA):** Aproxima a atualização de peso por produto de duas matrizes de baixo rank:
```
W' = W + ΔW = W + BA
B ∈ R^{d×r}, A ∈ R^{r×k}, r ≪ min(d,k)
```
Trainable params: `2×r×(d+k)` vs `d×k` full. Init: A ~ N(0,σ²), B = 0.

**Aplicação:** Fine-tuning de LLMs grandes em consumer GPU. QLoRA combina LoRA com NF4 quantization.

**Pitfalls:** Rank muito baixo → underfitting em tasks complexas. LoRA aplicado só em Q,V (padrão) pode ser subótimo — aplicar em todos os projection layers frequentemente melhora.

**Referência:** Hu et al. 2022. "LoRA: Low-Rank Adaptation of Large Language Models." ICLR.

---

## 10 — In-Context Learning (ICL)

**Definição:** Capacidade emergente de LLMs de aprender tasks a partir de exemplos no prompt, sem atualização de parâmetros.

**Conceito formal:** Para task T com k exemplos:
```
P(y | x, (x_1,y_1), ..., (x_k,y_k))
```
O modelo infere o padrão a partir da distribuição de exemplos, não de gradientes.

**Aplicação:** Zero-shot, one-shot, few-shot prompting. Foundation de ChatGPT-style interaction.

**Pitfalls:** Sensível à ordem dos exemplos, ao formato, e ao label space (Min 2022: labels aleatórios muitas vezes não degradam, sugerindo ICL não é "aprender a task"). Performance não-monotônica com k.

**Referência:** Brown et al. 2020 (GPT-3); Min et al. 2022 (Rethinking ICL). EMNLP.

---

## 11 — Chain-of-Thought (CoT)

**Definição:** Técnica de prompting que elicita raciocínio passo a passo antes da resposta final, melhorando accuracy em tasks de múltiplas etapas.

**Conceito formal:** Zero-shot CoT: adiciona "Let's think step by step." ao prompt. Few-shot CoT: exemplos com raciocínio explícito.

**Aplicação:** Melhora aritmética, reasoning lógico, coding. Fundamental para models ≥ 100B (emergent com escala).

**Pitfalls:** Verbose → maior latência e custo. "Unfaithful CoT" — o raciocínio pode ser post-hoc e não causal (Turpin 2023). Pode introduzir erros de raciocínio em cadeia.

**Referência:** Wei et al. 2022. "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models." NeurIPS.

---

## 12 — Retrieval-Augmented Generation (RAG)

**Definição:** Arquitetura que aumenta a geração de LLMs com documentos recuperados de uma base de conhecimento externa, reduzindo hallucination e permitindo atualização de conhecimento.

**Conceito formal:**
```
P(y | q) = Σ_d P(y | q, d) · P(d | q)
```
Na prática: top-K retrieval → concatenação com query → geração.

**Aplicação:** Open-domain QA, chatbots com knowledge bases corporativas. TriviaQA, NQ, HotpotQA.

**Pitfalls:** "Lost in the middle" — atenção do LLM degrada para documentos no meio do contexto (Liu 2023). Retrieval quality é gargalo: garbage in, garbage out. Latência adicional de retrieval.

**Referência:** Lewis et al. 2020. "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks." NeurIPS.

---

## 13 — Scaling Laws

**Definição:** Relações empíricas de power-law entre performance do modelo (perplexidade) e escala (parâmetros N, dados D, compute C).

**Conceito formal (Chinchilla):**
```
L(N, D) ≈ E + A/N^α + B/D^β
```
Compute-optimal: N ∝ C^0.5, D ∝ C^0.5 (tokens ≈ 20× parâmetros para Chinchilla-optimal).

**Aplicação:** Planejamento de treinamento (quanto compute investir em parâmetros vs dados). LLaMA 1 foi treinado com muito mais dados que Chinchilla-optimal.

**Pitfalls:** Leis calibradas em regime específico podem não extrapolar. Performance em perplexidade ≠ performance em downstream tasks (breaks in scaling). "Emerging abilities" não são previstos por leis de escala simples.

**Referência:** Hoffmann et al. 2022 (Chinchilla). "Training Compute-Optimal Large Language Models." NeurIPS.

---

## 14 — RLHF — Reinforcement Learning from Human Feedback

**Definição:** Pipeline de alinhamento em 3 etapas: SFT → treinar reward model → otimizar política com RL (PPO) para maximizar reward.

**Conceito formal:**
```
R_θ(x, y) = reward model score
L_PPO = E[R_θ(x, y)] - β · KL(π_θ || π_ref)
```
O termo KL penaliza divergência da política de referência (SFT), evitando reward hacking.

**Aplicação:** InstructGPT, ChatGPT, Claude, Llama-2-Chat. Base para alinhamento de LLMs.

**Pitfalls:** Reward hacking: política aprende a maximizar reward model sem melhorar qualidade real. Custo computacional alto (actor + critic + reference + reward model em memória). Instabilidade de PPO.

**Referência:** Ouyang et al. 2022 (InstructGPT); Stiennon et al. 2020 (Learning to Summarize).

---

## 15 — DPO — Direct Preference Optimization

**Definição:** Alternativa ao RLHF que otimiza preferências diretamente como fine-tuning supervisionado, sem treinar reward model explícito ou usar RL.

**Conceito formal:** Derivado como reparametrização do objetivo RLHF:
```
L_DPO = -E[(log σ(β log(π_θ(y_w|x)/π_ref(y_w|x)) - β log(π_θ(y_l|x)/π_ref(y_l|x))))]
```
y_w = resposta preferida, y_l = resposta rejeitada.

**Aplicação:** Fine-tuning de LLMs com datasets de preferência (UltraFeedback, Anthropic HH). Mais estável que PPO.

**Pitfalls:** Requer modelo de referência (π_ref) congelado em memória. Performance pode degradar se distribuição de respostas coletadas diverge muito do π_ref. Pode "esquecimento" de capabilities não cobertas pelos pares de preferência.

**Referência:** Rafailov et al. 2023. "Direct Preference Optimization." NeurIPS.

---

## 16 — KV Cache

**Definição:** Otimização de inferência autoregressiva que armazena os Key e Value computados para tokens anteriores, evitando recomputação em cada passo.

**Conceito formal:**
```
KV_cache_size = 2 × n_layers × n_heads × d_head × seq_len × bytes_per_element
```
Para LLaMA-2-7B (FP16): ≈ 2 × 32 × 32 × 128 × seq_len × 2 bytes = 0.5 MB/token.

**Aplicação:** Presente em toda inferência de decoder-only LLM. Gargalo de memória para batch grande ou contexto longo.

**Pitfalls:** Cresce linearmente com seq_len → limite de throughput. GQA/MQA reduzem o cache mas não eliminam o crescimento. PagedAttention resolve fragmentação.

**Referência:** Implementação canonical em HuggingFace `past_key_values`; Kwon et al. 2023 (análise de fragmentação).

---

## 17 — FlashAttention

**Definição:** Algoritmo de atenção IO-aware que reorganiza o cálculo em tiles para minimizar leituras/escritas em HBM (High Bandwidth Memory), atingindo velocidade 2–4× vs atenção padrão.

**Conceito formal:** Usa online softmax (Milakov & Gimelshein 2018) para computar atenção por blocos sem materializar a matriz N×N em HBM:
```
HBM reads: O(N · d)  vs  O(N²) padrão
```
FA2 melhora paralelismo (split seq entre thread blocks) e reduz shared memory.

**Aplicação:** Padrão em todos os frameworks modernos (PyTorch ≥2.0, HF Transformers). Necessário para seq_len > 2K.

**Pitfalls:** Requer SRAM suficiente (depende de `d_head`). Implementação em hardware diferente (TPU, AMD ROCm) mais difícil. Backward pass complexo (recomputa blocos em vez de armazenar).

**Referência:** Dao et al. 2022 (FA1), Dao 2023 (FA2). "FlashAttention-2: Faster Attention with Better Parallelism." ICLR 2024.

---

## 18 — PagedAttention / vLLM

**Definição:** Gerenciamento de memória para KV cache inspirado em virtual memory de SO: divide o cache em blocos de tamanho fixo, alocados sob demanda, eliminando fragmentação.

**Conceito formal:**
- KV cache dividido em blocos de B tokens.
- Tabela de blocos (block table) mapeia posição lógica → bloco físico.
- Fragmentação interna ≤ 1 bloco por sequência.
```
waste ≤ (B - 1) × bytes_per_token  vs  O(max_seq_len) na alocação pré-alocada
```

**Aplicação:** vLLM serve como base de praticamente todos os sistemas de serving LLM de produção. PagedAttention + continuous batching = 2–4× throughput vs HF TGI naive.

**Pitfalls:** Block table overhead pequeno mas não-zero. Preemption (eject blocks quando memória esgota) adiciona latência para requests de baixa prioridade.

**Referência:** Kwon et al. 2023. "Efficient Memory Management for Large Language Model Serving with PagedAttention." SOSP.

---

## 19 — Speculative Decoding

**Definição:** Técnica de inferência que usa um modelo draft pequeno para propor K tokens e um modelo target grande para verificar em paralelo, alcançando speedup sem alterar a distribuição de saída.

**Conceito formal:**
1. Draft model gera K tokens x̃_1,...,x̃_K.
2. Target model avalia todos em 1 forward pass.
3. Aceita token x̃_i se `q(x̃_i|x_{<i}) / p(x̃_i|x_{<i}) ≥ U[0,1]`.
4. Gera token de recuperação do target onde rejeitou.

**Aplicação:** vLLM speculative decoding, TensorRT-LLM. Speedup típico: 2–3× em tasks com alta aceitação (completions, summarization).

**Pitfalls:** Benefício cai em tasks de baixa previsibilidade (criação, diverse sampling). Requer ter dois modelos em memória (draft + target). Draft quality determina o speedup.

**Referência:** Leviathan et al. 2023. "Fast Inference from Transformers via Speculative Decoding." ICML.

---

## 20 — Tensor Parallelism

**Definição:** Estratégia de paralelismo que particiona os pesos de cada camada entre GPUs, com cada GPU computando uma fração da operação matricial.

**Conceito formal (Megatron):** Para linear Y = XW com W ∈ R^{H×H}:
- **Column split:** W = [W_1 | W_2], cada GPU computa Y_i = XW_i. All-gather no final.
- **Row split:** W = [W_1; W_2], X também particionado. All-reduce no final.
```
All-reduce volume: 2 × batch × seq_len × H × bytes  (por camada)
```

**Aplicação:** Megatron-LM, DeepSpeed, NeMo. Padrão para treinar modelos ≥ 20B.

**Pitfalls:** All-reduce é all-to-all → latência de comunicação limita TP degree. Eficiente apenas em InfiniBand ou NVLink (slow ethernet = gargalo). Cada GPU precisa de H/TP dimensional representation completo.

**Referência:** Shoeybi et al. 2019. "Megatron-LM: Training Multi-Billion Parameter Language Models." arXiv.

---

## 21 — Pipeline Parallelism

**Definição:** Particiona layers do modelo entre GPUs (stages), com micro-batches fluindo pelo pipeline de forma encadeada.

**Conceito formal (GPipe bubble):**
```
bubble_fraction = (p-1) / (m + p - 1)
```
p = stages, m = micro-batches. 1F1B schedule melhora para:
```
idle_time = (p-1) × t_microbatch  (constante, não escala com m)
```

**Aplicação:** Treino de modelos muito grandes onde tensor parallelism sozinho não basta. Megatron usa PP + TP + DP combinados (3D parallelism).

**Pitfalls:** Load imbalance entre stages (stages do embedding vs transformer). Bubble overhead vs pipeline depth. Recomputation de activations entre stages.

**Referência:** Huang et al. 2019 (GPipe); Narayanan et al. 2021 (PipeDream-Flush/1F1B). NeurIPS/SOSP.

---

## 22 — ZeRO / DeepSpeed

**Definição:** Zero Redundancy Optimizer: distribui estados do optimizer, gradientes e parâmetros entre GPUs em vez de replicar em todas, reduzindo memória por GPU.

**Conceito formal:**
| Stage | O que é shardado | Memória por GPU |
|---|---|---|
| Z1 | Optimizer states | 1/N × optimizer |
| Z2 | + Gradients | 1/N × (optimizer + grads) |
| Z3 | + Parameters | 1/N × tudo |

Para modelo de parâmetros M (FP32 optimizer): Z3 reduz de `16M bytes` para `16M/N bytes` por GPU.

**Aplicação:** DeepSpeed ZeRO, PyTorch FSDP (≈ZeRO-3). Padrão em treino de modelos > 7B em hardware múltiplo.

**Pitfalls:** Z3 adiciona all-gather de parâmetros em cada forward → latência. Frequência de comunicação 3× maior que Z1. Incompatível com `torch.nn.DataParallel` legado.

**Referência:** Rajbhandari et al. 2020. "ZeRO: Memory Optimizations Toward Training Trillion Parameter Models." SC.

---

## 23 — Quantização (INT8 / INT4)

**Definição:** Redução de precisão de pesos e/ou ativações de FP32/FP16 para inteiros de menor bit-width, reduzindo memória e acelerando computação.

**Conceito formal (absmax INT8):**
```
x_q = round(x / s)    onde s = max(|x|) / 127
x_dequant = x_q × s
```
GPTQ: quantização layer-by-layer usando Hessian de segunda ordem para minimizar erro de reconstrução.

**Aplicação:** LLM.int8() (Dettmers 2022): quantiza ativações exceto outliers. GPTQ/AWQ para INT4. QLoRA: NF4 para weights congelados + LoRA FP16.

**Pitfalls:** Outliers em ativações de LLMs quebram quantização uniforme → LLM.int8() trata separadamente. INT4 sem calibração pode degradar significativamente. Quantização de ativações (não só pesos) é mais difícil.

**Referência:** Dettmers et al. 2022 (LLM.int8()); Frantar et al. 2022 (GPTQ). NeurIPS/ICLR.

---

## 24 — Mixture of Experts (MoE)

**Definição:** Arquitetura que substitui cada FFN por um conjunto de E experts, com um router que seleciona top-K experts por token, mantendo compute constante com parâmetros totais maiores.

**Conceito formal:**
```
h = Σ_{i∈TopK} g_i(x) · FFN_i(x)
g_i(x) = softmax(x W_g)_i
```
Load balancing loss: `L_aux = α · n_experts · Σ_i f_i · P_i` onde f_i = fração de tokens e P_i = probabilidade média para expert i.

**Aplicação:** Switch Transformer, Mixtral-8x7B, GPT-4 (allegedly), DeepSeekMoE. Permite escalar parâmetros sem escalar FLOP por token.

**Pitfalls:** Expert collapse: router converge para poucos experts. Token dropping quando capacity_factor < 1. Expert parallelism adiciona comunicação all-to-all pesada. Difícil de quantizar.

**Referência:** Fedus et al. 2021 (Switch Transformer); Jiang et al. 2024 (Mixtral). JMLR/arXiv.

---

## 25 — Activation Checkpointing (Gradient Checkpointing)

**Definição:** Trade-off memória vs compute: em vez de manter todas as ativações do forward em memória para o backward, recomputa-as on-demand, reduzindo pico de memória.

**Conceito formal:**
- Padrão: memória ∝ `n_layers × batch × seq × d`
- Com checkpointing: memória ∝ `√(n_layers) × batch × seq × d`
- Custo: ~33% mais FLOP (1 forward extra).

**Aplicação:** `torch.utils.checkpoint.checkpoint_sequential`. Padrão em treino de modelos grandes onde o gradiente das ativações não cabe em memória.

**Pitfalls:** Aumenta wall-clock time. Incompatível com certas operações in-place. Recomputation pode ter custo diferente do forward original se RNG não for preservado corretamente.

**Referência:** Chen et al. 2016. "Training Deep Nets with Sublinear Memory Cost." arXiv.

---

## 26 — Continuous Batching

**Definição:** Estratégia de serving que insere novas requisições no batch assim que slots ficam disponíveis (à medida que sequências terminam), em vez de esperar o batch inteiro terminar.

**Conceito formal:** Ao contrário do batching estático onde todos terminam no passo T_max, o continuous batching mantém utilização de GPU constante:
```
throughput_cb >> throughput_static  (especialmente para requests de comprimento variável)
```

**Aplicação:** Orca (Yu 2022), vLLM, TGI. Fundamental para serving LLM de produção com SLA de latência.

**Pitfalls:** Gerenciamento de KV cache mais complexo (diferentes sequências em diferentes posições do cache). Requer PagedAttention ou gerenciamento de blocos similar para ser eficiente.

**Referência:** Yu et al. 2022. "Orca: A Distributed Serving System for Transformer-Based Generative Models." OSDI.

---

## 27 — SGLang / Disaggregated Prefill-Decode

**Definição:** SGLang é um sistema de serving com RadixAttention (cache prefixo compartilhado entre requests). Disaggregated serving separa fisicamente as fases de prefill e decode em hardware diferentes.

**Conceito formal (RadixAttention):** Mantém trie de KV cache para prefixos comuns:
```
hit_rate = tokens_com_prefixo_em_cache / tokens_totais
```
Disaggregation: prefill-bound (compute-bound) → GPU de alta compute; decode-bound (memory-bound) → GPU de alta memória.

**Aplicação:** SGLang para constrained generation (JSON schema, regex). Disaggregation em sistemas de alta escala (Splitwise, DistServe).

**Pitfalls:** Disaggregação adiciona rede de transferência entre prefill e decode nodes. RadixAttention assume alta repetição de prefixo — ineficaz para prompts únicos.

**Referência:** Zheng et al. 2024 (SGLang). arXiv 2312.07104; Patel et al. 2024 (Splitwise). ISCA.

---

## 28 — Hallucination

**Definição:** Geração de conteúdo factualmente incorreto, fabricado, ou não suportado pelo contexto/conhecimento, apresentado com alta confiança pelo modelo.

**Tipos:**
- **Intrinsic:** contradiz o contexto fornecido.
- **Extrinsic:** afirma algo não verificável pelo contexto (nem verdadeiro nem falso em relação ao input).
- **Factual:** fatos do mundo incorretos.

**Aplicação:** Crítico para RAG (hallucinar informação do documento) e medical/legal LLMs. Métricas: FActScore (Min 2023), HaluEval.

**Pitfalls:** Hallucination não é igual a incerteza — modelos frequentemente alucinam com alta confiança (overconfidence). RAG reduz mas não elimina hallucination (modelo pode ignorar contexto recuperado).

**Referência:** Ji et al. 2023. "Survey of Hallucination in Natural Language Generation." ACM Computing Surveys.

---

## 29 — Benchmark Leakage / Data Contamination

**Definição:** Presença de dados de benchmark (ou textos muito similares) no corpus de pré-treinamento, inflando artificialmente as métricas reportadas.

**Conceito formal (detecção — perplexity ratio):**
```
contamination_score = log P_model(benchmark_data) / log P_model(random_text)
```
n-gram overlap com training data também usado (Shi 2023: min-k% tokens matching).

**Aplicação:** MMLU, GSM8K, HumanEval têm contaminação documentada em vários modelos. Detectado via perplexity, n-gram overlap, ou membership inference.

**Pitfalls:** Difícil distinguir "modelo aprendeu habilidade" de "memorizou respostas". Benchmarks populares contaminam mais rápido. Avaliação em benchmarks privados / held-out como alternativa.

**Referência:** Shi et al. 2023. "Detecting Pretraining Data from Large Language Models." ICLR 2024.

---

## 30 — CLIP (Contrastive Language-Image Pretraining)

**Definição:** Modelo de representação multimodal treinado via contrastive learning em 400M pares (imagem, texto), aprendendo embeddings compartilhados para as duas modalidades.

**Conceito formal (InfoNCE em batch de N pares):**
```
L = -1/N Σ_i log exp(sim(I_i, T_i)/τ) / Σ_j exp(sim(I_i, T_j)/τ)
```
τ (temperatura) é parâmetro aprendido. Simetrico: imagem→texto e texto→imagem.

**Aplicação:** Base de DALL-E, Stable Diffusion (text conditioning), LLaVA (visual encoder). Zero-shot classification: comparar embedding da imagem com embeddings de label texts.

**Pitfalls:** Modality gap: embeddings de texto e imagem ocupam regiões diferentes do espaço hipersférico mesmo após treinamento. Weak spatial/compositional reasoning ("red cube on blue sphere" ≠ "blue cube on red sphere" para CLIP).

**Referência:** Radford et al. 2021. "Learning Transferable Visual Models From Natural Language Supervision." ICML.

---

## 31 — Multimodal Alignment

**Definição:** Problema de aprender correspondências entre representações de modalidades diferentes (texto, imagem, áudio) para uma mesma entidade ou conceito.

**Tipos:**
- **Contrastiva:** aprende via pares positivos/negativos (CLIP).
- **Generativa:** aprende via geração cross-modal (caption → image).
- **Implícita:** via co-ocorrência no mesmo modelo (early fusion).

**Aplicação:** Cross-modal retrieval, VQA, image captioning, audio-visual alignment (AV-HuBERT).

**Pitfalls:** Negative sampling crucial: aleatórios muito fáceis → collapse. Hard negatives muito difíceis → instabilidade. Modality gap persiste mesmo com alinhamento forte.

**Referência:** cmu-mmml.github.io; Li et al. 2021 (ALIGN). ICML.

---

## 32 — Tensor Fusion Network (TFN)

**Definição:** Operação de fusão multimodal que computa o produto tensorial externo das representações de cada modalidade, capturando interações de ordem alta entre modalidades.

**Conceito formal:** Para modalidades de representações z_t, z_v, z_a (+ bias 1):
```
z_m = [z_t; 1] ⊗ [z_v; 1] ⊗ [z_a; 1]  ∈ R^{(d_t+1)(d_v+1)(d_a+1)}
```
O produto tensorial captura todas as interações cross-modal.

**Aplicação:** CMU-MOSI e CMU-MOSEI sentiment analysis. Tensor quadratico/cúbico explícito de interações.

**Pitfalls:** Dimensão explode cubicamente: 3 modalidades de 100 dims → 10⁶ features antes de projeção. Low-rank Tucker decomposition (Liu 2018) alivia mas introduz aproximação.

**Referência:** Zadeh et al. 2017. "Tensor Fusion Network for Multimodal Sentiment Analysis." EMNLP.

---

## 33 — Deep CCA (Canonical Correlation Analysis)

**Definição:** Extensão da CCA clássica com redes neurais que aprende transformações não-lineares de duas views de dados que maximizam correlação canônica no espaço latente compartilhado.

**Conceito formal:** CCA clássica: encontra W_x, W_y que maximizam:
```
corr(W_x^T x, W_y^T y)
```
Deep CCA: F_θ(x), G_φ(y) são redes neurais; minimiza -CCA(F_θ(x), G_φ(y)).

**Aplicação:** Alinhamento de embeddings de texto e áudio/imagem. Representação compartilhada para cross-modal retrieval e multimodal generation.

**Pitfalls:** Otimização de correlação canônica é não-convexa e sensível a inicialização. Batch deve ser grande o suficiente para estimativa estável da matriz de covariância.

**Referência:** Andrew et al. 2013. "Deep Canonical Correlation Analysis." ICML.

---

## 34 — Multimodal VAE (MVAE)

**Definição:** Extensão de VAE para múltiplas modalidades que aprende um espaço latente compartilhado capaz de gerar dados de qualquer subset de modalidades, com representações shared e private explicitamente separadas.

**Conceito formal (MVAE ELBO):**
```
L = E_{q(z|x,y)}[log p(x|z) + log p(y|z)] - KL(q(z|x,y) || p(z))
```
Product-of-experts (PoE) para combinar posteriors: `q(z|x,y) ∝ q(z|x) · q(z|y) · p(z)`.

**Aplicação:** Cross-modal generation: dado somente texto, gerar imagem coerente (e vice-versa). Federated multimodal learning.

**Pitfalls:** PoE colapsa para prior quando uma modalidade está ausente em treinamento. Representações shared/private difíceis de disentrenchment sem supervisão adicional.

**Referência:** Wu & Goodman 2018. "Multimodal Generative Models for Scalable Weakly-Supervised Learning." NeurIPS.

---

## 35 — Diffusion Models (DDPM / DDIM)

**Definição:** Modelos generativos que aprendem a reverter um processo de adição de ruído gaussiano, gerando amostras de alta qualidade a partir de ruído.

**Conceito formal (DDPM):**
- Forward: `q(x_t|x_{t-1}) = N(x_t; √(1-β_t)x_{t-1}, β_t I)`
- Reverse: `p_θ(x_{t-1}|x_t) = N(μ_θ(x_t,t), Σ_θ(x_t,t))`
- Training: `L = E[||ε - ε_θ(x_t, t)||²]` (predict noise)
- DDIM: sampling determinístico, permite saltar passos (T/10 passos ainda funciona).

**Aplicação:** Stable Diffusion (latent diffusion), DALL-E 2, Imagen. Score-based generative modeling.

**Pitfalls:** Amostragem lenta (T=1000 passos para DDPM). CFG aumenta diversidade mas pode introduzir artefatos. Treinamento em espaço latente (LDM) pode perder detalhes de alta frequência.

**Referência:** Ho et al. 2020 (DDPM); Song et al. 2020 (DDIM); Rombach et al. 2022 (LDM/Stable Diffusion). NeurIPS/CVPR.

---

## 36 — Membership Inference Attack

**Definição:** Ataque que infere se um dado exemplo específico foi usado no treinamento do modelo, explorado tanto para privacidade quanto para detecção de contaminação.

**Conceito formal (perplexity-based):**
```
score(x) = -log P_model(x) / |x|    (normalizado por comprimento)
```
Exemplos de treino tendem a ter perplexidade menor. Variante: Min-k% (Shi 2023) usa os k% tokens de menor probabilidade.

**Aplicação:** Auditoria de privacidade de LLMs (dados pessoais memorizado?). Detecção de contaminação de benchmarks.

**Pitfalls:** Base rate muito baixa → muitos falsos positivos. Perplexidade depende da distribuição do texto, não só de memorização. Modelos maiores memorizam mais (capacity-dependente).

**Referência:** Carlini et al. 2021. "Extracting Training Data from Large Language Models." USENIX Security.

---

## 37 — Emergent Abilities

**Definição:** Capacidades que surgem abruptamente em modelos acima de certo threshold de escala, sem manifestação clara em modelos menores.

**Conceito formal:** Definição operacional (Wei 2022):
```
ability = emergente se: performance ≈ chance para N < N* e performance >> chance para N > N*
```
N* é o threshold de emergência.

**Aplicação:** Few-shot arithmetic, multi-step reasoning, CoT, code generation. Motivação para scale.

**Pitfalls:** Parcialmente artefato de métrica: com métricas suaves (BPE accuracy) emergência desaparece (Schaeffer 2023). "Emergência" pode ser gradual na perplexidade mas abrupta na métrica de accuracy (hard threshold). Não é garantida para novas capacidades.

**Referência:** Wei et al. 2022. "Emergent Abilities of Large Language Models." TMLR; Schaeffer et al. 2023 (Are Emergent Abilities of LLMs a Mirage?). NeurIPS.
