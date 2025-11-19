#Bibliotecas
from behave import given, when, then  
from selenium.webdriver import Edge  
from selenium.webdriver.edge.options import Options  
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys  
import time  
from faker import Faker   
fake = Faker('pt_BR')     

#Dado
@given("que o navegador Microsoft Edge está aberto e na loja")
def step_open_browser(context):

    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    context.driver = Edge(options=options)
    context.driver.get("https://projetofinal.jogajuntoinstituto.org/")
    time.sleep(4)

#Quando
@when('eu seleciono criar conta, preencho e confirmo')
def preencher_formulario(context):
    d = context.driver

    d.find_element(By.CSS_SELECTOR, ".register > a:nth-child(1)").click()
    time.sleep(3)

   
    email_falso = fake.email()  
    context.email_gerado = email_falso 

    d.find_element(By.NAME, 'email').clear()
    d.find_element(By.NAME, 'email').send_keys(email_falso)

    d.find_element(By.CSS_SELECTOR, 'div.css-1v4ccyo:nth-child(2) > input:nth-child(1)').clear()
    d.find_element(By.CSS_SELECTOR, 'div.css-1v4ccyo:nth-child(2) > input:nth-child(1)').send_keys("ilhabela123")

    d.find_element(By.CSS_SELECTOR, '.MuiInputBase-inputAdornedEnd').clear()
    d.find_element(By.CSS_SELECTOR, '.MuiInputBase-inputAdornedEnd').send_keys("ilhabela123")

    d.find_element(By.CSS_SELECTOR, ".sc-dhKdcB").click()

    context.driver.save_screenshot("evidence_conta.png")
    time.sleep(5)

#Então
@then("devo voltar e logar")
def step_send(context):
    d = context.driver

    d.find_element(By.NAME, "email").clear()
    d.find_element(By.NAME, "email").send_keys(context.email_gerado)
    
    d.find_element(By.CSS_SELECTOR, "#outlined-adornment-password").clear()
    d.find_element(By.CSS_SELECTOR, "#outlined-adornment-password").send_keys("ilhabela123")

    btn = d.find_element(By.CSS_SELECTOR, ".sc-eqUAAy")
    btn.click()
    time.sleep(5)

    print("Login efetuado. Verifique o screenshot.")

    context.driver.save_screenshot("evidence_login.png")
    context.driver.quit()
