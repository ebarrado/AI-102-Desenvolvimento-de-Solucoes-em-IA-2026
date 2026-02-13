# Modelos de Base

Os modelos de base, como os da família GPT, são modelos avançados de linguagem capazes de entender e gerar texto em linguagem natural. 

| Capacidade de IA                     | Descrição                                           | Exemplo de Uso |
|-------------------------------------|-----------------------------------------------------|----------------|
| Conversão de fala em texto (STT)     | Transforma áudio ou fala em texto escrito           | Gerar legendas automáticas para vídeos |
| Conversão de texto em fala (TTS)     | Converte texto escrito em áudio falado              | Leitura em voz alta de textos ou acessibilidade |
| Tradução automática                 | Traduz texto entre diferentes idiomas               | Traduzir texto do inglês para o japonês |
| Classificação de textos             | Categoriza textos com base em seu conteúdo          | Classificar e-mails como spam ou não spam |
| Extração de entidades               | Identifica e extrai informações importantes do texto| Extrair palavras-chave ou nomes de um documento |
| Resumo de texto                     | Gera uma versão curta e objetiva de textos longos   | Criar resumo de um documento de várias páginas |
| Respostas a perguntas               | Fornece respostas diretas com base em conhecimento  | Responder “Qual é a capital da França?” |
| Raciocínio                          | Analisa informações para resolver problemas         | Resolver um problema matemático |


## Escolher entre modelos de linguagem grandes e pequenos

No catálogo de modoles do Microsof Foundry é possível escolher entre diversos modelos de linguagem. É importante entender a necessidade para cada problema de forma a responder a pergunta: `À IA pode resolver meu caso de uso?`

Dessa forma é preciso descobrir, filtrar e implantar um modelo.

Existem 3 catálogos diferentes:

* **Hugging Face:** modelos open-source
* **GitHub:** modelos via GitHub Markeplace e GitHub Copilot
* **Microsoft Foundry:** catálogo com ferrametnas robustas para implantação

As opções variam entre LLMs(Modelos de Linguagem Grande) e SLMs(Modelos de Linguagem Pequena)

| Tipo de Modelo | Exemplos | Características | Indicação de Uso |
|---------------|----------|----------------|------------------|
| LLMs (Large Language Models) | GPT-4, Mistral Large, Llama 3 70B, Llama 405B, Command R+ | Modelos avançados com grande capacidade de parâmetros, alto poder de raciocínio, geração de conteúdo complexo e ampla compreensão de contexto | Tarefas que exigem raciocínio profundo, análise complexa, geração de textos elaborados, assistentes avançados e aplicações corporativas robustas |
| SLMs (Small Language Models) | Phi-3, Mistral OSS, Llama 3 8B | Modelos menores, mais leves, eficientes e econômicos, com bom desempenho em tarefas comuns de NLP | Execução em dispositivos com menor poder computacional, aplicações de borda (edge), cenários onde custo e velocidade são mais importantes que alta complexidade

## Modelos e Finalidade


| Modelo | Tipo | O que faz |
|--------|------|-----------|
| GPT-4 | Modelo de conclusão de chat (LLM) | Gera respostas coerentes e contextualizadas em texto para conversas e tarefas gerais. |
| Mistral Large | Modelo de conclusão de chat (LLM) | Produz respostas avançadas em linguagem natural com boa compreensão de contexto. |
| DeepSeek-R1 | Modelo de raciocínio | Resolve tarefas complexas que exigem lógica avançada, matemática, código e estratégia. |
| o1 | Modelo de raciocínio | Indicado para problemas que demandam análise profunda e tomada de decisão estruturada. |
| GPT-4o | Modelo multimodal | Processa e gera texto, imagens e outros tipos de dados no mesmo modelo. |
| Phi-3 Vision | Modelo multimodal | Analisa imagens e gera descrições ou respostas baseadas em conteúdo visual. |
| DALL·E 3 | Modelo de geração de imagem | Cria imagens realistas a partir de descrições em texto. |
| Stability AI | Modelo de geração de imagem | Gera artes, ilustrações e imagens digitais com base em prompts textuais. |
| Ada | Modelo de embeddings | Converte texto em vetores numéricos para busca semântica e recomendação (RAG). |
| Cohere Embeddings | Modelo de embeddings | Representa textos numericamente para melhorar relevância em buscas e sistemas inteligentes. |
| Core42 JAIS | Modelo regional (LLM em árabe) | Especializado no idioma árabe, ideal para aplicações voltadas a usuários de língua árabe. |
| Nixtla TimeGEN-1 | Modelo específico de domínio (Séries Temporais) | Especializado em previsão de séries temporais, como previsões financeiras e demanda. |

## Como selecionar o melhor modelo para Implantar e Integrar

| Critério | O que avaliar | Exemplo de Caso de Uso | Melhor Escolha |
|-----------|---------------|------------------------|----------------|
| Tipo de tarefa | Texto simples, multimodal, previsão, geração de imagem | Chatbot para atendimento ao aluno | Modelo de conclusão de chat (GPT-4, Mistral Large) |
| Tipo de tarefa | Análise de imagem + texto | Aplicativo que corrige atividades enviadas por foto | Modelo multimodal (GPT-4o, Phi-3 Vision) |
| Tipo de tarefa | Previsão de dados | Sistema que prevê evasão escolar ou demanda de matrículas | Modelo específico de domínio (TimeGEN-1) |
| Precisão | Necessidade de alta especialização | Assistente jurídico ou médico | Modelo ajustado (fine-tuned) |
| Precisão | Uso geral | FAQ institucional da escola | Modelo base (GPT-4 com engenharia de prompt) |
| Abertura | Necessidade de personalização | Empresa que deseja treinar modelo com seus próprios dados internos | Modelo open-source (Llama, Mistral OSS) |
| Implantação | Ambiente com restrição de internet | Sistema interno rodando em servidor local | Modelo implantado localmente (open-source) |
| Implantação | Escalabilidade sem gerenciar servidor | Aplicativo web com alto volume de usuários | Endpoint serverless no Azure/OpenAI |
| Implantação | Controle total da infraestrutura | Aplicação corporativa com requisitos de compliance | Infraestrutura gerenciada própria (VMs ou Kubernetes) |

# Exemplos práticos de decisão

## Caso 1 - Chatbot Educacional
* Tarefa: Texto
* Precisão: Média
* Implantação: Nuvem
    * ✅Modelo base GPT-4 em endpoint serveless

## Caso 2 – Previsão de vendas ou demanda
* Tarefa: Série temporal
* Precisão: Alta
* Implantação: Nuvem corporativa
    * ✅ Nixtla TimeGEN-1

## Caso 3 – Assistente especializado (jurídico/médico)
* Tarefa: Texto técnico
* Precisão: Muito alta
* Necessidade de ajuste fino
    * ✅ Modelo ajustado com fine-tuning

## Caso 4 – Aplicativo mobile offline
* Tarefa: NLP simples
* Implantação local
* Baixo custo
    * ✅ SLM como Phi-3 ou Llama 8B

# Filtrar modelos de desempenho

| Parâmetro de Comparação | Descrição |
|--------------------------|------------|
| Exatidão (Accuracy) | Compara o texto gerado pelo modelo com a resposta correta de acordo com o conjunto de dados. O resultado é 1 se o texto gerado corresponder exatamente à resposta e 0 caso contrário. |
| Coerência (Coherence) | Mede se a saída do modelo flui de maneira suave, é lida naturalmente e se assemelha à linguagem humana. |
| Fluência (Fluency) | Avalia o quão bem o texto gerado adere às regras gramaticais, estruturas sintáticas e uso apropriado do vocabulário, resultando em respostas linguisticamente corretas e naturais. |
| Aterramento (Groundedness) | Mede o alinhamento entre as respostas geradas pelo modelo e os dados de entrada fornecidos. |
| Similaridade de GPT (GPT Similarity)  | Quantifica a similaridade semântica entre uma frase de referência (ground truth) e a sentença gerada pelo modelo de IA. |
| Índice de Qualidade (Quality Index) | Pontuação agregada comparativa entre 0 e 1, em que modelos com melhor desempenho obtêm pontuação mais alta. |
| Custo (Cost) | Refere-se ao custo de uso do modelo com base no preço por token. Permite comparar qualidade versus investimento, ajudando na tomada de decisão. |

> Quando avalia o desempenho de um modelo, é comum começar com avaliações manuais

Após criar um protótipo com o modelo escolhido, é necessário prepará-lo para cargas de trabalho reais, considerando escalabilidade, custo e desempenho.

Para isso, é importante avaliar:

* **Implantação do modelo**: definir onde ele será hospedado (nuvem, local, serverless) buscando equilíbrio entre desempenho e custo.

* **Monitoramento e otimização**: acompanhar métricas de qualidade, uso e latência, realizando ajustes quando necessário.

* **Gerenciamento de prompts**: estruturar e melhorar prompts continuamente para aumentar precisão e relevância das respostas.

* **Ciclo de vida do modelo (GenAIOps)**: gerenciar versões, atualizações, dados e código de forma contínua e organizada.