from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')

s = Service("./chromedriver_linux64/chromedriver")
driver = webdriver.Chrome(service=s, options=options)


