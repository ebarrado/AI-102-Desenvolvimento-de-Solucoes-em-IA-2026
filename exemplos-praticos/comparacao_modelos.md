# Escolha e Implemente um Modelo de Linguagem

O **catálogo de modelos do Microsoft Foundry** é um repositório central que permite explorar, comparar e implantar modelos para cenários de IA generativa.

Neste exercício, você irá:
- Explorar modelos no portal Foundry
- Comparar métricas de desempenho
- Criar um projeto
- Implantar e testar modelos
- Refletir sobre custo e qualidade

⏱ Tempo estimado: 25 minutos  
⚠ Observação: Algumas funcionalidades podem estar em versão prévia.

---

# 1. Explorar Modelos

## Acessar o Portal
1. Abra: https://ai.azure.com  
2. Faça login com sua conta Azure.
3. Feche painéis de ajuda ou início rápido.
4. Navegue até a página inicial do Foundry.

---

## Analisar o modelo GPT-4o

1. Na seção **Explorar modelos e recursos**, pesquise: `gpt-4o`
2. Selecione o modelo.
3. Leia as informações na aba **Detalhes**.
4. Acesse a aba **Benchmarks** para visualizar métricas de desempenho.
5. Retorne ao catálogo usando a seta ←.

---

## Analisar o modelo Phi-4-reasoning

1. Pesquise: `Phi-4-reasoning`
2. Abra os detalhes do modelo.
3. Analise os benchmarks e métricas disponíveis.

---

# 2. Comparar Modelos

1. Volte ao catálogo.
2. Selecione **Comparar modelos**.
3. Clique em 🗑 para limpar modelos pré-selecionados.
4. Adicione:
   - `gpt-4o`
   - `Phi-4-reasoning`

O gráfico exibirá:

- Índice de Qualidade
- Custo
- Precisão

Passe o mouse sobre os pontos para visualizar os valores.

📌 Observação: O modelo **Phi-4-reasoning** pode apresentar melhor desempenho geral com menor custo, dependendo da métrica analisada.

---

# 3. Criar um Projeto no Foundry

Para usar um modelo, é necessário criar um projeto.

1. Na página do modelo **gpt-4o**, clique em **Usar este modelo**.
2. Insira um nome para o projeto.
3. Expanda **Opções avançadas** e configure:

- Recurso Foundry: Nome válido
- Assinatura: Sua assinatura Azure
- Grupo de Recursos: Criar ou selecionar existente
- Região: Uma região recomendada

⚠ Algumas regiões possuem limites de cota.

4. Clique em **Criar**.
5. Implante o modelo com:
   - Tipo: Global Padrão
   - Limite TPM: 50.000 (ou máximo disponível)

📌 Reduzir TPM evita consumo excessivo de cota.

---

# 4. Testar o Modelo GPT-4o

No ambiente de chat:

### Configuração
System Prompt:
```shell

### Pergunta 1
```

---

# 5. Implantar o Modelo Phi-4-reasoning

1. Vá em **Meus ativos → Modelos + endpoints**
2. Clique em **Implantar modelo base**
3. Pesquise `Phi-4-reasoning`
4. Aceite a licença
5. Configure:
   - Nome da implantação
   - Tipo: Global padrão
   - Configurações padrão

Aguarde a implantação.

---

# 6. Testar o Modelo Phi-4

1. Vá em **Playgrounds**
2. Selecione o modelo Phi-4-reasoning
3. Insira como primeira mensagem:


Resposta correta: **40**

Alterne entre os modelos e compare:

- Clareza da resposta
- Precisão
- Raciocínio
- Custo estimado

---

# 8. Reflexão Final

Ao escolher um modelo, considere:

- Adequação à tarefa
- Precisão
- Custo por token
- Capacidade de raciocínio
- Escalabilidade

O catálogo e as ferramentas de comparação do Foundry ajudam a selecionar candidatos ideais, mas o teste prático no playground é essencial.

---

# 9. Limpeza de Recursos

Para evitar custos:

1. Acesse o Portal do Azure.
2. Abra o grupo de recursos utilizado.
3. Clique em **Excluir grupo de recursos**.
4. Confirme a exclusão.

---

✅ Conclusão:  
A escolha de um modelo ideal envolve equilibrar **qualidade, custo e adequação ao problema**, testando diferentes opções antes da implantação definitiva.
