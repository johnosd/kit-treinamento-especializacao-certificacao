# Week 01 — Readings

Priorize leitura ativa: para cada item, escreva 5 bullets de contribuição, 3 limitações e 2 perguntas técnicas.

---

## Leituras Obrigatórias

### 1. scikit-learn — Model selection and evaluation

- **Fonte:** <https://scikit-learn.org/stable/model_selection>
- **Tipo:** documentação oficial.
- **Por que ler:** introduz avaliação, validação cruzada, métricas e seleção de modelos.
- **Foco:** entenda que avaliação é parte do desenho do problema, não etapa final decorativa.
- **Relação com a semana:** a especificação do problema precisa declarar métrica, split e baseline antes do modelo.

### 2. pandas — Getting started

- **Fonte:** <https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html>
- **Tipo:** documentação oficial.
- **Por que ler:** pandas será a base operacional para dados tabulares nas primeiras semanas.
- **Foco:** DataFrame, Series, leitura de dados, seleção, filtros e operações básicas.
- **Relação com a semana:** você ainda não faz EDA completa, mas precisa saber qual ferramenta sustentará o plano de dados.

### 3. PyTorch Tutorials — Learn the Basics

- **Fonte:** <https://docs.pytorch.org/tutorials/beginner/basics/>
- **Tipo:** documentação oficial.
- **Por que ler:** PyTorch será usado nas semanas de Deep Learning e Transformers.
- **Foco:** datasets, tensors, autograd e fluxo de treinamento.
- **Relação com a semana:** reconheça o que diferencia modelagem clássica de treinamento neural.

### 4. TensorFlow Basics

- **Fonte:** <https://www.tensorflow.org/guide/basics>
- **Tipo:** documentação oficial.
- **Por que ler:** TensorFlow/Keras aparece na matriz oficial do curso.
- **Foco:** tensores, operações, modelos e treinamento básico.
- **Relação com a semana:** comparar ecossistemas antes de escolher stack por hábito.

---

## Papers e Artigos Técnicos Fundamentais

### 1. Hidden Technical Debt in Machine Learning Systems

- **Fonte:** <https://papers.nips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html>
- **Tipo:** paper.
- **Contribuição:** mostra que sistemas de ML acumulam dívida técnica em dados, dependências, configuração, feedback loops e glue code.
- **Limitações:** não é um manual de implementação; é um mapa de riscos sistêmicos.
- **Relação com a semana:** force seu problem spec a considerar operação desde o início.

### 2. Datasheets for Datasets

- **Fonte:** <https://arxiv.org/abs/1803.09010>
- **Tipo:** paper.
- **Contribuição:** propõe documentação sistemática para datasets.
- **Limitações:** documentação não remove viés por si só.
- **Relação com a semana:** ajuda a formular perguntas sobre origem, composição, coleta, uso e riscos dos dados.

### 3. Model Cards for Model Reporting

- **Fonte:** <https://arxiv.org/abs/1810.03993>
- **Tipo:** paper.
- **Contribuição:** estrutura comunicação sobre uso pretendido, métricas, limitações e avaliação por subgrupos.
- **Limitações:** depende de honestidade e cobertura de avaliação.
- **Relação com a semana:** antecipa o tipo de documentação exigida nos projetos finais.

### 4. A Few Useful Things to Know about Machine Learning

- **Fonte:** <https://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf>
- **Tipo:** artigo técnico acadêmico.
- **Contribuição:** resume princípios práticos: generalização, features, overfitting, dados e avaliação.
- **Limitações:** é panorâmico e anterior à era GenAI moderna.
- **Relação com a semana:** ajuda a calibrar expectativa: modelo é só uma parte do sistema.

---

## Leituras de Apoio

### Python — venv

- **Fonte:** <https://docs.python.org/3/library/venv.html>
- **Uso:** criar ambientes isolados para experimentos.

### Jupyter Documentation

- **Fonte:** <https://docs.jupyter.org/>
- **Uso:** entender notebooks como ferramenta de exploração, não como substituto de engenharia.

### Google Machine Learning Crash Course — Framing

- **Fonte:** <https://developers.google.com/machine-learning/crash-course/framing>
- **Uso:** reforçar formulação de problemas de ML e tipos de saída.

---

## Perguntas de Leitura

1. Qual parte da avaliação precisa ser decidida antes da coleta de dados?
2. Que tipo de dívida técnica aparece antes mesmo do primeiro modelo?
3. Quais perguntas de Datasheets for Datasets você incorporaria ao problem spec?
4. Quando um notebook é evidência técnica suficiente e quando vira risco operacional?
5. Por que deep learning não deve ser a escolha padrão para dados tabulares?
