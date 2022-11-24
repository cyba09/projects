
from ast import While
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
from datetime import datetime, timedelta

a = b = c = d = e = f = 0
idx = 7

def getList():
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


options = Options()
options.headless = True
options.add_argument('--no-sandbox')
options.add_argument("--start-maximized")
s=Service('/usr/local/bin/chromedriver')
#s=Service('./webdriver/chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)
url='https://www.vegasbets.co.za/partner/bet-games'
driver.get(url)
time.sleep(10)
driver.switch_to.frame(driver.find_element(By.TAG_NAME,'iframe'))

while True:
    try:
        tme = driver.find_element(By.CSS_SELECTOR,'button.px2BltBZ9d0JArpfjthg:nth-child(11) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)').text
    except:
        tme = '00:00'
    if tme == '00:27':
        lst = getList()
        if len(lst) < 2:
                continue
        red = lst[1]
        blue = lst[2]
        if red%2 != 0:
                a = 0
                b += 1
        else:
            a += 1 
            b = 0
        if blue%2 != 0:
            c = 0
            d += 1
        else:
            c += 1 
            d = 0
        sum = red + blue
        if sum%2 != 0:
            e = 0
            f += 1
        else:
            e += 1
            f = 0
        if a == idx:
            a = b = c = d = e = f = 0
            
        if b == idx:
            a = b = c = d = e = f = 0
            
        if c == idx:
            a = b = c = d = e = f = 0
            
        if d == idx:
            a = b = c = d = e = f = 0
            
        if e == idx:
            a = b = c = d = e = f = 0
            
        if f == idx:
            a = b = c = d = e = f = 0
            
        print(f'a is {a}')
        print(f'b is {b}')
        print(f'c is {c}')
        print(f'd is {d}')
        print(f'e is {e}')
        print(f'f is {f}')
        print("############################")
    time.sleep(1)