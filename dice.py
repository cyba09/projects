
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
from tqdm import tqdm
import os

a = b = c = d = e = f = g = h = i = j = 0
idx = 7
tot = 8



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

def write_text(mmm):
    file1 = open("myfile.txt", "a+")  # append mode
    file1.write(f"{mmm} \n")
    file1.close()

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
        ctme = datetime.now().strftime("%I:%M%p on %B %d, %Y")
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
        if red < 3.5:
            g = 0
            h += 1
        else:
            g += 1
            h = 0
        if blue < 3.5:
            i = 0
            j += 1
        else:
            i += 1
            j = 0
        '''print(f"one is ...{a}")
        print(f"two is ...{b}")
        print(f"three is .{c}")
        print(f"four is ..{d}")
        print(f"five is ..{e}")
        print(f"six is ...{f}")
        print(f"seven is .{g}")
        print(f"eight is .{h}")
        print(f"nine is ..{i}")
        print(f"ten is ...{j}")
        print('####################################')'''
        os.system('cls' if os.name == 'nt' else 'clear')
        pbar_a = tqdm(total=tot)
        pbar_a.set_description(f'one is ...{a}')
        pbar_a.update(a)
        pbar_a.close()

        pbar_b = tqdm(total=tot)
        pbar_b.set_description(f'two is ...{b}')
        pbar_b.update(b)
        pbar_b.close()

        pbar_c = tqdm(total=tot)
        pbar_c.set_description(f'three is .{c}')
        pbar_c.update(c)
        pbar_c.close()

        pbar_d = tqdm(total=tot)
        pbar_d.set_description(f'four is ..{d}')
        pbar_d.update(d)
        pbar_d.close()

        pbar_e = tqdm(total=tot)
        pbar_e.set_description(f'five is ..{e}')
        pbar_e.update(e)
        pbar_e.close()

        pbar_f = tqdm(total=tot)
        pbar_f.set_description(f'six is ...{f}')
        pbar_f.update(f)
        pbar_f.close()

        pbar_g = tqdm(total=tot)
        pbar_g.set_description(f'seven is .{g}')
        pbar_g.update(g)
        pbar_g.close()

        pbar_h = tqdm(total=tot)
        pbar_h.set_description(f'eight is .{h}')
        pbar_h.update(h)
        pbar_h.close()

        pbar_i = tqdm(total=tot)
        pbar_i.set_description(f'nine is ..{i}')
        pbar_i.update(i)
        pbar_i.close()

        pbar_j = tqdm(total=tot)
        pbar_j.set_description(f'ten is ...{j}')
        pbar_j.update(j)
        pbar_j.close()
    time.sleep(1)