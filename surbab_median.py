from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import requests
from selenium.common import exceptions   
import csv 
from csv import writer
########################################################################################
options = Options()
options.headless = True
#options.add_argument('--no-sandbox')
options.add_argument("--start-maximized")
s=Service('/usr/local/bin/chromedriver')
#s=Service('./webdriver/chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)

def get_data(sb,st):
    url=f'http://house.speakingsame.com/p.php?q={sb}%2C+{st}'
    driver.get(url) 
    try:

        house = driver.find_element(By.CSS_SELECTOR, "#mainT > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > a:nth-child(1)").text
    except:
        house = 'no-value'
    try:
        unit = driver.find_element(By.CSS_SELECTOR, "#mainT > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > a:nth-child(1)").text
    except:
        unit = 'no-value'
    try:
        land = driver.find_element(By.CSS_SELECTOR, "#mainT > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > a:nth-child(1)").text
    except:
        land = 'no-value'
    #driver.close()
    return [house,unit,land]

def write_csv(ls):
    with open('fin.csv', 'a') as f_object:
 
        writer_object = writer(f_object)
 
        writer_object.writerow(ls)
 
  
        f_object.close()
################################################################
with open('sl.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
num = 0
for i in data:
  sbb = i[0]
  suburb = sbb.replace(' ', '+')
  state = i[2]
  ls = get_data(suburb,state)
  bg_ls =[i[0],i[1],i[2],ls[0],ls[1],ls[2]]
  write_csv(bg_ls)
  #suburb,code,state,house,unit,landsuburb,postcode,state,no-value,no-value,no-value
  num += 1
  print(num)





