# 🤖 Automação de Testes com Python, Selenium e Behave

Este projeto demonstra uma automação de testes com **Python**, **Selenium WebDriver** e **Behave (BDD)** para acessar o site do [Instituto Joga Junto](https://www.jogajuntoinstituto.org/).  
O objetivo é ensinar os alunos a construir e executar testes automatizados com base em comportamento (Behavior Driven Development).

---

## 🚀 Objetivo

- Criar um **teste automatizado** que simula o comportamento de um usuário acessando o site pelo navegador.
- Ensinar o uso de **cenários BDD com Behave**.
- Mostrar como gerenciar ambientes e dependências com **venv** e **requirements.txt**.
- Demonstrar **integração prática entre código Python e testes comportamentais**.

---

## 🧱 Estrutura do Projeto

Aula 9 - Automacao/
│
├── features/
│ ├── buscar_site.feature # Cenário BDD em linguagem Gherkin
│ └── steps/
│ └── steps_buscar_site.py # Implementação dos passos do cenário
│
├── test_automacao.py # Script de teste simples (sem BDD)
├── requirements.txt # Lista de bibliotecas necessárias
├── README.md # Documento explicativo do projeto
├── .gitignore # Arquivo para ignorar itens desnecessários no GitHub
└── .vscode/
└── settings.json # Configurações locais do VSCode (opcional)

---
---

## ⚙️ Instalação e Configuração

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/dionebraga/Automacao-2025.git
cd Automacao-2025/Aula\ 9\ -\ Automacao

2️⃣ Crie o ambiente virtual
python -m venv venv

3️⃣ Ative o ambiente virtual

Windows (PowerShell):

.\venv\Scripts\activate

4️⃣ Instale as dependências
pip install -r requirements.txt

▶️ Execução dos Testes
🔹 Rodar o teste direto (sem BDD)
python test_automacao.py


Esse comando abrirá o navegador Microsoft Edge, realizará a busca no Google e exibirá no terminal:

✅ Primeiro resultado encontrado: Instituto Joga Junto
🌐 Página aberta com sucesso!

🔹 Rodar com BDD (Behave)
behave


O Behave executa o arquivo .feature e segue o comportamento descrito no formato Gherkin.

🧩 Exemplo de Cenário — features/buscar_site.feature
Funcionalidade: Acessar o site do Instituto Joga Junto pelo Google

  Cenário: Usuário realiza a busca e acessa o site com sucesso
    Dado que o navegador Microsoft Edge está aberto
    Quando eu pesquisar por "Instituto Joga Junto" no Google
    Então devo ver o site do Instituto aberto com sucesso

🧠 Exemplo de Step — features/steps/steps_buscar_site.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
import time
from behave import given, when, then

@given('que o navegador Microsoft Edge está aberto')
def step_open_browser(context):
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    context.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
    context.driver.get("https://www.google.com")

@when('eu pesquisar por "Instituto Joga Junto" no Google')
def step_search_google(context):
    search_box = context.driver.find_element(By.NAME, "q")
    search_box.send_keys("Instituto Joga Junto")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

@then('devo ver o site do Instituto aberto com sucesso')
def step_validate_site(context):
    primeiro_resultado = context.driver.find_element(By.CSS_SELECTOR, "h3")
    print(f"✅ Primeiro resultado encontrado: {primeiro_resultado.text}")
    primeiro_resultado.click()
    time.sleep(4)
    print("🌐 Página aberta com sucesso!")
    context.driver.quit()

💻 Tecnologias Utilizadas

Tecnologia	Finalidade
Python	Linguagem base do projeto
Selenium WebDriver	Controle do navegador (Edge)
Behave	Framework BDD para testes automatizados
WebDriver Manager	Gerenciamento automático de drivers
Microsoft Edge	Navegador usado nos testes
VSCode	Ambiente de desenvolvimento recomendado

🧾 Arquivo .gitignore

Salve este conteúdo em um arquivo chamado .gitignore na raiz do projeto:

# Ambiente virtual
venv/
.venv/

# Cache do Python
__pycache__/
*.pyc

# Configurações do VSCode
.vscode/

# Logs
*.log

# Arquivos temporários
*.tmp
*.bak

# Dados de execução
*.sqlite3

# Arquivos do sistema
.DS_Store
Thumbs.db

📬 Créditos

Projeto criado e mantido por
Dione Braga Ferreira
Facilitadora – Ilhabela Tech / Instituto Joga Junto
📧 dionebraga.work@gmail.com

📍 Ilhabela/SP

💡 Dica Extra

Se quiser manter o navegador aberto após o teste para demonstração, adicione:

time.sleep(10)

antes do context.driver.quit() no step final.

🧠 “Automatizar é transformar o conhecimento humano em eficiência digital.”

— Dione Braga Ferreira
