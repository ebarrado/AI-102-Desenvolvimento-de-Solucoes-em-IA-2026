import streamlit as st
import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# Carrega configurações
load_dotenv()

# Configurações - AGORA CORRETAS para seu ambiente
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
MODEL_DEPLOYMENT = os.getenv("MODEL_DEPLOYMENT", "modelo-chat-barrado")
API_VERSION = "2024-12-01-preview"  # Versão da sua imagem

# Inicializa cliente do OpenAI com CHAVE DE  API
@st.cache_resource
def get_openai_client():
    """
    Cria e retorna um cliente Azure OpenAI autenticado com chave de API
    """
    try:
        if not AZURE_OPENAI_KEY:
            st.error("❌ Chave de API não encontrada. Verifique seu arquivo .env")
            return None
            
        client = AzureOpenAI(
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            api_key=AZURE_OPENAI_KEY,
            api_version=API_VERSION
        )
        return client
    except Exception as e:
        st.error(f"Erro na autenticação: {str(e)}")
        return None

# Interface Streamlit
st.set_page_config(
    page_title="Chat IA Generativa - Azure AI Foundry",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Chat IA Generativa - Azure AI Foundry")
st.caption(f"Powered by **{MODEL_DEPLOYMENT}** via Azure OpenAI")

# Inicialização do histórico
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": 
            "Você é uma professora técnica de tecnologia. "
            "Explique de forma clara, objetiva e didática. "
            "Use linguagem simples e exemplos práticos. "
            "Responda em português do Brasil."}
    ]

# Sidebar para configurações e informações
with st.sidebar:
    st.header("⚙️ Configurações")
    
    # Controles de temperatura
    temperature = st.slider(
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
    
    if st.button("🗑️ Limpar Conversa", use_container_width=True):
        st.session_state.messages = [
            {"role": "system", "content": "Você é um assistente útil e responde em português do Brasil."}
        ]
        st.rerun()
    
    st.divider()
    
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
    
    # Dicas
    with st.expander("📘 Dicas de uso"):
        st.markdown("""
        - **Temperatura baixa** (0.0-0.3): Respostas mais precisas e consistentes
        - **Temperatura média** (0.4-0.7): Bom equilíbrio entre criatividade e precisão
        - **Temperatura alta** (0.8-1.0): Respostas mais criativas e variadas
        """)

# Área principal do chat
chat_container = st.container()

with chat_container:
    # Exibe histórico (pulando mensagens do sistema)
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
                    temperature=temperature,
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