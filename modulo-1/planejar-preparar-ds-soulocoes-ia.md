# Introdução - Desenvolvimento de Soluções em Inteligência Artificial

A Inteligência Artificial deixou de ser um conceito restrito à pesquisa acadêmica e passou a fazer parte do dia a dia das empresas, dos sistemas de informação e das decisões estratégicas. Hoje, soluções baseadas em IA são utilizadas para automatizar atendimentos, analisar grandes volumes de dados, interpretar imagens e documentos, apoiar diagnósticos e gerar conteúdos de forma inteligente.

Nesse cenário, o papel do desenvolvedor evoluiu. Não basta apenas programar: é necessário planejar, integrar e orquestrar diferentes componentes de IA, combinando modelos de aprendizado de máquina, serviços cognitivos, engenharia de prompts e código personalizado, sempre com atenção à ética, à segurança e à escalabilidade das soluções.

# O que é IA (Inteligência Artificial)

A Inteligência Artificial (IA) é um conjunto de tecnologias que permite a sistemas interpretar dados, identificar padrões e gerar respostas ou previsões de forma automatizada.

Resumindo, Inteligência Artificial é um conjunto de software e técnicas que permitem aos sistemas apresenta comportamentos semelhantes aos humanos, tais como:

* Percepção Visual
* Análise de Texto
* Conversa
* Tomada de decisão

### Recursos comuns de IA para desenvolvedores

|Capacidade | Descrição|
| ---| ----|
|IA Geradora | capacidade de gerar respostas originais a partir de indicações em linguagem natural.|
|Agentes| Aplicativos de IA generativos que podem responder à entrada do usuário ou avaliar situações de forma autônoma e tomar as medidas apropriadas.|
| Visão Computacional| Capacidade de aceitar, interpretar e processar a entrada visual de imagens, vídeos e fluxos de câmeras ao vivo|
|Fala| Capacidade de reconhecer e sintetizar fala.|
|Processamento de linguagem natural| Capacidade de processar a linguagem natural em forma escrita ou falada, analisá-la, identificar pontos-chaves e gerar resumos ou categorizações.|
|Extração de Informações| Capacidade de usar visual computacional, a fla e o processamento de linguagem natural para extrair informações de documentos, formulários, imagens, gravações e outros tipos de conteúdo.|
|Apoio à decisão| Capacidade de usar dados históriucos e correlações aprendidads para fazer previsões que dão suporte à tomada de decisões de negócios.


## Modelos de Linguagem usados em soluções de IA Generativas

* LLMs (grandes modelos de linguagem)
  - Eles são capazes de realizar uma ampla variedade de tarefas de linguagem com alta precisão e fluidez, mas exigem mais recursos computacionais para treinamento e execução. Exemplos incluem modelos como o GPT-3, LaMDA e modelos maiores do Gemini.

* SLMs (otimizados para cenários
  -  Eles são frequentemente otimizados para tarefas específicas ou para serem executados em dispositivos com recursos limitados (como dispositivos móveis ou em "edge computing"). Embora possam não ter a mesma capacidade geral dos LLMs, eles podem ser muito eficazes para seus casos de uso direcionados e são mais econômicos para implantar em escala.

### Serviços

|Serviço| Descrição |
|--|--|
|OpenAI do Azure| OpenAI no Foundry Models fornece acesso aos modelos de IA generativos do OpenAI, inclui família GPT e modelos de geração de imagem DALL-E|
|Visão de IA do Azure| Oferece conjunto de modelos e APIS que pode ser usada para implementar funcionalidades comuns de visão computacional em um aplicativo.|
|Fala de IA do Azure| oferece APIs que você pode usar para implementar transformações de conversão de texto em fala e conversão de fala em texto|
|Linguagem de IA do Azure| oferece modelos e APIs que você usa para analisar texto em linguagem natural e executar tarefas comuns com extração de entidades, análise de sentimento e sumarização|
|Segurança de conteúdo do Azure AI Foundry| Azure AI Foundry Content Safety fornece aos desenvolvedores acesso a algoritmos avançados para processar imagens e texto e sinalizar conetúdo pontencialmente ofensivo, arriscado ou indesejavel|
|Tradutor de IA do Azure| usa modelos de linguagem avançados para traduzir texto entre um grande número de idiomas|
|Detecção Facial da IA do Azure| Pode detectar, analisar e reconhecer rostos humanos. |
|Visão Personalizada de IA do Azure| Permite treinar e usar modelos personalizados de visão computacional para classificação e detecção de objetos|
|IA do Azure para Informações de Documentos| usar modelos predefinidos ou personalizados para extrair campos de documentos complexos como faturas, recibos e formulários|
|Compreensão de Conteúdo de IA do Azure| oferece funcionalidade de análise de conteúdo multimodal que permitem criar modelos para extrair dados de formulários e documentos, imagens, vídeos e fluxos de áudio|
|Pesquisa de IA do Azure| usa pipeline de habilidades de IA baseadas em outros Serviços de IA do Azure e Código personalizado para extrair informações de conteúdos e criar índice pesquisável|

## Recurso de serviço único ou multisserviço

![alt text](/imagens/ai_servicos_unicos_servicos_multi.jpg)

## Disponibilidade

Acesse [tabela de disponibilidade do produto por região](https://azure.microsoft.com/pt-br/explore/global-infrastructure/products-by-region/table).

## Projetos do Microsoft Foundry

1. Projetos Foundry (Projetos de Fundação)

Esses projetos são associados a um recurso do Microsoft Foundry dentro de uma assinatura do Azure. Eles oferecem suporte a:

* Modelos do Microsoft Foundry (incluindo modelos OpenAI)

* Serviço de Agentes do Microsoft Foundry

* Ferramentas de fundação para IA

* Avaliação e desenvolvimento responsável de IA

Os projetos Foundry são ideais para a maioria dos cenários de desenvolvimento de aplicativos e agentes de chat com IA generativa, pois centralizam recursos essenciais com menor complexidade administrativa. Todo o gerenciamento pode ser feito diretamente pelo portal do Microsoft Foundry, facilitando a conexão de recursos e a implantação de modelos e agentes.

2. Projetos Baseados em Hub

Os projetos baseados em hub são associados a um recurso do Hub de IA do Azure e incluem uma estrutura mais avançada. Além do Microsoft Foundry, eles oferecem:

* Computação gerenciada

* Suporte ao desenvolvimento com Prompt Flow

* Recursos de armazenamento do Azure

* Integração com Azure Key Vault para armazenamento seguro de dados

Esses projetos são indicados para cenários avançados, como ajuste fino de modelos e desenvolvimento de fluxos complexos de IA. Eles podem ser utilizados tanto no portal do Microsoft Foundry quanto no Azure Machine Learning, facilitando o trabalho colaborativo entre cientistas de dados, especialistas em machine learning e desenvolvedores de IA.



