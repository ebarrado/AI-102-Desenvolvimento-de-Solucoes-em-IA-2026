import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Minha Primeira Página",
    page_icon="🚀",
    layout="centered"
)

# Título
st.title("🚀 Minha Primeira Página com Streamlit")

st.markdown("Este é um exemplo simples usando apenas componentes do Streamlit.")

st.divider()

# Entrada de texto
nome = st.text_input("Digite seu nome:")

# Slider
idade = st.slider("Escolha sua idade:", 0, 100, 18)

# Seleção
curso = st.selectbox(
    "Escolha um curso:",
    ["Python", "Java", "Cloud", "Flutter"]
)

# Botão
if st.button("Enviar"):
    st.success(f"""
    ✅ Dados enviados com sucesso!

    👤 Nome: {nome}  
    🎂 Idade: {idade}  
    📚 Curso: {curso}
    """)

st.divider()

# Sidebar
st.sidebar.title("Menu Lateral")
st.sidebar.write("Exemplo de sidebar no Streamlit.")
st.sidebar.checkbox("Ativar modo especial")
