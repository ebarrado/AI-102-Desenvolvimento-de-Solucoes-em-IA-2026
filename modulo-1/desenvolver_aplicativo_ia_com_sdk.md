# O que é SDK do Microsoft Foundry?

Microsoft Foundry fornece uma API REST que você pode usar para trabalhar com projetos do AI Foundry.

Pacote principal para projetos é a biblioteca de Projetos de IA do Azure

# Biblioteca Cliente do Azure AI Projects para Python

A Biblioteca Cliente do Azure AI Projects para Python é uma biblioteca em preview do Azure AI Foundry SDK que permite acessar e gerenciar recursos em projetos do Azure AI Foundry de forma programática.

## Instalação

* Instale via pip com o comando `pip install azure-ai-projects`. Para suporte assíncrono, adicione `pip install aiohttp`.
​
## Criação do Cliente

Use AIProjectClient.from_connection_string com credenciais como DefaultAzureCredential e uma string de conexão do projeto:

```text
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
import os

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"]
)
```

A biblioteca de clientes de Projetos de IA, faz parte do SDK do Azure AI Foundry. Use para:

* Crie e execute agentes usando métodos na .agentspropriedade do cliente.
* Obtenha um cliente AzureOpenAI usando o .get_openai_client()método client.
* Enumere os modelos de IA implantados em seu projeto Foundry usando métodos na .deploymentspropriedade do cliente.
* Enumere os recursos do Azure conectados em seu projeto Foundry usando métodos na .connectionspropriedade do cliente.
* Faça o upload de documentos e crie conjuntos de dados para referenciá-los usando métodos na .datasetspropriedade do cliente.
* Crie e enumere índices de pesquisa usando métodos na .indexespropriedade do cliente.

## Como usar o SDK para se conectar a um projeto

Cada projeto tem um **ponto de extremidade** exclusivo.
Para encontrar acesse **visão geral** do projeto no portal **Microsoft Foundry**.

![alt text](/imagens/projeto_ai_foundry.png)

## O que o projeto fornece?

Vários pontos de extremidade e chaves

* Um ponto de extremidade para o projeto em si; que pode ser usado para acessar conexões de projeto, agentes e modelos no recurso Microsoft Foundry.
* Um endpoint para as APIs do Serviço Azure OpenAI no recurso Microsoft Foundry do projeto.
* Um ponto de extremidade para APIs do Foundry Tools (como Visão do Azure e Linguagem do Azure) no recurso do Microsoft Foundry.

| Endpoint      | Propósito     | Formato Exemplo learn.microsoft+1       |
| ------------- | --------- | ----- |
| Projeto Geral | Acessa conexões, agentes, modelos e serviços no Foundry (via AIProjectClient). | https://<projeto>.projects.ai.azure.com |
| Azure OpenAI  | APIs completas para chat, assistentes, batch e modelos OpenAI.                 | https://<recurso>.openai.azure.com      |
| Foundry Tools | APIs de visão, linguagem e ferramentas cognitivas do Azure.                    | https://<recurso>.services.ai.azure.com |

