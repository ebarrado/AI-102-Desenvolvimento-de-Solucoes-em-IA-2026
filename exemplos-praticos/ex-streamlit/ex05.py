import streamlit as st
import pandas as pd
import datetime

# Configuração da página
st.set_page_config(
    page_title="Sistema de Cadastro",
    page_icon="📊",
    layout="wide"
)

# Título principal
st.title("📊 Sistema de Cadastro de Alunos")
st.markdown("---")

# Sidebar
st.sidebar.header("Menu")
pagina = st.sidebar.radio("Navegação", ["Cadastro", "Dashboard"])

# ==========================
# PÁGINA DE CADASTRO
# ==========================
if pagina == "Cadastro":

    st.header("📝 Cadastro")

    with st.form("form_cadastro"):
        nome = st.text_input("Nome")
        idade = st.number_input("Idade", min_value=0, max_value=100)
        curso = st.selectbox("Curso", ["Python", "Java", "Cloud", "Flutter"])
        data = st.date_input("Data de matrícula", datetime.date.today())

        submitted = st.form_submit_button("Salvar")

        if submitted:
            st.success(f"Aluno {nome} cadastrado com sucesso!")

# ==========================
# PÁGINA DE DASHBOARD
# ==========================
elif pagina == "Dashboard":

    st.header("📈 Dashboard")

    # Dados fictícios
    dados = pd.DataFrame({
        "Curso": ["Python", "Java", "Cloud", "Flutter"],
        "Alunos": [30, 20, 25, 15]
    })

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total de Alunos", sum(dados["Alunos"]))

    with col2:
        st.metric("Total de Cursos", len(dados))

    st.bar_chart(dados.set_index("Curso"))
