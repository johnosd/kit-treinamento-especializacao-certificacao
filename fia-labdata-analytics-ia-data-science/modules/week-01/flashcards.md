# Week 01 — Flashcards

Formato compatível com estudo ativo. Para Anki, use frente como pergunta e verso como resposta.

---

### Q: O que diferencia Analytics de Machine Learning?
**A:** Analytics é uso sistemático de dados para descrever, diagnosticar, prever ou prescrever decisões. Machine Learning é uma classe de métodos que aprende padrões a partir de dados para predizer, classificar, ranquear ou gerar saídas.

### Q: Qual é a unidade mínima de um bom projeto de Data Science?
**A:** Uma decisão mensurável, não um notebook ou modelo.

### Q: O que é unidade de predição?
**A:** A entidade sobre a qual uma previsão é feita, como cliente, transação, pedido, documento ou sessão.

### Q: O que é horizonte de predição?
**A:** A janela temporal em que o target será observado, como churn nos próximos 30 dias.

### Q: Por que baseline é obrigatório?
**A:** Porque sem baseline não há comparação honesta para saber se o modelo avançado adiciona valor.

### Q: Dê três exemplos de baseline.
**A:** Regra de negócio, média histórica, modelo linear simples, previsão naive ou busca lexical.

### Q: O que é data leakage?
**A:** Uso de informação que não estaria disponível no momento real da decisão ou predição.

### Q: Qual é um exemplo clássico de leakage em churn?
**A:** Usar `cancellation_reason` ou dados coletados após o cancelamento para prever cancelamento futuro.

### Q: Por que acurácia pode ser ruim em classes desbalanceadas?
**A:** Porque um modelo pode acertar a classe majoritária quase sempre e ainda ser inútil para detectar a classe rara.

### Q: O que mede AUC?
**A:** Mede capacidade de ranking entre positivos e negativos em diferentes thresholds, mas não define sozinha a política de decisão.

### Q: O que é métrica técnica?
**A:** Métrica que avalia comportamento do modelo, como AUC, RMSE, recall@k ou calibration error.

### Q: O que é métrica de negócio?
**A:** Métrica que avalia impacto da decisão, como receita retida, custo reduzido, margem, tempo economizado ou satisfação.

### Q: Correlação implica causalidade?
**A:** Não. Correlação mede associação; causalidade exige desenho experimental ou hipóteses causais mais fortes.

### Q: O que é target?
**A:** Variável que o modelo tenta prever ou explicar.

### Q: O que é label?
**A:** Valor observado usado como resposta supervisionada para treinar ou avaliar o modelo.

### Q: O que é proxy metric?
**A:** Métrica indireta usada como aproximação de valor real. Pode ser perigosa quando desalinhada da decisão.

### Q: O que é go/no-go criterion?
**A:** Critério objetivo para avançar, pausar ou abandonar o projeto.

### Q: Por que definir custo de erro?
**A:** Porque falsos positivos e falsos negativos raramente têm o mesmo impacto operacional ou financeiro.

### Q: O que é model selection?
**A:** Processo de escolher modelo, hiperparâmetros e estratégia com base em avaliação adequada.

### Q: O que é validação offline?
**A:** Avaliação em dados históricos separados do treino para estimar generalização antes de produção.

### Q: Qual risco de holdout aleatório em séries temporais?
**A:** Misturar passado e futuro, produzindo avaliação otimista por leakage temporal.

### Q: Quando Deep Learning é proporcional?
**A:** Quando há dados e problema com representação complexa, como imagem, texto, áudio, sequência ou multimodalidade.

### Q: Quando GenAI é proporcional?
**A:** Quando a tarefa exige geração, síntese, interação linguística, raciocínio contextual ou uso flexível de documentos/ferramentas.

### Q: Quando GenAI é desproporcional?
**A:** Quando uma consulta SQL, regra determinística, dashboard ou modelo simples resolve com menor custo, risco e latência.

### Q: O que é failure mode?
**A:** Forma específica pela qual um sistema pode falhar, como leakage, drift, viés, latência excessiva ou métrica desalinhada.

### Q: O que é data drift?
**A:** Mudança na distribuição dos dados de entrada ao longo do tempo.

### Q: O que é concept drift?
**A:** Mudança na relação entre entradas e target ao longo do tempo.

### Q: Por que documentar datasets?
**A:** Para registrar origem, composição, coleta, limitações, vieses e usos apropriados dos dados.

### Q: O que é model card?
**A:** Documento que descreve uso pretendido, métricas, limitações, avaliação e riscos de um modelo.

### Q: Qual é o entregável central da Semana 01?
**A:** Uma especificação de problema orientado a dados com decisão, dados, métrica, baseline, riscos e go/no-go.
