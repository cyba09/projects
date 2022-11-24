from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
import requests
from selenium.common import exceptions   
import csv 
from csv import writer
########################################################################################
options = Options()
#options.headless = True
#options.add_argument('--no-sandbox')
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
s=Service('/usr/local/bin/chromedriver')
#s=Service('./webdriver/chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)
#############################################################################################




url="https://www.eddiebauer.com/p/20612690/women's-microlight-down-parka?sp=1&color=Amethyst"
driver.get(url) 
driver.implicitly_wait(3)
nme = driver.find_element(By.CSS_SELECTOR, '//span[@class="old_price"]') #//span[@class="old_price"]//text()
print(nme.text)
driver.close()