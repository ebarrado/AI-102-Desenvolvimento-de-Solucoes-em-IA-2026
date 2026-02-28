# Configuração do Ambiente

Abra o VS Code e crie um novo projeto com o nome `chat-ai-app`.

Crie os arquivos conforme mostrado no exemplo a seguir:

# Estrutura do Projeto

```text
chat-ai-app/
├── app.py              # App Streamlit
├── .env               # Configurações
├── requirements.txt   # Dependências
└── README.md
```

1. Crie um arquivo `requirements.txt`
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

2. Crie um arquivo `.env`
```text
PROJECT_ENDPOINT=https://.....
MODEL_DEPLOYMENT=nome_modelo
```
* Configure com os valores do projeto criado no Microsoft Foundry

3. Crie um arquivo `app.py`. Encontre o passo a passo no arquivo, [clicando aqui](explicação_aplicacao_app_chat_ai_generativa.md)
4. Execute no VS Code
    * Abra o Terminal no VS Code
    * Crie um ambiente virtual: `python -m venv .venv`
    * Ative: `.venv\Scripts\activate` (Windows) ou source `.venv/bin/activate` (Linux/Mac)
    * Após a ativação você verá algum assim no prompt
    ```text
    (.venv)seguidodocaminhodapasta
    ```
    * Instale dependências: `pip install -r requirements.txt`
    * Execute: `streamlit run app.py`

Se apresentar algum erro de política instale primeiro: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

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