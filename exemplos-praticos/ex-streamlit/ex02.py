import streamlit as st

with st.form("user_input_form"):
    name = st.text_input("Nome")
    email = st.text_input("Email")
    submit_button = st.form_submit_button("Enviar")
    
if submit_button:
  st.write(f"Nome: {name}")
  st.write(f"Email: {email}")