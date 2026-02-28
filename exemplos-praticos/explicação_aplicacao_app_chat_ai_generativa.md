# Passo a Passo - Aplicativo de bate-papo com IA generativa

![alt text](/imagens/app_chat_ia_generativa.png)

Antes de começar a programar acesse o arquivo [configuração de ambiente](configuracao_ambiente.md).

## Configuração Arquivo `app.py`

```python
import streamlit as st
import os
from dotenv import load_dotenv
from openai import AzureOpenAI
```
* `import streamlit as st`: Importa o Streamlit, framework usado para criar aplicações web em Python.
O as st cria um apelido para facilitar o uso.

* `import os`: Permite acessar variáveis do sistema operacional (ex: variáveis de ambiente).
* `from dotenv import load_dotenv`: Importa a função que carrega variáveis do arquivo .env.

* `from openai import AzureOpenAI`:Importa a classe que permite conectar ao Azure OpenAI.

## Carregando as Variáveis

Carrega as variáveis do arquivo `.env`para dentro do sistema

```python
load_python
```
O arquivo `.env`está configurado da seguinte forma:

```bash
AZURE_OPENAI_ENDPOINT=https://...
AZURE_OPENAI_KEY=xxxxx
MODEL_DEPLOYMENT=modelo-chat-barrado
```
## Configuração do Ambiente

```python
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
MODEL_DEPLOYMENT = os.getenv("MODEL_DEPLOYMENT", "modelo-chat-barrado")
API_VERSION = "2024-12-01-preview"
```

* `os.getenv()`: pega valores do .env

* Se `MODEL_DEPLOYMENT`:  não existir, usa "modelo-chat-barrado" como padrão.

* Define a versão da API que será usada.

## Função que inicia o Cliente Azure OpenAI

```Python
@st.cache_resource
def get_openai_client():
```
* `@st.cache_resource`:
Diz ao Streamlit para criar o cliente apenas uma vez e reutilizar depois.
Isso melhora desempenho.

```python
if not AZURE_OPENAI_KEY:
    st.error("Chave de API não encontrada")
    return None
```

* ✔ Verifica se a chave existe
* ✔ Se não existir, mostra erro

```python
cliente = AzureOpenAI(
    azure_endpoint= AZURE_OPENAI_ENDPOINT,
    api_key= AZURE_OPENAI_KEY,
    api_version= API_VERSION
)
```
* ✔ Cria o objeto cliente
* ✔ Conecta com o Azure OpenAI

## Configuração da Página

```python
st.set_page_config(
    page_title="Chat IA Generativa - Azure AI Foundry",
    page_icon="🤖",
    layout="wide"    
)
```
* Título da aba do navegador
* Ícone
* Layout em tela larga

## Inicialização da Memória da Conversa

```python
if "messages" not in st.session_state:
```

### `session_state`

É a memória da aplicação durante a sessão do usuário.

```python
st.session_state.messages = [
    {
        "role": "system", 
        "content": "Você é um professor..."
    }
]
```
* ✔ Define o comportamento do assistente
* ✔ Essa mensagem do tipo "system" orienta o modelo

## Sidebar (Painel Lateral)

```python
with st.sidebar:
```
* Cria o painel lateral.

## Controle de Temperatura

```python
temperatura = st.slider(...)
```
Controla criatividade:

* 0.0 → respostas mais objetivas
* 1.0 → mais criativas

## Controle de Max Tokens

Define tamanho máximo da resposta.

```python
max_tokens = st.slider(...)
```

## Controle Top-P

```python
top_p = st.slider(...)
```
Controla diversidade das palavras usadas.

## Botão Limpar Conversa

```python
if st.button("🚨Limpar Conversa"):
```
* ✔ Testa se o cliente foi criado
* ✔ Mostra status da conexão

# Exibição das Mensagens

```python
for message in st.session_state.messages:
```
Percorre todas as mensagens salvas.

```python
Percorre todas as mensagens salvas.
```

Renderiza:

* Mensagem do usuário
* Mensagem do assistente

## Entrada do Usuário

```python
if prompt := st.chat_input("💬 Digite sua mensagem..."):
```

```text
:= é o operador WALRUS
Ele atribui e verifica ao mesmo tempo.
```

## Enviando para API

```python
response = client.chat.completions.create(
```
Parâmetros importantes:

* model
* messages
* temperature
* max_tokens
* top_p
* stream=True:  ativa streaming

## Streaming da Resposta

```python
for chunk in response:
```
O modelo envia a resposta em partes.

```python
full_response += content
message_placeholder.markdown(full_response + "▌")
```
* ✔ Junta os pedaços
* ✔ Mostra digitando em tempo real

## Tratamento de Erros

```python
except Exception as e:
```
Trata erros comuns:

* 401 → erro de autenticação

* 404 → modelo não encontrado

* 429 → limite excedido

Connection → erro de conexão

Isso melhora a experiência do usuário.

# Rodapé

```python
col1, col2, col3 = st.columns(3)
```
Divide a tela em 3 colunas.

Exibe:

* Tipo de autenticação
* Nome do modelo
* Limite de tokens

## Código Final

```python
import streamlit as st
import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

#Configuração do Ambiente
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
MODEL_DEPLOYMENT = os.getenv("MODEL_DEPLOYMENT", "modelo-chat-barrado")
API_VERSION = "2024-12-01-preview"


#INICIAR O CLIENTE DO OPENAI
@st.cache_resource
def get_openai_client():
    """
    Cria e retorna um cliente Azure OpenAI
    """
    try:
        if not AZURE_OPENAI_KEY:
            st.error("Chave de API não encontrada")
            return None
        cliente = AzureOpenAI(
            azure_endpoint= AZURE_OPENAI_ENDPOINT,
            api_key= AZURE_OPENAI_KEY,
            api_version= API_VERSION
        )
        return cliente
    except Exception as e:
        st.error(f"Erro na autenticação: {str(e)}")
        
st.set_page_config(
    page_title="Chat IA Generativa - Azure AI Foundry",
    page_icon="🤖",
    layout="wide"    
)

st.title("🤖 Chat IA Generativa - Azure AI Foundry")
st.caption(f"{MODEL_DEPLOYMENT} via Azure OpenAI")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system", "content":
                "Você é um professor de tecnologia, especializado em treinamentos Microsoft para certificações de nível fundamentos, associado e especialista. "
                "Explique de forma clara, objetiva e didática. "
                "Use linguagem simples e exemplos práticos. "
                "Responda em Português do Brasil. "
        }
    ]

with st.sidebar:
    st.header("Configurações")
    
    #Controles
    temperatura = st.slider(
        "Temperatura",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1,
        help="Controla a criatividade das respostas"
    )
    max_tokens = st.slider(
        "Máximo de tokens",
        min_value=100,
        max_value=4000,
        value=1000,
        step=100,
        help="Tamanho máximo da resposta"
    )
    
    top_p = st.slider(
        "Top P",
        min_value=0.1,
        max_value=1.0,
        value=0.95,
        step=0.05
    )
    if st.button("🚨Limpar Conversa", use_container_width=True):
        st.session_state.messages = [
            {"role":"system","content":"Você é um assistente útil e responde em português do Brasil"}
        ]   
        st.rerun()
    # Informações do sistema
    st.header("ℹ️ Informações da Implantação")
    
    # Verifica status da conexão
    client = get_openai_client()
    status = "✅ Conectado" if client else "❌ Desconectado"
    
    st.info(f"""
    **Modelo:** {MODEL_DEPLOYMENT}
    **Endpoint:** {AZURE_OPENAI_ENDPOINT.split('//')[1].split('.')[0] if AZURE_OPENAI_ENDPOINT else 'Não configurado'}
    **Status:** {status}
    **Versão API:** {API_VERSION}
    **Limite:** 50K tokens/min
    """)
    
    st.divider()

    
#Area Principal
chat_container = st.container()

with chat_container:
    for message in st.session_state.messages:
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

# Input do usuário
if prompt := st.chat_input("💬 Digite sua mensagem..."):
    # Adiciona mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Gera resposta
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        with st.spinner("🤔 Pensando..."):
            try:
                client = get_openai_client()
                
                if client is None:
                    st.error("❌ Cliente não inicializado. Verifique suas credenciais.")
                    st.stop()
                
                # Prepara mensagens
                messages_for_api = st.session_state.messages.copy()
                
                # Faz a chamada à API com STREAMING
                response = client.chat.completions.create(
                    model=MODEL_DEPLOYMENT,
                    messages=messages_for_api,
                    temperature=temperatura,
                    max_tokens=max_tokens,
                    top_p=top_p,
                    stream=True
                )
                
                # Processa streaming
                full_response = ""
                for chunk in response:
                    if chunk.choices and chunk.choices[0].delta.content:
                        content = chunk.choices[0].delta.content
                        full_response += content
                        message_placeholder.markdown(full_response + "▌")
                
                message_placeholder.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
                
            except Exception as e:
                error_message = str(e)
                st.error(f"❌ Erro na geração da resposta")
                
                # Tratamento específico de erros
                if "401" in error_message:
                    st.warning("🔑 **Erro de autenticação**: Verifique se sua chave de API está correta no arquivo .env")
                elif "404" in error_message:
                    st.warning(f"🔍 **Modelo não encontrado**: Verifique se o nome '{MODEL_DEPLOYMENT}' está correto")
                elif "429" in error_message:
                    st.warning("⏳ **Limite de taxa excedido**: Aguarde um momento (limite: 50K tokens/min)")
                elif "Connection" in error_message:
                    st.warning(f"🌐 **Erro de conexão**: Verifique se o endpoint '{AZURE_OPENAI_ENDPOINT}' está acessível")
                else:
                    st.info(f"Detalhes: {error_message[:200]}...")

# Rodapé
st.divider()
col1, col2, col3 = st.columns(3)
with col1:
    st.caption(f"🔒 Autenticação: **Chave de API**")
with col2:
    st.caption(f"🤖 Modelo: **{MODEL_DEPLOYMENT}**")
with col3:
    st.caption(f"📊 Limite: **50K tokens/min**")
```

Para executar utilize o comando:

```bash
streamlit run app.py
```

Não esqueça que o ambiente virtual deve estar ativo e ao executar deve-se estar na pasta do arquivo `app.py`

Caso não tenha realizado a configuração do ambiente veja os passos para realizar:

```text
1ª - Configuração do Ambiente Virtual
	* python -m venv .venv 

2º - instalação da Politica
	* Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

3º - Ativição do Ambiente Virtual
	* .venv\Scripts\Activate.ps1 

4º - Instalação do arquivo requerements.txt
	*  pip install -r requirements.txt

5º - Executar o arquivo principal
	* streamlit run app.py
```