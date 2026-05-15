# 02 — Schema canônico de `curriculum.md`

> Schema único usado por toda a suite. Produzido pelo Pesquisador Acadêmico (`01-prompt-curriculum.md`), consumido por Coordenador, Professor, Engenheiro de Labs, Banca e Revisor de Fidelidade.
>
> Toda seção é obrigatória. Quando a fonte oficial não publica, registrar `Não informado publicamente` em vez de omitir.

---

## Esqueleto completo

```markdown
# 📚 Grade Curricular — <Nome do Curso>

**Instituição:** <Nome oficial da instituição> — <Unidade acadêmica>
**Programa identificado:** <Nome oficial completo + tipo: Online Graduate Certificate / Master's / Pós lato sensu / etc.>
**Total de carga horária:** <X horas | Não informado publicamente>
**Duração publicada:** <ex: 12 months>
**Próxima entrada publicada:** <ex: Fall 2026 | Não informado publicamente>
**Modalidade:** <Online | Presencial | Híbrida>
**Data de acesso:** YYYY-MM-DD

---

## Fontes Consultadas

Lista todas as URLs oficiais inspecionadas. Categorizar:

- **Página oficial do programa:** <URL>
- **Syllabus público:** <URL>
- **Schedule público:** <URL>
- **Assignments públicos:** <URL>
- **Repositório GitHub do curso:** <URL ou N/A>
- **Páginas pessoais dos professores:** lista
- **Livros-texto dos professores:** lista

### Nota de fidelidade

Texto livre explicando:

- O que está publicado oficialmente (fonte primária).
- O que vem de fonte secundária oficial (syllabus público de edição anterior, GitHub do curso).
- O que NÃO está publicado e foi marcado como `Não informado publicamente`.
- Discrepâncias entre fontes (ex: certificate page lista 3 cursos, syllabus público lista um deles com código diferente).

---

# Programa

## Identificação

| Campo | Valor |
|---|---|
| Nome oficial | |
| Tipo | |
| Instituição | |
| Unidade acadêmica | |
| Duração publicada | |
| Modalidade | |
| Público-alvo declarado | |
| URL oficial | |

---

# Objetivo Oficial do Programa

Cópia fiel do objetivo publicado pela instituição. Sem reformular. Sem expandir. Use bullet list só se a fonte usar.

```txt
<copiado literalmente da fonte oficial>
```

---

# Pré-Requisitos Oficiais

## Para o programa como um todo

Liste textualmente, preservando exigências de matemática, CS, linguagens, frameworks.

## Para disciplinas específicas (quando o syllabus público publica)

Tabela:

| Disciplina | Pré-requisitos publicados |
|---|---|
| `<código>` | `<lista>` |

---

# Professores e Publicações Relevantes

> Preenchido pela persona Pesquisador (`01-prompt-curriculum.md` — Passo 4: Professor Extraction Rule). Esta seção é **fonte primária de leituras** para a persona Professor (`07-professor-disciplina.md`).

Para cada professor identificado:

## <Nome completo do Professor>

- **Afiliação:** <Departamento, Universidade>
- **Página pessoal:** <URL>
- **Disciplinas que leciona neste programa:** <lista>
- **Publicações relevantes ao tema:**
  - <Autores>. *<Título>*. <Venue>, <Ano>. <URL/DOI quando público>
- **Livros-texto publicados:** (se aplicável)
- **Lecture notes / slides públicos:** (se aplicável)

Repita por professor.

---

# Estrutura Curricular Original

> Cole a grade oficial sem reorganizar. A reorganização pedagógica é responsabilidade do Coordenador.

## Módulo 1 — <Nome oficial do módulo, semestre ou disciplina>

**Período publicado:** <ex: Fall 2026>
**Código oficial:** <ex: 11-967>

### 📖 Disciplina: <Nome oficial>

- **Carga Horária:** <X horas | Não informado publicamente>
- **Professor(es):** <Nome(s) | Não informado publicamente>
- **Pré-requisitos:** <Lista | Nenhum>

#### 📝 Ementa

> Cópia fiel da ementa oficial.

#### 📚 Bibliografia

**Básica:**
- <Autor. Título. Editora, Ano.>

**Complementar:**
- <Autor. Título. Editora, Ano.>

#### Avaliações da disciplina (quando publicado)

- <tipo, peso, deadline>

---

Repita o bloco para cada módulo/disciplina.

---

# Aulas / Semanas Oficiais

> Quando a fonte publica cronograma semana a semana, reproduzir literalmente.

| Semana | Tema oficial | Tópicos | Leituras / Entregas |
|---:|---|---|---|
| 01 | | | |
| 02 | | | |

---

# Bibliografia Oficial (consolidada)

## Papers

- <Autores>. *<Título>*. <Venue>, <Ano>. <URL/DOI>

## Livros

- <Autor>. *<Título>*. <Editora>, <Ano>.

## Documentação / Repositórios

- <Nome>. <URL oficial>

---

# Avaliações Oficiais

Descrever provas, projetos, labs, capstone, rubricas, critérios de aprovação publicados.

- <Avaliação 1: descrição, peso, formato>
- <Avaliação 2: ...>

---

# Filosofia Pedagógica Extraída

> **Não preencher na fase de pesquisa.** Esta seção é responsabilidade do Coordenador de Curso (`06-coordenador-curso.md`), que deriva a filosofia a partir do material que o Pesquisador coletou.
>
> Conteúdo esperado depois: ≤ 200 palavras descrevendo o vetor pedagógico (engineering-heavy / research-heavy / systems-heavy / business-oriented / multimodal-heavy / theory-first / hands-on-first), com evidências curtas extraídas das fontes (ex: "8 dos 12 assignments são labs de implementação", "Bibliografia é 80% papers + 20% livro-texto do professor Y").

---

# Cursos-Irmãos Top-Tier Identificados

> Preenchido pelo Pesquisador. Base para a Gap Supplementation Rule (`03-kit-rules.md`).

Lista 2–4 cursos top-tier com material público que cobrem o mesmo domínio. Para cada um, registrar:

- Nome do curso e código.
- Instituição.
- URL oficial do material público.
- Por que é considerado curso-irmão (overlap de tópicos, professores citados em comum, livro-texto compartilhado).

---

# Observações para Adaptação Autodidata

> Preenchido pelo usuário ou pelo Coordenador antes de gerar o kit. Define os parâmetros operacionais.

| Campo | Valor |
|---|---|
| Carga horária desejada por semana | <ex: 10-15h> |
| Duração desejada do kit | <ex: 48 semanas> |
| Proporção teoria/engenharia | <ex: 60% eng / 40% theory> |
| Stack principal | |
| Ambiente de execução | <local GPU / cloud / CPU-only / misto> |
| Idioma de saída | <pt-BR / en-US> |
| Background do aluno | |
| Áreas fracas | |
| Áreas fortes | |
| Objetivo final | <research engineer / LLM systems engineer / GenAI architect / Data Scientist senior> |

---

# Material Bruto Colado da Fonte

> Opcional. Cole aqui texto bruto extraído da página oficial, PDF, ou ementa. Ajuda a preservar terminologia exata e a auditar a fidelidade depois.

```txt
<texto bruto>
```
```

---

## Regras de preenchimento

- **Sempre datar** o acesso. Ementas mudam entre edições.
- **Sempre citar fonte por afirmação**. Ao registrar "carga horária = 360h", indicar de qual URL veio.
- **Preservar idioma original** nas seções de cópia fiel (ementa, objetivo). Não traduzir o que foi publicado em inglês para pt-BR — o aluno consome material em inglês também.
- **Distinguir explicitamente**: oficial × complemento público (syllabus do GitHub do prof) × `Não informado publicamente`.
