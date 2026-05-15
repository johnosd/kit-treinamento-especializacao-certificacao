# Readings — Semana 01

> **Roteiro de leitura:** leia na ordem listada. As obrigatórias cobrem a mecânica; as complementares aprofundam aspectos específicos.

---

## Leituras obrigatórias

---

### Paper (seminal)

- **Citação:** Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., & Polosukhin, I. (2017). Attention is All You Need. *Advances in Neural Information Processing Systems (NeurIPS)*, 30.
- **URL:** https://arxiv.org/abs/1706.03762
- **Por que ler:** O paper que define a arquitetura base de todos os LLMs modernos. Leitura primária obrigatória — cada seção desta semana mapeia para uma seção do paper.
- **Tempo estimado:** 2h (primeira leitura com anotações)
- **Foco:**
  1. Por que os autores chamam o mecanismo de "scaled" dot-product attention — qual a justificativa para o fator de escala?
  2. Qual a diferença entre self-attention e cross-attention? Quando cada um aparece na arquitetura?
  3. Como a complexidade computacional por layer do Transformer compara com LSTM e CNN convolucional? (Tabela 1 do paper)
  4. Por que positional encoding é necessário e como o encoding sinusoidal permite generalização para comprimentos não vistos?

---

### Paper (encoder-only / MLM)

- **Citação:** Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. *NAACL-HLT*, 4171–4186.
- **URL:** https://arxiv.org/abs/1810.04805
- **Por que ler:** Estabelece MLM como objetivo de pré-treinamento para encoders. Define o padrão de fine-tuning em tasks de NLU que dominou 2019–2021.
- **Tempo estimado:** 1.5h
- **Foco:**
  1. Por que o MLM mascara 15% dos tokens de forma não-uniforme (80%/10%/10%)? Qual a intuição para o 10% de tokens aleatórios?
  2. Qual a limitação fundamental do BERT para geração de texto? Por que você não pode usar BERT diretamente para completar uma frase?
  3. O que é Next Sentence Prediction (NSP) e por que experimentos posteriores (RoBERTa, Liu 2019) mostraram que ele não ajuda?
  4. Qual a diferença entre BERT-Base e BERT-Large em número de parâmetros, heads e layers?

---

### Paper (decoder-only / CLM em escala)

- **Citação:** Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., ... & Amodei, D. (2020). Language Models are Few-Shot Learners. *NeurIPS*, 33.
- **URL:** https://arxiv.org/abs/2005.14165
- **Por que ler:** Demonstra que CLM em escala emergiu em few-shot learning sem fine-tuning. Define o paradigma de in-context learning (S05). Seções 2.1–2.3 são obrigatórias para esta semana; seções de benchmark podem ser lidas mais tarde.
- **Tempo estimado:** 1.5h (foco nas seções 2.1–2.3 e experimentos ICL)
- **Foco:**
  1. Qual a diferença entre "few-shot", "one-shot", e "zero-shot" conforme definido neste paper?
  2. Como o GPT-3 é treinado em relação ao GPT-2 (Radford 2019)? Qual é a principal mudança de design?
  3. Qual a relação entre escala (número de parâmetros) e capacidade de few-shot no paper? A relação é linear?
  4. Qual a principal limitação de usar GPT-3 para tasks de raciocínio multi-step, identificada pelos autores?

---

### Tutorial (referência prática — Professor Extraction Rule)

- **Citação:** Neubig, G. (2017). Neural Machine Translation and Sequence-to-sequence Models: A Tutorial. *arXiv preprint*.
- **URL:** https://arxiv.org/abs/1703.01619
- **Por que ler:** Graham Neubig (CMU LTI, co-faculty do certificado) tem tutorial didático cobrindo seq2seq e atenção — contexto histórico direto de onde o Transformer surgiu. Capítulos 1–4 são relevantes para esta semana.
- **Tempo estimado:** 1h (caps. 1–4)
- **Foco:**
  1. Como a atenção de Bahdanau (2015) difere da atenção dot-product do Transformer? Qual a vantagem computacional da dot-product?
  2. O que o tutorial identifica como limitação dos RNNs que motivou a busca por alternativas?

---

## Leituras complementares

---

### Paper (arquitetura de referência moderna)

- **Citação:** Touvron, H., Lavril, T., Izacard, G., Martinet, X., Lachaux, M.-A., Lacroix, T., ... & Lample, G. (2023). LLaMA: Open and Efficient Foundation Language Models. *arXiv preprint*.
- **URL:** https://arxiv.org/abs/2302.13971
- **Por que ler:** LLaMA é o modelo open-weight de referência. A seção 2 descreve como o Transformer original foi modificado para treino eficiente: Pre-LN → RMSNorm, sinusoidal PE → RoPE, ReLU → SwiGLU. Conecta diretamente esta semana com S02.
- **Tempo estimado:** 45min (seções 1–2)

---

### Lecture notes (material oficial do curso)

- **Citação:** CMU 11-667 (Fall 2025). Lecture 1: Building Blocks of Modern LLMs. *2025.cmu-llms.org*.
- **URL:** https://2025.cmu-llms.org/schedule/
- **Por que ler:** Slides e notas da aula oficial. Prioridade para qualquer diagrama ou notação que difira deste material.
- **Tempo estimado:** 30min

---

### Blog post técnico (opcional — arquitetura detalhada)

- **Citação:** The Annotated Transformer. Rush, A. M. (2018). *Harvard NLP Group*. Atualizado para PyTorch 2.x por Huang, A. et al.
- **URL:** https://nlp.seas.harvard.edu/annotated-transformer/
- **Por que ler:** Implementação linha-a-linha do paper Vaswani 2017 em PyTorch com anotações. Use como referência para validar sua implementação no lab.
- **Nota:** É um blog técnico de grupo acadêmico (Harvard NLP), não um blog genérico — qualificado por §2 do kit-rules.
- **Tempo estimado:** 1h (com código)

---

### Paper (induction heads — por que MHA funciona)

- **Citação:** Elhage, N., Nanda, N., Olsson, C., Henighan, T., Joseph, N., Mann, B., ... & Olah, C. (2021). A Mathematical Framework for Transformer Circuits. *Transformer Circuits Thread*.
- **URL:** https://transformer-circuits.pub/2021/framework/index.html
- **Por que ler:** Explica o mecanismo emergente mais relevante descoberto em Transformers pequenos: "induction heads" que implementam cópia de in-context. Conecta com S05 (ICL) e S07 (interpretability).
- **Tempo estimado:** 1.5h (seções 1–3)
