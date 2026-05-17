# 03 — Regras pedagógicas (válidas para todas as personagens)

> Estas regras se aplicam a **todas** as personagens da suite (`06`–`10`). Toda persona deve, antes de gerar, consultar este arquivo e o vetor de filosofia pedagógica extraído pelo Coordenador.

---

## 1. Qualidade acadêmica

O material gerado deve ter nível de:

- pós-graduação técnica
- mestrado profissional
- research engineering
- senior/principal engineer training

**NUNCA gerar**:

- conteúdo superficial
- tutorial de iniciante
- "hello world" inútil
- explicações infantis
- fluff
- motivação genérica
- texto introdutório que não acrescenta densidade técnica

---

## 2. Fontes permitidas

### Prioridade máxima

- papers originais (arxiv, ACL, NeurIPS, ICLR, ICML, KDD, SIGMOD, OSDI, SOSP, …)
- documentação oficial (pytorch.org, tensorflow.org, huggingface.co, kubernetes.io, docs.aws.amazon.com, learn.microsoft.com, developer.nvidia.com)
- repositórios oficiais (github.com/<projeto>)
- livros-texto reconhecidos pela comunidade
- lecture notes/slides publicados pela própria instituição

### Permitidas

- arxiv.org, paperswithcode.com
- huggingface.co, pytorch.org, tensorflow.org
- openai.com, anthropic.com, mistral.ai, llama.meta.com
- docs.vllm.ai, ray.io, kubernetes.io
- docs.aws.amazon.com, learn.microsoft.com, cloud.google.com/docs
- developer.nvidia.com, docs.databricks.com
- GitHub oficial dos projetos

### NUNCA usar

- blogs genéricos
- Medium aleatório
- cursos genéricos de marketplace (Udemy/Coursera quando não-oficial)
- YouTube genérico (canais de creators sem afiliação acadêmica)
- conteúdo motivacional
- sites de "resumo" / "cheatsheets" de terceiros

---

## 3. Profundidade obrigatória

Toda explicação técnica deve cobrir, quando aplicável:

- teoria (matemática, complexidade, derivações)
- implementação (código real, não pseudocódigo)
- arquitetura (componentes, contratos, fluxos de dados)
- tradeoffs
- limitações
- scaling (latência, throughput, custo)
- avaliação (métricas, benchmarks)
- failure modes
- deployment
- custo computacional

Se um tópico não cobre 5+ desses, ele provavelmente está raso.

---

## 4. Regras transversais novas (críticas para "clone perfeito")

### 4.1 Source Diversity Rule

Para instituições top-tier (Harvard, MIT, Stanford, CMU, Berkeley, Princeton, Yale, Oxford, Cambridge, ETH, EPFL, Caltech, NYU, Columbia, U Toronto, UCL, Imperial College):

- **≥ 2 fontes oficiais corroborantes** antes de afirmar conteúdo de um tópico.
- Se só uma fonte existe, declarar essa limitação no output da persona em uso.
- Aplicada principalmente no Pesquisador (`01`) e no Revisor de Fidelidade (`10`).

### 4.2 Professor Extraction Rule

- Identificar os professores reais da disciplina e usar suas publicações como **leituras primárias** quando o tema bate.
- Operacionalização: a persona Professor (`07-professor-disciplina.md`) recebe a lista de publicações do prof real (extraída na seção `# Professores e Publicações Relevantes` do `02-curriculum.md`) e adiciona pelo menos uma delas à seção `02-readings.md` da semana.
- Quando o programa não publica os professores (`Não informado publicamente`), o Professor usa autores canônicos do tema documentados pelos cursos-irmãos top-tier.

### 4.3 Gap Supplementation Rule

Quando uma semana ou tópico está marcado como `Não informado publicamente` no `02-curriculum.md`, a suplementação segue ordem estrita:

1. **Curso-irmão top-tier** (primeira escolha): use o material correspondente em algum dos cursos listados em `# Cursos-Irmãos Top-Tier Identificados`. Ex: CMU não publica detalhe da semana 5 → ver Stanford CS324 semana equivalente.
2. **Sequência canônica de papers seminais** do tema, quando nem o curso-irmão publica.
3. **Capítulo correspondente do livro-texto do professor**, quando o professor publicou livro.

Toda suplementação deve declarar explicitamente a fonte no arquivo gerado. Padrão de declaração:

```markdown
> **Suplementado de:** Stanford CS324, Lecture 7 ("Mixture of Experts").
> **Razão:** CMU 11-967 syllabus público não publica detalhe deste tópico.
> **Fonte:** https://stanford-cs324.github.io/winter2022/lectures/moe/
```

**Nunca suplementar sem declarar**. A integridade do clone depende dessa rastreabilidade.

### 4.4 Philosophy Preservation Rule

Antes de gerar conteúdo, toda persona consulta a seção `# Filosofia Pedagógica Extraída` do `02-curriculum.md` (preenchida pelo Coordenador). Esse vetor calibra:

- A proporção theory/engineering por semana (research-heavy programs → mais leitura de papers; engineering-heavy → mais labs).
- A escolha de exemplos (systems-heavy programs → exemplos de inferência distribuída; business-oriented → exemplos com ROI).
- A voz da explicação (research-heavy → linguagem de paper; engineering-heavy → linguagem de spec técnica).
- A natureza das avaliações (research → "leia o paper X e critique a contribuição"; engineering → "implemente Y e benchmark contra baseline Z").

Quando a filosofia colide com preferências do aluno declaradas em `# Observações para Adaptação Autodidata`, a **filosofia do programa prevalece** (o objetivo é clonar a especialização, não criar uma versão personalizada).

### 4.5 Theory-as-pointers Rule

O Professor (`07`) **não reescreve o livro-texto**. Quando existe livro canônico que cobre o tópico:

1. Escreve resumo conciso de **300–600 palavras** que conecta o tópico ao restante do programa, explica intuição e indica o que será exercitado no notebook.
2. Inclui bloco obrigatório `## Leituras canônicas (capítulos)` apontando **capítulo/seção/páginas específicas** — não título solto.
   - ✅ Bom: `Géron 2019, *Hands-On ML*, cap. 4 §4.2, pp. 132–145.`
   - ❌ Ruim: `Leia Géron 2019.`
3. Pode incluir derivação curta de 1–2 pontos críticos (e.g., justificar $\sqrt{d_k}$ porque o aluno vai implementar isso no notebook). Não derivar tudo.
4. Sempre indicar **tempo estimado** de leitura por capítulo apontado.

Quando **não existe** livro canônico (paper de research recente, tópico de fronteira sem livro publicado), o Professor escreve denso como antes, e declara no topo: `> Sem livro canônico identificado — teoria escrita por extenso.`

Operacionalização:

- Aplicada no Professor (`07`) durante a geração.
- Verificada pelo Revisor de Fidelidade (`10`) ao auditar a semana.

### 4.6 Notebook-first Practice Rule

Labs são por default **Jupyter notebooks** (`.ipynb`), no formato "FIA-style":

- células markdown curtas (200–400 palavras por bloco) explicando o conceito;
- célula de código executável logo abaixo (`pip install`, imports, transformações reais);
- célula markdown de interpretação do output (o que esses números significam? qual decisão técnica eles implicam?);
- repete por etapa do lab.

Convenções:

- `03-lab-guided` agora é `.ipynb`. O `04-lab-speedrun` continua `.md` (referência condensada para revisão futura — não é executável, é cola de comandos).
- `01-theory` continua `.md` por default. **Pode** virar `.ipynb` quando "aprender fazendo" funciona melhor que explicar (e.g., feature engineering, EDA, transformações de dados — qualquer coisa onde demonstrar é mais barato que descrever).
- Todo notebook deve ter:
  - kernel spec declarado (Python 3.x);
  - `requirements.txt` no mesmo `code/`;
  - outputs preservados após execução (não notebook "limpo" sem run);
  - seeds fixados quando há randomness.

Aplicada no Eng. de Labs (`08`) durante a geração. Verificada pelo Revisor (`10`).

---

## 5. Objetivo pedagógico final

Ao concluir o kit, o aluno deve poder defender tecnicamente o domínio como um egresso da especialização original. Especificamente:

- explicar fundamentos com matemática e código
- ler papers modernos e sintetizar contribuição/limitação
- reproduzir resultados publicados
- avaliar modelos/sistemas em benchmarks reconhecidos
- projetar arquiteturas em escala
- discutir tradeoffs como um engineer/researcher sênior
- entregar projetos com benchmark e análise crítica

---

## 6. Anti-padrões a evitar

- Gerar conteúdo sem citar fonte.
- Misturar inferência pedagógica com fato oficial sem distinguir.
- Inventar professor, paper, livro, dataset.
- Substituir lab real por "exemplo didático".
- Repetir conteúdo já coberto em semana anterior sem agregar profundidade.
- Avaliação só com múltipla escolha trivial.
- Mini-project desconectado do tema da semana.

---

## 7. Critério de sucesso final

O material gerado deve parecer uma mistura de:

- CMU
- Stanford
- Berkeley
- HuggingFace engineering blogs
- OpenAI / Anthropic engineering write-ups
- Systems engineering training

E **NÃO**:

- bootcamp superficial
- curso de influencer
- tutorial introdutório de blog
