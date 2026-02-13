# Introdução ao Streamlit para Aplicação com IA

Streamlit é um framework Python para criar aplicações web interativas de forma simples e rápida, sem precisar escrever HTML, CSS ou JavaScript.

Ele transforma scripts Python em aplicações web automaticamente.

* Interface rápida
* Entrada de texto
* Exibição dinâmica
* Controles como sliders
* Resposta em tempo real

## Instalação
```bash
python -m venv .venv  # Criar um ambiente virtual
.venv\Scripts\activate   # Ativar o ambiente virtual (Linux/Mac) ou
source env/bin/activate
```
```bash
pip install streamlit
```

## Executar

```bash
streamlit run app.py
```

* Abre automaticamente no navegador:

```text
http://localhost:8501
```

## Estrutura básica de um app


```python

import streamlit as st

# --- Título principal da página --- #
st.title('Minha primeira aplicação Streamlit!')

# --- Cabeçalho --- #
st.header('Bem-vindo ao mundo Streamlit!')

# --- Subcabeçalho --- #
st.subheader('Vamos explorar essa ferramenta incrível!')

# --- Texto genérico --- #
st.write('Este é um texto simples usando o st.write()')

# --- Texto formatado com Markdown --- #
st.markdown('''
Este é um exemplo de **Markdown** no Streamlit.
Podemos usar **negrito**, *itálico* e até mesmo **listas**:
* Item 1
* Item 2
''')

# --- Texto literal --- #
st.text('Este é um texto puro, sem formatação.')
```
# Exemplo Criando um Formulário


```python
import streamlit as st

with st.form("user_input_form"):
    name = st.text_input("Nome")
    email = st.text_input("Email")
    submit_button = st.form_submit_button("Enviar")
    
if submit_button:
  st.write(f"Nome: {name}")
  st.write(f"Email: {email}")
```

![alt text](/imagens/form_streamlit.png)

# Widgets
São elementos interativos que você pode adicionar às suas aplicações para permitir que os usuários interajam com os dados ou modelos que você está exibindo. Esses widgets incluem coisas como inputs, botões e até mesmo a sua webcam. Da mesma forma que vimos anteriormente, widgets são criados como uma simples declaração de variável

```python
import streamlit as st


x = st.slider('x')  # isto é um widget
st.write(x, 'ao quadrado é', x * x)
```

### Widgets de Entrada de Dados
#### Texto

* st.text_input() → Campo de texto simples

* st.text_area() → Campo de texto multilinha

* st.chat_input() → Entrada estilo chat (ótimo para apps com IA)

```python
import streamlit as st

nome = st.text_input("Digite seu nome:")
st.write("Olá,", nome)
```
![alt text](/imagens/text_input.png)

#### Números

* st.number_input() → Campo numérico

* st.slider() → Barra deslizante

* st.select_slider() → Slider com opções personalizadas

```python
idade = st.slider("Qual sua idade?", 0, 100, 18)
st.write("Idade:", idade)
```

#### Seleção

* st.checkbox() → Caixa de seleção

* st.radio() → Botões de opção

* st.selectbox() → Lista suspensa

* st.multiselect() → Múltiplas escolhas

```python
linguagem = st.selectbox(
    "Escolha uma linguagem:",
    ["Python", "Java", "C#"]
)
st.write("Você escolheu:", linguagem)
```

#### Data e Hora

* st.date_input() → Data

* st.time_input() → Hora

#### Upload de Arquivos

* st.file_uploader()

```python
arquivo = st.file_uploader("Envie um arquivo CSV")
```
#### Widgets de Ação

* st.button() → Botão

* st.form() → Formulários

* st.form_submit_button() → Botão dentro de formulário
```python

```

#### Widgets para Apps com IA (Muito Usados Hoje)

Se você está trabalhando com LLMs ou Azure OpenAI, esses são importantes:

* st.chat_message()

* st.chat_input()

* st.spinner() → Indicador de carregamento

```python
with st.chat_message("user"):
    st.write("Olá!")

with st.chat_message("assistant"):
    st.write("Oi! Como posso ajudar?")
```

#### Layout e Organização

* st.sidebar → Menu lateral

* st.columns() → Colunas

* st.tabs() → Abas

* st.expander() → Seção expansível

* st.container() → Container agrupador

```python
col1, col2 = st.columns(2)

with col1:
    st.write("Coluna 1")

with col2:
    st.write("Coluna 2")
```
# Exemplo Página Simples com Streamlit

```python
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
```
![alt text](/imagens/pagina_simples.png)

# Exemplo Sistema de Cadastro de Alunos

```python
import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Sistema de Cadastro de Alunos",
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
```
![alt text](/imagens/sistema_cadastro_aluno.png)

![alt text](/imagens/dashboard.png)


# Referências

* [Basic concepts of Streamlit](https://docs.streamlit.io/get-started/fundamentals/main-concepts)
* [Como usar Streamlit com Python: um guia passo a passo](https://www.datahackers.news/p/como-usar-streamlit-com-python-um-guia-passo-a-passo)
