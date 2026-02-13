import streamlit as st

nome = st.text_input("Digite seu nome:")
st.write("Olá,", nome)

idade = st.slider("Qual sua idade?", 0, 100, 18)
st.write("Idade:", idade)


linguagem = st.selectbox(
    "Escolha uma linguagem:",
    ["Python", "Java", "C#"]
)
st.write("Você escolheu:", linguagem)

arquivo = st.file_uploader("Envie um arquivo CSV")


if st.button("Clique aqui"):
    st.success("Botão clicado!")


with st.chat_message("user"):
    st.write("Olá!")

with st.chat_message("assistant"):
    st.write("Oi! Como posso ajudar?")


col1, col2 = st.columns(2)

with col1:
    st.write("Coluna 1")

with col2:
    st.write("Coluna 2")
