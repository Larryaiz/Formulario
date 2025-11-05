from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

# Configurações para simular um usuário humano
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

# Inicializa o navegador Edge
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)

# Abre o Google
driver.get("https://www.google.com")
time.sleep(3)

# Aceita cookies se aparecer
try:
    aceitar = driver.find_element(By.XPATH, "//button[contains(., 'Aceitar')]")
    aceitar.click()
    time.sleep(2)
except:
    pass  # ignora se não aparecer

# Pesquisa pelo termo
campo_pesquisa = driver.find_element(By.NAME, "q")
campo_pesquisa.send_keys("Instituto Joga Junto")
time.sleep(1.5)
campo_pesquisa.send_keys(Keys.RETURN)

# Aguarda o carregamento dos resultados
time.sleep(5)

# Seleciona o primeiro resultado e clica
resultados = driver.find_elements(By.CSS_SELECTOR, "h3")
if resultados:
    resultados[0].click()
    print("🌐 Site do Instituto Joga Junto aberto com sucesso!")
else:
    print("❌ Nenhum resultado encontrado.")

# Mantém o navegador aberto até o usuário pressionar Enter
input("Pressione Enter para encerrar...")
driver.quit()
