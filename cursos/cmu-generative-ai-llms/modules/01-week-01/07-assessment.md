# Assessment — Semana 01: Building Blocks of Modern LLMs

> **Total de pesos: 100**
> **Instrução:** responda sem consultar material. Após, compare com as model answers e aplique a rubrica. Seja honesto — o propósito é identificar gaps, não inflar nota.

---

## Q1. Derivação e intuição do scaling factor
**Categoria:** open-ended / derivação
**Tempo esperado:** 20 minutos
**Peso:** 20 / 100

**Enunciado:**
Seja $\mathbf{q}, \mathbf{k} \in \mathbb{R}^{d_k}$ com componentes i.i.d. $\sim \mathcal{N}(0, 1)$.

(a) Prove que $\text{Var}(\mathbf{q} \cdot \mathbf{k}) = d_k$.

(b) Explique por que variância $d_k$ nos dot products é problemática para o treinamento com softmax.

(c) Mostre que dividir por $\sqrt{d_k}$ normaliza a variância para 1.

(d) Por que o Transformer usa $\sqrt{d_k}$ em vez de, por exemplo, $d_k$ (normalização de variância para $1/d_k$)?

---

### Rubrica Q1

| Nível | Critério |
|---|---|
| A+ | Prova correta de (a) via variância de soma de variáveis independentes; identifica saturação de softmax em (b) com argumento de gradiente (softmax satura → gradiente ~0); derivação correta de (c); em (d) argumenta que $1/d_k$ seria subótimo — produziria scores muito pequenos para d_k grande, equivalente a underfitting da atenção |
| A | Prova (a) correta; identifica a saturação mas sem argumento de gradiente explícito; (c) correto; (d) parcial |
| B | Afirma (a) sem prova; identifica o problema de saturação intuitivamente; (c) correto |
| C | Diz "para estabilidade numérica" sem derivação; sem prova |
| F | Confunde variância com desvio padrão na prova; ou não responde (b)/(c) |

### Model answer (A+)

**(a)** Seja $z = \mathbf{q} \cdot \mathbf{k} = \sum_{i=1}^{d_k} q_i k_i$. Como $q_i$ e $k_j$ são independentes com média 0 e variância 1:

$$\text{Var}(q_i k_i) = \mathbb{E}[(q_i k_i)^2] - (\mathbb{E}[q_i k_i])^2 = \mathbb{E}[q_i^2]\mathbb{E}[k_i^2] - 0 = 1$$

Por independência dos termos e aditividade da variância:

$$\text{Var}(z) = \sum_{i=1}^{d_k} \text{Var}(q_i k_i) = d_k$$

**(b)** Com variância $d_k$, o desvio padrão dos scores é $\sqrt{d_k}$. Para $d_k = 512$, scores típicos têm magnitude $\pm 22$. Na região $|z| \gg 1$, o softmax concentra quase toda probabilidade no máximo: $\sigma(z)_i \approx \mathbf{1}[i = \arg\max j] + O(e^{-\Delta z})$. O gradiente da loss em relação aos scores $s$ é proporcional a $(\sigma(s) - \mathbf{1}[\text{correct}])$ — que é $\approx 0$ quando o softmax é muito concentrado. Logo: **gradients near zero → learning stalls**.

**(c)** Se $s = z / \sqrt{d_k}$, então $\text{Var}(s) = \text{Var}(z) / d_k = d_k / d_k = 1$. A distribuição dos scores ficará com desvio padrão $\approx 1$ independente de $d_k$.

**(d)** Dividir por $d_k$ (em vez de $\sqrt{d_k}$) produziria $\text{Var}(s) = 1/d_k$. Para $d_k = 512$, os scores teriam desvio padrão $\approx 0.044$ — distribuição tão estreita que o softmax seria quase uniforme independentemente do input. O modelo não conseguiria aprender a distinguir tokens. O fator $\sqrt{d_k}$ é o ponto de equilíbrio: variância 1 → softmax nem saturado nem uniforme.

**Pitfalls comuns:**
- Confundir $\text{Var}(X \cdot Y) = \text{Var}(X)\text{Var}(Y)$ apenas quando X e Y são independentes com média zero.
- Dizer "para estabilidade numérica" sem mencionar gradientes — estabilidade é consequência, não causa.
- Não responder (d) — a questão _por que sqrt_ (não uma constante menor ou maior) é a mais instigante.

**Referências:** Vaswani et al. 2017, Seção 3.2.1; Goodfellow et al. 2016, Cap. 6 (gradients in deep networks).

---

## Q2. Design question — escolha de arquitetura
**Categoria:** design
**Tempo esperado:** 15 minutos
**Peso:** 20 / 100

**Enunciado:**
Você precisa construir um modelo para classificação de sentimento em reviews de produto (input: texto, output: positivo/negativo). Você tem acesso a BERT-base e GPT-2-small pré-treinados. Ambos têm ~110M de parâmetros.

(a) Qual escolheria para fine-tuning? Justifique com base nas diferenças arquiteturais (não apenas "BERT foi treinado em mais dados").

(b) Para geração de reviews sintéticos como data augmentation, qual usaria? Por quê?

(c) Qual a limitação fundamental de usar GPT-2 para classificação sem modificação arquitetural?

---

### Rubrica Q2

| Nível | Critério |
|---|---|
| A+ | (a) BERT com justificativa sobre atenção bidirecional vs unidirecional e por que classificação precisa de representação do input completo; (b) GPT-2 por ser generativo nativo (CLM); (c) identifica que CLM é autoregressive e não produz representação da sequência inteira sem modificação (usa apenas o último token como "summary" — hack, não design) |
| A | (a) e (b) corretos com justificativa parcial; (c) identificado mas mal explicado |
| B | (a) correto mas justificativa superficial ("BERT é melhor para classificação"); (b) correto; (c) confuso |
| C | Escolha correta mas sem justificativa arquitetural |
| F | Inverte (a) e (b), ou não consegue justificar nem uma das escolhas |

### Model answer (A+)

**(a) BERT para classificação.** BERT usa atenção bidirecional — o token `[CLS]` atende a todos os tokens da sequência de ambas as direções, produzindo uma representação que integra contexto completo. GPT-2 usa causal masking: cada token vê apenas tokens anteriores. Para classificação de sentimento, o último token (posição T) não "viu" diretamente tokens no meio da sequência de forma bidirecional — precisaria de atenção para a frente e para trás para capturar ironias ou negações ("this was NOT what I expected — absolutely wonderful"). O `[CLS]` do BERT com atenção bidirecional é arquiteturalmente mais adequado para esse tipo de representação holística.

**(b) GPT-2 para geração.** CLM é o objetivo de geração natural — dada uma sequência, prevê o próximo token. Isso permite amostrar sequências completas de forma autoregressiva: `model.generate(...)`. BERT com MLM não gera texto completo de forma natural sem modificações como BERT-for-generation ou modificação para seq2seq.

**(c) Limitação do GPT-2 para classificação.** GPT-2 não produz inerentemente uma representação "resumo" da sequência inteira. O hack comum é pegar a representação do último token como classificador — mas esse token, por causal masking, não atendeu diretamente a nenhum token futuro. Funciona empiricamente em alguns casos mas é arquiteturalmente inadequado comparado ao `[CLS]` do BERT. A alternativa seria adicionar um token especial de "fim" e usar sua representação, similar ao que alguns trabalhos fizeram — mas aí você está remendando o modelo, não usando-o como foi projetado.

**Pitfalls comuns:**
- Justificar apenas com tamanho de corpus de pre-training (irrelevante para a comparação arquitetural).
- Dizer "BERT é para NLU e GPT é para NLG" sem explicar *por que* arquiteturalmente.

**Referências:** Devlin et al. 2019 (BERT); Radford et al. 2019 (GPT-2); Raffel et al. 2020 (T5, que discute encoder-decoder trade-offs).

---

## Q3. Tradeoff analysis — MHA vs atenção simples
**Categoria:** tradeoff analysis
**Tempo esperado:** 15 minutos
**Peso:** 20 / 100

**Enunciado:**
Compare MHA com h=1 (single-head attention com projeções $W^Q, W^K, W^V$ de dimensão $d_{\text{model}} \times d_{\text{model}}$) contra MHA com h=8 e $d_k = d_{\text{model}}/8$.

(a) Qual tem mais parâmetros de projeção? Calcule para $d_{\text{model}} = 512$.

(b) Qual tem maior custo em FLOPs por forward pass? Justifique.

(c) Quando h=1 seria preferível a h=8? Cite pelo menos um cenário empírico ou teórico.

---

### Rubrica Q3

| Nível | Critério |
|---|---|
| A+ | (a) iguais: ambos têm 3×512×512 projeções + W_O 512×512; (b) iguais também — dividir em h heads com d_k=d_model/h mantém os FLOPs constantes; (c) evidência de que heads muito pequenas (d_k=1 para h muito grande) perdem capacidade expressiva por espaço de projeção insuficiente — cita algum ablation study (ex: Michel et al. 2019 "Are Sixteen Heads Better Than One?") |
| A | (a) correto; (b) afirma igualdade mas sem derivação; (c) menciona overparameterization ou d_k muito pequeno |
| B | (a) errado (acha que h=1 tem mais parâmetros); (b) parcialmente correto; (c) intuitivo mas sem evidência |
| C | Confunde n_heads com n_parâmetros; sem cálculo |
| F | Afirma que h=8 tem 8x mais parâmetros |

### Model answer (A+)

**(a) Iguais.** Para h=1 com $d_{\text{model}}=512$: $W^Q, W^K, W^V \in \mathbb{R}^{512 \times 512}$ → $3 \times 512^2 = 786{,}432$ parâmetros. $W^O \in \mathbb{R}^{512 \times 512}$ → $262{,}144$. Total: $\approx 1.05$M.

Para h=8: cada head tem $W_i^Q, W_i^K, W_i^V \in \mathbb{R}^{512 \times 64}$ (d_k=64). Total: $8 \times 3 \times 512 \times 64 = 786{,}432$. Mesmo número. W_O idêntico. **MHA com h cabeças tem exatamente os mesmos parâmetros que single-head desde que $d_k = d_{\text{model}}/h$.**

**(b) FLOPs também iguais.** Para h heads, cada head processa $d_k$ dimensões em sequência de comprimento n: custo por head = $O(n^2 d_k + n d_k^2)$. Somando h heads: $h \times O(n^2 d_k + n d_k^2) = O(n^2 d_{\text{model}} + n d_{\text{model}}^2 / h)$. Para h=1: $O(n^2 d_{\text{model}} + n d_{\text{model}}^2)$. Para n≪d_model, o segundo termo domina e h=8 tem FLOPs ligeiramente menores (fator h no denominador). Na prática, para tamanhos usuais, são aproximadamente iguais.

**(c) Quando h=1 pode ser melhor.** Michel et al. 2019 "Are Sixteen Heads Really Better Than One?" mostrou via ablation que em tasks de tradução, até 70% das heads podem ser removidas sem degradação — sugerindo que muitas heads são redundantes. Em regimes de poucos dados ou modelos pequenos, heads muito numerosas com $d_k$ muito pequeno (ex: h=32 com $d_k=2$) podem não ter capacidade de representação suficiente por head. O trade-off empírico: h ∈ {8, 16, 32} para modelos de tamanho médio; não há benefício claro acima de 32 heads para $d_{\text{model}} = 512$.

**Pitfalls comuns:**
- Afirmar que h=8 tem 8x mais parâmetros (erro clássico).
- Não perceber que FLOPs são conservados com a divisão de d_k.

**Referências:** Michel et al. 2019 (Are Sixteen Heads Really Better Than One?); Vaswani et al. 2017 Tabela 3 (ablation sobre n_heads).

---

## Q4. Debugging de código — softmax axis error
**Categoria:** debugging
**Tempo esperado:** 10 minutos
**Peso:** 15 / 100

**Enunciado:**
O seguinte código PyTorch produz um resultado silenciosamente errado (não gera exceção mas produz output incorreto). Identifique o bug, explique por que é silencioso, e escreva a versão correta.

```python
import torch
import torch.nn.functional as F

def broken_mha_forward(Q, K, V):
    # Q, K, V: (batch=2, heads=4, seq=8, d_k=16)
    d_k = Q.size(-1)
    scores = torch.bmm(Q.view(-1, 8, 16), K.view(-1, 16, 8)) / (d_k ** 0.5)
    weights = F.softmax(scores, dim=1)  # BUG
    out = torch.bmm(weights, V.view(-1, 8, 16))
    return out.view(2, 4, 8, 16), weights

Q = torch.randn(2, 4, 8, 16)
K = torch.randn(2, 4, 8, 16)
V = torch.randn(2, 4, 8, 16)
out, w = broken_mha_forward(Q, K, V)
print(w.sum(dim=1))  # O que você espera vs o que você recebe?
```

---

### Rubrica Q4

| Nível | Critério |
|---|---|
| A+ | Identifica `dim=1` deveria ser `dim=-1` ou `dim=2`; explica que `dim=1` normaliza sobre as 8 posições na dimensão de "heads-collapsed" view, não sobre a dimensão key — os pesos somam 1 por coluna de keys em vez de por linha de queries; detecta que o bug é silencioso porque `softmax` sempre produz valores em (0,1) somando 1 em alguma dimensão — não gera erro de shape |
| A | Identifica o dim errado; explica parcialmente por que é silencioso |
| B | Identifica o bug mas não explica o que `dim=1` faz incorretamente |
| C | Vê que tem um bug mas não consegue localizar |
| F | Não identifica o bug ou propõe mudança errada |

### Model answer (A+)

**Bug:** `F.softmax(scores, dim=1)` aplica softmax sobre a dimensão 1. Após o `view(-1, 8, 8)`, o tensor tem shape `(batch*heads, seq_q, seq_k) = (8, 8, 8)`. A dimensão 1 corresponde à dimensão de queries (seq_q), não de keys (seq_k). O correto é `dim=-1` ou `dim=2`, que normaliza sobre keys para cada query — dando a distribuição de atenção "quanto cada query atende a cada key".

**Por que é silencioso:** `F.softmax` com qualquer dim válida não gera exceção. O tensor de output continua com shape correto e valores em (0,1). A verificação `weights.sum(dim=...)` passaria se você somar no eixo errado — `w.sum(dim=1)` daria uma matriz de 1s (coincidentemente, a soma correta mas no eixo errado).

**Versão correta:**
```python
weights = F.softmax(scores, dim=-1)  # normaliza sobre seq_k (último eixo)
```

**Como detectar:** `w.sum(dim=-1)` deve retornar uma matriz de 1s. Com o bug: `w.sum(dim=-1)` produz valores que não são 1.

**Pitfalls comuns:** Usar `view(-1, ...)` collapsa batch e heads sem separar explicitamente — dificulta rastreamento de qual dimensão é qual. Preferível usar `reshape` com shape explícito ou manter dimensões separadas.

**Referências:** PyTorch docs — `torch.nn.functional.softmax`; Kaplan et al. (qualquer paper que usa MHA — sempre `dim=-1`).

---

## Q5. Paper critique — Attention is All You Need
**Categoria:** paper critique
**Tempo esperado:** 20 minutos
**Peso:** 25 / 100

**Enunciado:**
Com base em sua leitura de Vaswani et al. 2017:

(a) Identifique a contribuição técnica principal. Evite parafrasear o abstract — explique o que especificamente era novo em relação ao estado da arte de 2017 (LSTM + attention de Bahdanau).

(b) Identifique a limitação mais significativa do paper como publicado em 2017, que motivou pesquisa subsequente (cite o paper subsequente que endereçou essa limitação).

(c) A Tabela 2 do paper reporta BLEU de 41.0 para EN→DE. Um revisor argumenta: "Esse benchmark está contaminado porque os dados do WMT14 são públicos e o modelo provavelmente foi ajustado para esse dataset". Avalie esse argumento: é válido? Por que ou por que não?

---

### Rubrica Q5

| Nível | Critério |
|---|---|
| A+ | (a) identifica especificamente que a novidade é eliminar recorrência *e* convolução, mantendo somente atenção — e que isso permite paralelização total e caminho de informação O(1); (b) limitação de comprimento fixo / posicional encoding que não generaliza + cita trabalho subsequente (ex: Press et al. 2022 ALiBi, ou Su et al. 2021 RoPE); (c) argumento inválido — benchmark leakage exigiria que exemplos de teste fossem vistos no treinamento, o que é metodologicamente improvável com WMT14 train/test split; confunde "dataset público" com "test set visto em treinamento" |
| A | (a) correto mas parcial (menciona paralelização sem O(1) path); (b) limitação correta com ou sem citação; (c) parcialmente correto |
| B | (a) parafraseia abstract; (b) identifica limitação; (c) ou valida o argumento erroneamente ou invalida sem justificativa |
| C | (a) superficial; (b) identifica limitação mas sem evidência; (c) não responde |
| F | (a) parafraseia o título; confunde contribuição com resultados |

### Model answer (A+)

**(a) Contribuição central.** O estado da arte em 2017 para sequências eram LSTMs com atenção de Bahdanau: o encoder LSTM processa a entrada sequencialmente (sem paralelização), e a atenção é aditiva ($e_{ij} = v^\top \tanh(W_a s_i + U_a h_j)$) com custo $O(n)$ por step. O Transformer elimina a recorrência completamente — a atenção opera diretamente sobre todos os tokens em paralelo, com caminho de informação de O(1) hops entre quaisquer dois tokens. Isso habilita: (1) paralelização total no treinamento (sem dependência sequencial), (2) caminho de gradiente mais curto (reduz problema de gradiente de longo alcance), (3) custo por layer O(n²d) vs O(nd²) para LSTM. A trade-off é o custo quadrático em n — aceitável para sequências curtas de 2017.

**(b) Limitação principal.** O positional encoding sinusoidal não generaliza para comprimentos maiores que os vistos em treinamento. Papers que endereçaram:
- Su et al. 2021 (RoPE): embedding rotacional relativo — permite extrapolação natural.
- Press et al. 2022 (ALiBi): adiciona viés linear ao score de atenção, sem embedding posicional — generaliza para sequências longas sem retreinamento.

**(c) Argumento inválido.** "Dataset público" não implica "test set visto em treinamento". Benchmark leakage (contaminação) ocorre quando exemplos de teste aparecem no conjunto de treinamento — o que requereria que os autores tenham incluído especificamente os pares de tradução do test set de WMT14 no corpus de treinamento. O train/test split do WMT14 é padrão na área e não implica tal contaminação. O argumento confunde "o dataset de treinamento é público" com "os exemplos de teste foram vistos em treinamento" — são proposições completamente distintas. Contaminação no sentido moderno (benchmark memorizado de dados web) não se aplica aqui porque os autores coletaram e processaram o corpus explicitamente.

**Pitfalls comuns:**
- Em (a): citar "multi-head attention" como a contribuição, quando MHA é uma extensão natural da atenção de Bahdanau — a novidade real é a eliminação da recorrência.
- Em (c): validar o argumento do revisor sem analisar o que "contaminação" significa tecnicamente.

**Referências:** Vaswani et al. 2017; Bahdanau et al. 2015 (atenção de seq2seq); Press et al. 2022 (ALiBi); Su et al. 2021 (RoPE).
