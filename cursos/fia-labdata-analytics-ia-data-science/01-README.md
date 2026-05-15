# FIA Business School / Labdata FIA — Analytics e Inteligência Artificial — Data Science

Kit autodidata de nível pós-graduação técnica, derivado da matriz pública da Pós-Graduação Analytics e Inteligência Artificial — Data Science da FIA Business School / Labdata FIA.

Este kit não é material oficial da FIA. Ele é uma adaptação autodidata baseada nas fontes oficiais registradas em `curriculum.md`, complementada com papers, documentação oficial e projetos práticos para atingir profundidade técnica equivalente a uma especialização séria em Data Science, Machine Learning, Deep Learning e Generative AI.

---

## Visão Geral

| Campo | Valor |
|---|---|
| Programa de referência | Pós-Graduação Analytics e Inteligência Artificial — Data Science |
| Instituição de referência | FIA Business School / Labdata FIA |
| Carga oficial publicada | 360 horas |
| Duração oficial publicada | 16 meses |
| Plano autodidata | 64 semanas |
| Carga recomendada | 8-12h/semana |
| Proporção sugerida | 65% engenharia / 35% teoria |
| Idioma | pt-BR, com termos técnicos em inglês quando necessário |
| Stack principal | Python, Google Colab, pandas, scikit-learn, TensorFlow/Keras, PyTorch, Hugging Face, XGBoost, LightGBM, CatBoost, SHAP, LIME, MLflow, LLM APIs, RAG tooling |
| Ambiente | misto: local CPU/GPU quando disponível, Google Colab/cloud notebooks e APIs comerciais para labs de LLM |

---

## Objetivos Finais

Ao concluir o programa, o aluno deve ser capaz de:

- estruturar bases de dados para análise e modelagem;
- executar EDA rigorosa, visualização e diagnóstico estatístico;
- treinar, validar, comparar e explicar modelos de regressão, classificação, séries temporais e segmentação;
- aplicar AutoML sem perder controle sobre validação, leakage, custo e interpretabilidade;
- implementar pipelines de MLOps com versionamento, monitoramento e reprodutibilidade;
- construir redes neurais densas, convolucionais e recorrentes;
- entender Transformers, GPT, embeddings, attention, tokenization e limitações de LLMs;
- implementar RAG, agentes, tool calling, avaliação de prompts e observabilidade de sistemas GenAI;
- projetar soluções de IA com arquitetura, avaliação, custo computacional, failure modes e critérios de negócio;
- defender tecnicamente um projeto final com benchmark, tradeoffs, documentação e análise crítica.

---

## Metodologia

Cada semana deve combinar quatro camadas:

1. **Teoria técnica:** matemática, estatística, arquitetura, algoritmos, papers e limitações.
2. **Implementação:** código em Python, notebooks, bibliotecas reais e experimentos reprodutíveis.
3. **Engenharia de sistemas:** dados, versionamento, avaliação, monitoramento, deployment, custo e failure modes.
4. **Produção intelectual:** notas técnicas, flashcards, revisões, mini-projetos e decisões documentadas.

Use a matriz oficial como eixo curricular, mas trate este kit como uma especialização prática. A régua de qualidade é: conseguir explicar e implementar, não apenas reconhecer conceitos.

---

## Como Estudar

Mantenha um ciclo semanal fixo:

| Bloco | Tempo sugerido | Atividade |
|---|---:|---|
| Teoria e papers | 2-3h | Ler o material central, extrair fórmulas, premissas e limitações |
| Implementação guiada | 3-4h | Reproduzir algoritmos, notebooks ou pipelines |
| Lab/projeto | 2-3h | Transformar conteúdo em artefato executável |
| Revisão e avaliação | 1-2h | Flashcards, mistake log, perguntas abertas e análise de tradeoffs |

Para semanas avançadas, preserve tempo para profiling, avaliação e documentação. Um notebook que roda sem análise crítica não conta como domínio técnico.

---

## Workflow Semanal

1. Leia `weekly-roadmap.md` para saber o tema, complexidade e entregável da semana.
2. Estude a teoria planejada em `study-plan.md`.
3. Implemente o lab da semana quando ele for gerado com `Generate Week XX`.
4. Registre decisões, bugs e benchmarks no template de notas da semana.
5. Escreva pelo menos 10 flashcards técnicos.
6. Faça o assessment da semana sem consultar resposta.
7. Atualize o mistake log com erros de conceito, implementação e arquitetura.

---

## Definição de Sucesso

O curso está sendo executado com qualidade se, ao final de cada bloco, você consegue:

- reconstruir o raciocínio matemático essencial dos modelos;
- implementar uma versão mínima e uma versão usando biblioteca;
- explicar quando o modelo falha e por quê;
- desenhar arquitetura de dados/modelo/serving;
- medir qualidade com métricas adequadas;
- comparar custo, latência, explicabilidade, robustez e manutenção;
- transformar o aprendizado em um projeto acumulativo.

---

## Roadmap Macro

| Fase | Semanas | Tema | Resultado esperado |
|---|---:|---|---|
| 1 | 1-8 | Fundamentos, Python, estatística e EDA | Base técnica sólida e notebooks reprodutíveis |
| 2 | 9-20 | Regressão, árvores, ensembles e validação | Pipeline supervisionado completo com diagnóstico |
| 3 | 21-28 | Séries temporais, classificação e segmentação | Modelos comparados com validação adequada |
| 4 | 29-34 | AutoML, MLOps e projeto estruturado | Projeto de dados estruturados versionado e monitorado |
| 5 | 35-44 | Deep Learning, CNNs, RNNs e NLP clássico | Modelos neurais treinados, avaliados e interpretados |
| 6 | 45-54 | IA generativa, Transformers, GPT e prompts | Aplicações com LLMs, avaliação e análise de falhas |
| 7 | 55-60 | RAG, agentes, tool calling e operação | Sistema GenAI com avaliação, observabilidade e custos |
| 8 | 61-64 | Empreendedorismo técnico e capstone | Defesa técnica de solução aplicada |

---

## Milestones

| Marco | Semana | Evidência |
|---|---:|---|
| Base analítica pronta | 8 | Notebook de EDA com relatório técnico |
| Pipeline supervisionado robusto | 20 | Comparação entre regressão, árvores e boosting |
| Validação avançada dominada | 28 | Classificação, séries temporais e clustering com diagnóstico |
| Projeto estruturado entregue | 34 | Sistema ML com versionamento, métricas e monitoramento |
| Deep Learning aplicado | 44 | Modelo neural para imagem/texto com avaliação |
| GenAI aplicado | 54 | Aplicação com LLM, prompts avaliados e análise de falhas |
| Sistema RAG/agente operacional | 60 | Pipeline com retrieval, tools, avaliação e observabilidade |
| Capstone defendido | 64 | Relatório, benchmark, arquitetura e apresentação técnica |

---

## Fontes Centrais

- FIA Business School: <https://fia.com.br/pos-graduacao-ead/analytics-inteligencia-artificial-data-science/>
- Labdata FIA: <https://labdata.fia.com.br/curso/pos-analytics-e-inteligencia-artificial-data-science-ao-vivo/>
- PDF FIA/Labdata 2025: <https://fia.com.br/wp-content/uploads/2025/05/CP-LABDATA-Pos_Analytics-e-IA-Data-Science-2025.pdf>
- PDF FIA 2026: <https://fia.com.br/wp-content/uploads/2026/03/Pos-Graduacao-%E2%80%A8Analytics-e-Inteligencia-Artificial-%E2%80%93-Data-Science.pdf>

---

## Próximo Passo

Este é o Passo 1 da geração incremental. Para criar o material completo da primeira semana, solicite:

```txt
Generate Week 01
```
