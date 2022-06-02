from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
#from selenium.webdriver.chrome.options import Options

#options = Options()
#options.add_argument('--headless')

s = Service("./chromedriver_linux64/chromedriver")
#driver = webdriver.Chrome(service=s, options=options)
navegador = webdriver.Chrome(service=s)

navegador.get("https://lupa.uol.com.br/")
time.sleep(1)

#Clica no ok
navegador.find_element(by=By.XPATH,value='/html/body/div[3]/div/div[2]/button').click()

#Espera alguns segundos e vai no ícone da busca
time.sleep(0.5)
caminho_busca = '/html[1]/body[1]/div[2]/header[1]/div[1]/div[1]/div[1]/div[1]/div[2]/*[name()="svg"][1]'

navegador.find_element(by=By.XPATH,value = caminho_busca).click()
time.sleep(0.5)
#escrevendo palavra na busca

#navegador.find_elements_by_xpath('/html[1]/body[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/input[1]').send_keys("eleição")
pesquisa_eleicao = navegador.find_element(by=By.XPATH,value='/html[1]/body[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/input[1]')
pesquisa_eleicao.send_keys('eleição')
time.sleep(5)

navegador.find_element(by=By.XPATH, value='//*[@id="root"]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/span').click()
time.sleep(0.5)

navegador.find_element(by=By.XPATH, value='//*[@id="root"]/div[2]/div/div/div[2]/div/div[7]/div[2]/div[2]/button').click()
time.sleep(3)

