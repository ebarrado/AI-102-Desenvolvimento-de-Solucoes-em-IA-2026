# Crie um aplicativo cliente para conversar com o modelo

1. No portal do Foundry, visualzie a página **Visão Geral** do seu projeto
2. Em **Endpoints e chaves**, certifique que a biblioteca Foundry esteja selecionada e visualize o endpoint do projeto Foundry
3. Abra o VS Code
4. Clique em **Terminal - New Terminal**
5. Acesse um diretório para clonar a pasta do GitHub
6. Insira os seguinte comando para clonar o repositório do GitHub

```bash
rm -rf mslearn-ai-foundry  # Remove se existir
git clone https://github.com/microsoftlearning/mslearn-ai-studio mslearn-ai-foundry
```
6. Aguarde
7. No menu **File-Open Folder**, selecione a pasta clonada

![alt text](/imagens/repositorio_git.png)

8. Acesse a pasta que contém os arquivos de código do aplicativo de bate-papo e visualize-os:`mslearn-ai-foundry/labfiles/chat-app/python`

> A pasta pode ser acessada via terminal usando os comandos:

```bash
cd labfiles/chat-app/python
ls -la #lista conteúdo da pasta
```

## Instalar as bibliotecas

```bash
#acesse a pasta do projeto
pip install -r requirements.txt
pip install -r requirements.txt azure-identity azure-ai-projects openai

# se precisar atualizar 
python.exe -m pip install --upgrade pip
# execute novamente - pip install -r requirements.txt azure-identity azure-ai-projects openai
```

9. No Terminal, digite o seguinte comando no diretorio raiz, para criar e ativar `venv`

```bash
python -m venv labenv
```
> O VS Code detecta que um novo ambiente virtual foi criado e pergunta se você quer usá-lo como interpretador padrão do projeto.


![alt text](/imagens/notificacao.png)

* Clique em `Yes` - Isso fará com que:
    * O VS Code use o Python do labenv
    * As bibliotecas instaladas fiquem isoladas nesse projeto
    * O terminal já abra com o ambiente correto

## Ativar

```bash
labenv\Scripts\activate
# No Linux/Mac: source labenv/bin/activate
```

## Configuração do arquivo `.env`

1. Abra `.env` no VS Code (Ctrl+P, digite .env). Substitua:

* `your_project_endpoint` pelo endpoint do Foundry (Visão geral > Endpoints e chaves)
* `your_model_deployment` por gpt-4o (ou nome da implantação).


```txt
PROJECT_ENDPOINT=your_project_endpoint
MODEL_DEPLOYMENT=your_model_deployment 
```

## Escrevendo o código para conectar ao projeto e conversar com o modelo

1. Abra o arquivo `chat-app.py`
2. Adicione o seguinte código para referênciar aos namespaces nas bibliotecas que você instalou

```python

# Add references
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from openai import AzureOpenAI

```

3. Na função principal, comentário `Obter Configurações` (Inicialize the project client)

```python
# Initialize the project client
project_client = AIProjectClient(            
         credential=DefaultAzureCredential(
             exclude_environment_credential=True,
             exclude_managed_identity_credential=True
         ),
         endpoint=project_endpoint,
     )
```
4. Localize o comentário "Obter um cliente de bate-papo", adicione:

```python

​# Get a chat client
openai_client = project_client.get_openai_client(api_version="2024-10-21")
```
5. Adicione ao comentário "Initialize prompt with system message":

```python

# Initialize prompt with system message
prompt = [
        {"role": "system", "content": 
        "Você é um assistente educacional claro, didático e objetivo. "
        "Responda em português do Brasil. "
        "Explique conceitos de forma simples e use exemplos quando possível."
}
     ]
```


. Na seção do loop, encontre o comentário " Obter uma conclusão do chat" e adicione

```python
# Get a chat completion
prompt.append({"role": "user", "content": input_text})
response = openai_client.chat.completions.create(
         model=model_deployment,
         messages=prompt)
completion = response.choices[0].message.content
print(completion)
prompt.append({"role": "assistant", "content": completion})
```

7. Salve

## Iniciar sessão no Azure e executar a Aplicação

1. No terminal execute o comando
```bash
az login
```
* Ative a credencial Azure

2. Execute o aplicativo com o comando:

```bash
python chat-app.py
```

# Controlar temperatura (mais controle de respostas)

Para melhorar a estabilidade adicionando parâmetros: `temperature`, `max_tokens=800`.

* Substitua as linhas:

```python
response = openai_client.chat.completions.create(
    model=model_deployment,
    messages=prompt)
```

* Por:

```python
response = openai_client.chat.completions.create(
    model=model_deployment,
    messages=prompt,
    temperature=0.3,   # mais controlado
    max_tokens=800
)
```
* temperature=0.3 → respostas mais técnicas e estáveis

* max_tokens=800 → evita respostas gigantes

* top_p=0.95 → mantém diversidade controlada

## Recomendado

| Objetivo           | temperature |
| ------------------ | ----------- |
| Respostas técnicas | 0.2 – 0.4   |
| Chat equilibrado   | 0.5 – 0.7   |
| Criatividade alta  | 0.8 – 1.0   |


# Exemplo

```python
prompt = [
            {"role": "system", "content": 
            "Você é uma professora técnica de tecnologia. "
            "Explique de forma clara, objetiva e didática. "
            "Use linguagem simples e exemplos práticos. "
            "Responda em português do Brasil."
}
        ]
```

* Execute: python chat-app.py

* Pergunta : `Crie uma analogia para explicar o que é Machine Learning.`

* Resposta:
```text
Digite uma mensagem (ou digite 'sair' para encerrar): Crie uma analogia para explicar o que é Machine Learning.
Claro! Aqui vai uma analogia prática para entender o que é **Machine Learning**: Imagine que você está ensinando um amigo a identificar frutas só olhando para elas. Esse amigo é como uma "máquina" que precisa aprender observando exemplos. 1. **Treinamento (Aprendendo com exemplos):** Primeiro, você mostra várias frutas para o seu amigo. Você aponta para uma maçã e diz: "Isso é uma maçã". Depois, você mostra uma banana e diz: "Isso é uma banana". O mesmo acontece com laranjas, uvas e outras frutas. Ou seja, você está fornecendo **dados de entrada (imagens das frutas)** e o **rótulo correto (o nome de cada fruta)**. 2. **Reconhecimento (Fase de aprendizado):** Com o tempo, seu amigo começa a perceber padrões. Ele aprende, por exemplo, que maçãs geralmente têm uma forma redonda e são vermelhas ou verdes, enquanto bananas são alongadas e amarelas. Ele **aprendeu com os exemplos**. 3. **Testando o aprendizado:** Agora você mostra uma fruta nova para o seu amigo e pergunta: "O que é isso?". É aqui que você descobre se ele aprendeu mesmo! Ele olha e diz: "Parece uma maçã porque é redonda e vermelha". Se ele acertar, significa que ele **generalizou bem o aprendizado**. Se errar, talvez precise de mais exemplos para corrigir. --- Agora vamos conectar isso com **Machine Learning**: - O **amigo** representa um **modelo de machine learning**. - As **frutas mostradas** são os **dados de treinamento**. - O processo de identificar padrões é como o **algoritmo aprendendo** a partir dos dados. - Testar o que ele aprendeu equivale a usar o modelo para fazer **previsões** em novos dados. ### Exemplo real: Um aplicativo de fotos, como o Google Fotos, usa Machine Learning desse jeito para identificar fotos de "cachorros" ou "pessoas". Ele "aprendeu" o que é um cachorro olhando milhões de imagens de treinamento (dados) e agora consegue identificar cachorros nas suas fotos, mesmo que nunca tenha visto aquele cão específico antes. Espero que essa analogia tenha ajudado! 😊
```

### Resposta usando temperature e max_tokens e top_p

```text
Digite uma mensagem (ou digite 'sair' para encerrar): Crie uma analogia para explicar o que é Machine Learning.
Claro! Vamos imaginar que você está ensinando um cachorro a buscar uma bolinha. Essa situação pode ser uma ótima analogia para entender o que é **Machine Learning** (Aprendizado de Máquina). ### O cachorro é como uma máquina ou um computador. Ele não sabe, por conta própria, como buscar a bolinha. Mas, com o tempo e prática, ele pode aprender. ### O treinamento é o processo de aprendizado. Você começa jogando a bolinha e, toda vez que o cachorro traz a bolinha de volta, você dá um petisco (recompensa). Se ele não traz a bolinha, você não dá nada. Com o tempo, ele entende que, para ganhar o petisco, precisa buscar a bolinha. ### Os dados são as tentativas. Cada vez que você joga a bolinha e o cachorro tenta buscar, isso é como um "dado" que ele usa para aprender. Quanto mais vezes ele tenta, mais ele entende o que precisa fazer. ### O modelo treinado é o cachorro que aprendeu. Depois de várias tentativas, o cachorro já sabe o que fazer: ele busca a bolinha automaticamente, sem precisar de mais petiscos. Ele aprendeu o "padrão" do que você quer. --- Agora, trazendo para o mundo da tecnologia: - O **cachorro** é o computador ou sistema. - O **treinamento** é o processo de ensinar o sistema usando dados. - Os **dados** são as informações que você fornece para o sistema aprender (como fotos, números, textos, etc.). - O **modelo treinado** é o sistema que aprendeu a realizar uma tarefa, como reconhecer rostos em fotos ou prever o clima. Assim como o cachorro precisa de prática para aprender, o computador precisa de muitos dados para entender padrões e realizar tarefas de forma inteligente. 😊
```

* Com `temperature = 0.3`

Temperatura baixa =
✔️ Mais previsível
✔️ Mais conservador
✔️ Menos criatividade

> A temperatura não escolhe a resposta.
Ela controla o nível de variação probabilística.

## 🔴 Ultra controlado

```python
temperature=0.1
max_tokens=200
```

* Resposta curta
* Pouca criatividade
* Mais técnica

## 🟣 Criativo

```python
temperature=0.9
max_tokens=400
```
* Metáforas diferentes
* Linguagem mais criativa
* Resposta menos previsível

# Top_p

`top_p`controla o nível de diversidade das palavras escolhidas pelo modelo.
Imagine que o modelo está escolhendo a próxima palavra. Ele calcula várias possibilidades com probabilidade:

| Palavra possível | Probabilidade |
| ---------------- | ------------- |
| cachorro         | 40%           |
| animal           | 30%           |
| pet              | 15%           |
| lobo             | 10%           |
| dragão           | 5%            |

* Se o `top_p = 0.5` 

Ele só considera as palavras que somam até 50% de probabilidade

* No caso:
    * Cachorro (40%)
    * Animal (30%)

Já passou de 50%, então ele escolhe apenas entre essas duas.

### Resultado: mais previsível.

*  Se top_p = 0.95

    * Ele considera quase todas as opções.

### Resultado: mais variedade.

| Valor | Comportamento            |
| ----- | ------------------------ |
| 0.1   | Muito conservador        |
| 0.5   | Moderadamente controlado |
| 0.9   | Criativo                 |
| 1.0   | Totalmente livre         |

## Diferença entre `temperature`e `top_p`

| Parâmetro   | O que controla               |
| ----------- | ---------------------------- |
| temperature | O quanto ele "arrisca"       |
| top_p       | Quantas opções ele considera |

> Temperature controla a ousadia.

> top_p controla o tamanho do universo de escolhas.

> Arquitetura de IA é decidir o nível de risco criativo adequado ao negócio.

# Fluxo real

1. O Código envia requisição HTTPS
2. Azure autentica via token
3. O Foundry localiza o modelo implantado
4. O modelo processa o prompt
5. Aplica temperatura e top_p
6. Retorna os tokens gerados
7. SDK transforma em objeto Python
8. Você extrai: `response.choices[0].message.content`

> Sempre que for executar o projeto acesse a pasta e ative o ambiente virtual `labenv\Scripts\activate`