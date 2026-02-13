# Desenvolvendo um aplicativo de bate-papo com IA generativa

>Exercício adaptado - Microsoft Learn utilizando SDK Python do Microsoft Foundry

# Criar Grupo de Recursos - Portal Azure

1. Abra o [Portal do Azure](https://portal.azure.com/)
2. Crie um grupo de recurso com o nome: `rg-sobrenome-ano`

![alt text](/imagens/resource_group.png)

> Importante: o grupo de recurso deve estar na região `eastus2`, seguindo a regra da política `Allowed resource deployment regions`

* Para encontrar as regiões que poderá provisionar os recursos Azure, acesse: **Portal Azure - Políticas - Criação - Atribuições - Allowed resource deployment regions**.

![alt text](/imagens/politicas_regions_azure.png) 

![alt text](/imagens/allowed_resource.png)

> Veja na imagem que na referida conta só podemos provisionar recursos nas regiões `["eastus","brazilsouth","northcentralus","mexicocentral","eastus2"]`
> Para serviços de AI generativa iremos utilizar sempre `eastus2`

## Por que  `eastus2` para IA Generativa?

A região **eastus2** é recomendada porque:

### 1️⃣ Maior disponibilidade de modelos
Muitos modelos de IA generativa (como GPT-4o e modelos de raciocínio) são disponibilizados primeiro ou exclusivamente em regiões específicas.  
A eastus2 geralmente possui melhor suporte a modelos mais recentes.

### 2️⃣ Melhor compatibilidade com serviços de IA
Alguns recursos do Azure AI Foundry e Azure OpenAI possuem dependência regional.  
Utilizar eastus2 reduz a chance de erro de cota ou indisponibilidade de modelo.

### 3️⃣ Estabilidade e suporte global
A região eastus2 é uma das regiões principais (core regions) do Azure, com:
- Alta disponibilidade
- Melhor suporte a atualizações
- Maior capacidade de escalabilidade

### 4️⃣ Evita problemas de cota
Determinadas regiões podem não ter cota liberada para modelos específicos.  
Padronizar eastus2 reduz falhas durante a implantação.


# 🌍 Exemplos de regiões com suporte a IA generativa no Azure
Estas regiões geralmente suportam serviços de IA como Azure OpenAI ou Azure AI Foundry (incluindo modelos de linguagem e visão), sujeitas à disponibilidade de modelo e cota:

### 🌎 Américas

* East US 2 (forte suporte a modelos mais recentes)
* Central US
* South Central US
* West US 2
* West US 3
* Canada Central

### 🇧🇷 América do Sul

* Brazil South

### 🇪🇺 Europa

* France Central
* North Europe
* West Europe
* (Outras podem ter suporte parcial conforme serviço)

### 🌏 Ásia–Pacífico

* Australia East
* Japan East
* Korea Central
* Southeast Asia

### 🌍 Outros

* UK South

# Implantar um modelo - projeto Microsoft Foundry

1. Abra o [portal do Foundry](https://ai.azure.com)
2. Em explorar modelos e funcionalidade - Ir para o catálogo de modelos completo. Pesquise por `gpt-4o`

![alt text](/imagens/catalogo_modelos.png)

3. Após selecionar o modelo, clique no botão **Usar esse modelo**

![alt text](/imagens/gpt-4o.png)

4. Ao solicitado para selecionar um projeto, clique em criar projeto e insira um nome válido para o projeto
    * Exemplo: `chat-ai-exemplo-aula`

![alt text](/imagens/project_name.png)

> Para um projeto Foundry no Azure AI, escolha nomes descritivos, únicos e seguindo convenções Azure (letras minúsculas, hífens, sem espaços). Aqui vão sugestões baseadas no contexto do seu app de chat IA:



| Propósito        | Nome Sugerido      | Formato              |
| ---------------- | ------------------ | -------------------- |
| Chat IA Pessoal  | chat-ia-marilia    | Local + função       |
| App Web Demo     | chat-ai-foundry    | Produto + plataforma |
| Protótipo GPT-4o | gpt4o-chat-app     | Modelo + app         |
| Teste Foundry    | foundry-chat-br    | Plataforma + região  |
| IA Generativa    | ai-chat-marilia-sp | Função + localização |

>Importante: Veja se a região está em `East US 2`, caso não esteja altere. Observe o `Grupo de Recursos` e selecione o grupo de recurso criado na `Etapa 1`
* Após selecionar corretamente a assinatura ´Azure for Students, o `Grupo de Recursos`e a `Região East US2`, clique em **Criar e Continuar**

![alt text](/imagens/criando_projeto.png)


5. Na tela de implantação do modelo, o nome deve ser um indicador único que é definido para referênciar o modelo no SDK/Código

### Regras de Nomeação
* Minúsculas, hífens, 1-32 chars
* Sem espaços ou caracteres especiais
* Único no projeto
#### Exemplos:​
| Nome        | Quando Usar        | Vantagem            |
| ----------- | ------------------ | ------------------- |
| gpt-4o-chat | Apps de chat       | Descritivo          |
| chat-model  | Projetos genéricos | Simples             |
| gpt4o-prod  | Produção           | Identifica ambiente |
| modelo-chat | Português          | Linguagem local     |

* Utilizaremos para o exemplo de modelo: `modelo-chat-sobrenome`

Os tipos de implantação no Azure AI Foundry definem como seu modelo gpt-4o é hospedado, roteado e cobrado, otimizando para latência, cota e conformidade.
​

## Tipos de Implantação Disponíveis

| Tipo               | Explicação                                                                 | Quando Usar                             | Cobrança          |
| ------------------ | -------------------------------------------------------------------------- | --------------------------------------- | ----------------- |
| Global Standard    | Roteia globalmente para melhor data center disponível. Maior cota inicial. | ✅ Seu chat app - máxima disponibilidade | Por token         |
| DataZone Standard  | Limita processamento a zona de dados (US/EU). Conformidade GDPR.           | Apps regulados                          | Por token         |
| Standard           | Hospedagem regional básica. Latência previsível.                           | Testes locais                           | Por chamada       |
| ProvisionedManaged | Reserva capacidade fixa (PTUs). Alta taxa de transferência garantida.      | Produção pesada                         | Por PTU/hora      |
| GlobalBatch        | Processamento em lote assíncrono global.                                   | Análise massiva                         | Por token (batch) |
| DataZoneBatch      | Lote restrito a zona de dados.                                             | Batch regulado                          | Por token (batch) |

A cobrança `por token`significa pagar pelo uso real do modelo de IA, medido em pequenas unidades de texto chamanhdas tokens.

## Token

```text
1 token ≈ 4 caracteres (texto inglês)
"Olá mundo" = ~3 tokens
"Explique IA generativa" = ~6 tokens
```

#### Pagamento por Entrada + Saída

```text
Pergunta (input): 100 tokens
Resposta (output): 200 tokens  
TOTAL: 300 tokens × preço/1.000 tokens
```
### Exemplo Prático (gpt-4o Global Standard)

```text
Preço variável: R$0,01 por 1.000 tokens entrada
                     R$0,03 por 1.000 tokens saída

Chat típico:
- Sua pergunta: 50 tokens × R$0,01/1k = R$0,0005
- Resposta IA: 150 tokens × R$0,03/1k = R$0,0045  
**TOTAL: ~R$0,005 por conversa**
```
## Diferença vs Outros Modelos
| Modelo      | Cobrança     | Exemplo           |
| ----------- | ------------ | ----------------- |
| Por Token   | Uso real     | 10 chats = R$0,05 |
| PTU/Hora    | Reserva fixa | R$50/mês (fixo)   |
| Por Chamada | Cada request | R$0,10/chat       |

![alt text](/imagens/config_implantacao.png)

No nosso caso verifique se a região `East US 2`está selecionada, se não tiver clique em Personalizar e altere para `East US 2`

> Veja que aparece a opção `Limite de Taxa de Tokens de cota disponível para sua implantação`e pode chegar até 50K. Isso significa que são `50K por minuto`, que sua implantação gpt-4o pode processar 50.000 tokens a cada minuto antes de atingir o limite de cota.

### Representa:

```text
50K TPM = 50.000 tokens/minuto
1 chat típico = ~200 tokens (pergunta + resposta)
✅ 250 chats por minuto
✅ 15.000 chats por hora
✅ 360.000 chats por dia
```

Para um App Streamlit:

```
✅ Perfeito para:
- 100 usuários simultâneos
- 1.000 usuários/dia
- App público pequeno/médio
```
## Exemplo:

```text
["Qual", " é", " a", " capital", " do", " Brasil", "?"]
= 7 tokens
Resposta típica: "A capital do Brasil é Brasília."
✅ Output: 8 tokens

TOTAL por chat: 15 tokens

50.000 tokens/min ÷ 15 tokens/chat
= **3.333 chats por minuto**
✅ Ampla capacidade para seu app
```

6. Após clicar em `Impantar`, aguarde. 
> Se aparecer algum tipo de erro por causa de cota - altere o modelo, para outro modelo de `conclusão de chat` e tente novamente - pode ser a capacidade limitada para nossas contas de estudante.

* Veja a tela que abriu na guia Geral

![alt text](/imagens/modelo_chat_barrado.png)

# Criando App Web de Chat com IA Generativa

Nosso projeto utilizará:
* Streamlit
* Azure AI Projects SDK
* VS Code

1. Após implantar o modelo no Microsoft Foundry
2. Instale e configure o VS Code com extensões Python e Azure
3. Acesse Azure no VS Code e realize o Login com a conta da Assinatura Azure

    * Abra o Terminal
    * Digite: `az login`
    * Autentique as credenciais
    * Selecione a conta com a qual deseja iniciar sessão.
![alt text](/imagens/login_tenant.png)

![alt text](/imagens/conta_azure.png)

4. Liste as assinaturas da sua conta com o comando: `az account list --output table`
5. Copie a Subscription ID ativa na sua conta e adicione ao comando: 
    * `az account set --subscription "nome-ou-id"`

6. Adicione a conta a extensão do Azure no VS Code

![alt text](/imagens/conta_azure_vs.png)

# Estrutura do Projeto

```text
chat-ai-app/
├── app.py              # App Streamlit
├── .env               # Configurações
├── requirements.txt   # Dependências
└── README.md
```
1. Crie um novo projeto no VS Code como o nome: `chat-ai-app`
2. Crie um arquivo `requirements.txt`
    * Adicione as versões:

```text
streamlit==1.38.0
azure-identity==1.19.0
azure-ai-projects==1.0.0b1
openai==1.51.2
python-dotenv==1.0.1
```

| Pacote          | Versão        | Função no Seu App       |
| -------------- | ------------- | ---------------- |
| streamlit==1.38.0          | Interface web | Cria o chat UI com st.chat_input(), st.chat_message() |
| azure-identity==1.19.0     | Autenticação  | DefaultAzureCredential() para login Azure AD          |
| azure-ai-projects==1.0.0b1 | Core IA       | AIProjectClient(endpoint=...) conecta ao Foundry      |
| openai==1.51.2             | Inferência    | client.chat.completions.create(model="gpt-4o")        |
| python-dotenv==1.0.1       | Config        | Carrega PROJECT_ENDPOINT e MODEL_DEPLOYMENT do .env   |

3. Crie um arquivo `.env`
```text
PROJECT_ENDPOINT=https://seu-projeto.projects.ai.azure.com
MODEL_DEPLOYMENT=gpt-4o
```
* Configure com os valores do projeto criado no Microsoft Foundry

4. Crie um arquivo `app.py`
5. Execute no VS Code
    * Abra o Terminal no VS Code
    * Crie um ambiente virtual: `python -m venv .venv`
    * Ative: `.venv\Scripts\activate` (Windows) ou source `.venv/bin/activate` (Linux/Mac)
    * Instale dependências: `pip install -r requirements.txt`
    * Execute: `streamlit run app.py`

# Referência

* [Create a generative AI chat app](https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/02a-AI-foundry-sdk.html)
* [Regiões com suporte a idioma](https://learn.microsoft.com/pt-br/azure/ai-services/language-service/concepts/regional-support?utm_source=chatgpt.com)
* [Azure OpenAI in Microsoft Foundry Models quotas and limits] (https://learn.microsoft.com/en-us/azure/ai-foundry/openai/quotas-limits?view=foundry-classic&tabs=REST)