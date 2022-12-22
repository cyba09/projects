from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common import exceptions   

########################################################################################
options = Options()
options.headless = True
#options.add_argument('--no-sandbox')
options.add_argument("--start-maximized")
s=Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=s, options=options)
url = "https://phantombuster.com/api/v1/agent/8558197011716025/launch"
driver.get(url) 
print(driver.page_source)

 






