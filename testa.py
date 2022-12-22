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
import const
from datetime import datetime, timedelta


bets = const.BETS
user = const.USER
key = const.KEY

options = Options()
options.headless = True
options.add_argument('--no-sandbox')
options.add_argument("--start-maximized")
s=Service('/usr/local/bin/chromedriver')
#s=Service('./webdriver/chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)

def trade(x):
    tabb = driver.find_element(By.CSS_SELECTOR, "div.J5ZZlDCTjcPDVTwQUuf4:nth-child(1) > div:nth-child(2)" )
    driver.execute_script("arguments[0].click();", tabb)
    ammnt = driver.find_element(By.ID,"amount-input")
    ammnt.clear()
    x = str(x)
    for i in x:
        ammnt.send_keys(i)
    
    logn = driver.find_element(By.CLASS_NAME, "place-bet-button")
    driver.execute_script("arguments[0].click();", logn)

def get_results():
    p = 1
    nw = datetime.now()
    d = nw.strftime('%Y-%m-%d')
    url3 = 'https://betgames9.betgames.tv/s/web/v1/game/results/testpartner?game_id=10&page={page}&date={date}&timezone=1'
    try:

       data = requests.get(url3.format(date=d, page=p)).json()
       lst = data['runs'][0]['results']
       gst = [round((data['runs'][0]['time'])/1000)]
       for i in data['runs'][0]['results']:
           gst.append(i['number'])
    except requests.ConnectionError:
        lst = 2
    return gst



    
    
########################################################################################
def placebet():  
    
    url='https://www.vegasbets.co.za/partner/bet-games'
    driver.get(url)
    try:
        signin = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "qa-Sign in"))
        )
    except:
        driver.quit()
    signin.click()
    time.sleep(1)
    #############################print(vegas.getList())
    elem = driver.find_element(By.ID, 'qa-username')
    elem.clear()
    elem.send_keys(user)
    passwd = driver.find_element(By.ID, 'qa-password')
    passwd.clear()
    passwd.send_keys(key)
    btn = driver.find_element(By.ID, 'qa-sign-in-button')
    btn.click()
    driver.switch_to.frame(driver.find_element(By.TAG_NAME,'iframe')) 
    try:
        element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.px2BltBZ9d0JArpfjthg:nth-child(11)"))
        )
    except:
        driver.quit()
    #element = driver.find_element(By.CSS_SELECTOR,"button.px2BltBZ9d0JArpfjthg:nth-child(11)")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(3)
    oddeven = driver.find_element(By.CSS_SELECTOR,'button.AKxHERhQ54809pCLD4UV:nth-child(3)')
    driver.execute_script("arguments[0].click();", oddeven)
    time.sleep(1)
    trade(bets[0])
    idxx = 0
    while idxx < len(bets):
        curr = datetime.now()
        hr = curr.hour
        if hr == 0:
            break
        try:
            tme = driver.find_element(By.CSS_SELECTOR,'button.px2BltBZ9d0JArpfjthg:nth-child(11) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)').text
        except:
            tme = '00:00'
        if tme == '00:27':
            lst = get_results()
            if len(lst) < 2:
                break
            red = lst[1]
            if red%2 != 0:
                break
            else:
                idxx += 1
                time.sleep(1)
                trade(bets[idxx])
        time.sleep(1)

    time.sleep(10)
    driver.close()

placebet()




