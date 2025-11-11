#Bibliotecas

from behave import given, when, then  
from selenium.webdriver import Edge  
from selenium.webdriver.edge.options import Options  
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys  
import time  

#Dado
@given("que o navegador Microsoft Edge está aberto e no formulário")
def step_open_browser(context):

    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    context.driver = Edge(options=options)
    context.driver.get("https://formulario-contato-m8p8.onrender.com/")
    time.sleep(3)

#Quando
@when('eu preencher os campos')
def preencher_formulario(context):
    d = context.driver
    d.find_element(By.NAME, "nome").clear()
    d.find_element(By.NAME, "nome").send_keys("Graziele Souza")
    time.sleep(4)
    d.find_element(By.NAME, "email").clear()
    d.find_element(By.NAME, "email").send_keys("grazielesilvasouza@hotmail.com")
    time.sleep(4)
    d.find_element(By.NAME, "telefone").clear()
    d.find_element(By.NAME, "telefone").send_keys("11-967077283")
    time.sleep(4)
    d.find_element(By.NAME, "bairro").clear()
    d.find_element(By.NAME, "bairro").send_keys("Barra velha alta")
    time.sleep(4)
    d.find_element(By.XPATH, "/html/body/div/div/form/div[3]/label[2]/input").click()
    time.sleep(4)
    d.find_element(By.NAME, "mensagem").clear()
    d.find_element(By.NAME, "mensagem").send_keys("Olá, essa é uma mensagem de teste")
    time.sleep(4)

#Então
@then("devo enviar o formulário preenchido")
def step_send(context):
    d = context.driver
    sucess = d.find_element(By.XPATH, "/html/body/div/div/form/button").click()
    time.sleep(5)
    if sucess:
        print("formulário enviado com sucesso")
    else:
        print("Algo deu errado. Formulário não enviado.")
    context.driver.quit()