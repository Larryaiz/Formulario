from behave import given, when, then
from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@given("que o navegador Microsoft Edge está aberto")
def step_open_browser(context):
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    context.driver = Edge(options=options)
    context.driver.get("https://www.google.com")
    time.sleep(3)

@when('eu pesquisar por "Instituto Joga Junto" no Google')
def step_search_google(context):
    campo = context.driver.find_element(By.NAME, "q")
    campo.send_keys("Instituto Joga Junto")
    campo.send_keys(Keys.RETURN)
    time.sleep(4)

@then("devo ver o site do Instituto aberto com sucesso")
def step_verify_site(context):
    resultados = context.driver.find_elements(By.CSS_SELECTOR, "h3")
    if resultados:
        resultados[0].click()
        time.sleep(5)
        assert "jogajunto" in context.driver.current_url.lower()
        print("🌐 Site do Instituto Joga Junto aberto com sucesso!")
    else:
        raise AssertionError("❌ Nenhum resultado encontrado.")
    context.driver.quit()
