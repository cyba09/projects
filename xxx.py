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

user = 'tzion.shahzaib@minutestep.com'
pswd = 'yexipic'


url='https://wiimaxx.com/'
driver.get(url) 

nme = driver.find_element(By.ID, "email")
nme.clear()
nme.send_keys(user)
pss  = driver.find_element(By.ID, "password")
pss.clear()
pss.send_keys(pswd)

lgn = driver.find_element(By.CSS_SELECTOR, '.login-btn')
lgn.click()
try:
    signin = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sidebar-header-name"))
    )
except:
    driver.quit()
marketing = driver.find_element(By.CSS_SELECTOR,'.item-marketing')
marketing.click()
driver.implicitly_wait(2)
virtual = driver.find_element(By.CSS_SELECTOR,'div.sidebar-menu-sub-item:nth-child(4) > a:nth-child(1) > div:nth-child(1)')
virtual.click()
driver.implicitly_wait(2)
################################################################add new
add_new = driver.find_element(By.CSS_SELECTOR, '.grid-button-cell > button:nth-child(1)')
driver.execute_script("arguments[0].click();", add_new)
driver.implicitly_wait(5)
domain = driver.find_element(By.CSS_SELECTOR, '.margin-width15p > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)')
domain.click()
sub = driver.find_element(By.CSS_SELECTOR,'#ui-select-choices-row-2-0')
sub.click()

land_to = driver.find_element(By.CSS_SELECTOR, 'div.input-with-validation:nth-child(5) > div:nth-child(1) > div:nth-child(1)')
land_to.click()
#driver.execute_script("arguments[0].click();", land_to)
driver.implicitly_wait(3)
subb = driver.find_element(By.CSS_SELECTOR,'#ui-select-choices-row-8-1 > a:nth-child(1) > span:nth-child(1)')
subb.click()

register_to = driver.find_element(By.CSS_SELECTOR, 'div.input-with-validation:nth-child(6) > div:nth-child(1) > div:nth-child(1)')
#driver.execute_script("arguments[0].click();", register_to)
register_to.click()
driver.implicitly_wait(3)
sb = driver.find_element(By.CSS_SELECTOR,'#ui-select-choices-row-9-1 > a:nth-child(1) > span:nth-child(1)')
sb.click()

descr = driver.find_element(By.CSS_SELECTOR,'.no-resize')
descr.clear()
descr.send_keys('testing')
img = driver.find_element(By.CSS_SELECTOR,'div.virtual-box:nth-child(1)')
img.click()
sve = driver.find_element(By.CSS_SELECTOR,'button.btn:nth-child(8)')
sve.click()
time.sleep(10)