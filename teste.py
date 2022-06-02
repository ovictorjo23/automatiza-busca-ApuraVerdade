from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("./chromedriver_linux64/chromedriver")
driver = webdriver.Chrome(service=s)
