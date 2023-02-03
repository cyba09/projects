from playwright.sync_api import Playwright, sync_playwright, expect
from bs4 import BeautifulSoup
import time
import pandas as pd

#first test
all_links = []
all_data = []

def run(playwright: Playwright, city):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.groupon.com/")
    page.locator("#closeForm").click()
    page.locator("#ls-location-cx").click()
    #page.locator("#ls-location-landing").fill('pasedena ca')
    page.locator("#ls-location").fill(city)
    page.keyboard.press("Enter")
    time.sleep(10)
    html = page.inner_html('body')
    soup = BeautifulSoup(html, 'html.parser')
    pgn = soup.select('li.slot > a')
    last = pgn[-1]
    last = last.getText()
    last = int(last)
    for i in range(1,2):
        time.sleep(5)
        page.goto(f'https://www.groupon.com/?page={i}')
        html = page.inner_html('#all-deals')
        soup = BeautifulSoup(html, 'html.parser')
        cards = soup.select('figure.card-ui')
        for card in cards:
            link = card.select_one('div:nth-child(1) > a:nth-child(1)').get('href')
            all_links.append(link)
        # ---------------------
    #########################################collected all the link now to loop them and get data
    for item in all_links:
        page.goto(item)
        time.sleep(5)
        html1 = page.inner_html('.main')
        soup = BeautifulSoup(html1, 'html.parser')
        try:
            nme = soup.select_one('#about-merchant > h3:nth-child(1)').get_text().strip()
            nme = nme.replace('About ','')
        except:
            nme = 'None'
        try:
            st = soup.select_one('.address-bottom').get_text().strip()
            
        except:
            st = 'None'
        ls = st.split(',')
        street = ls[0]
        city= ls[1].strip()
        ste = ls[-1]
        ste = ste.strip()
        ste = ste.split(' ')
        state = ste[0]
        zip_code = ste[-1]
        try:
            website = soup.select_one('#website-url').get('href')
        except:
            website = 'None'
        try:
            star = soup.select_one('#numerical-rating').get_text().strip()
        except:
            star = 'None'
        try:
            review = soup.select_one('.star-rating-text').get_text().strip()
            review = review.replace(' Groupon Ratings','')
        except:
            review = 'None'
        try:
            phone = soup.select_one('#phone-number').get_text().strip()
        except:
            phone = 'None'
        try:
            cat1 = soup.select_one('li.crumb:nth-child(2) > a:nth-child(1)').get_text().strip() #li.crumb:nth-child(2) > a:nth-child(1)
        except:
            cat1 = 'None'
        try:
            cat2 = soup.select_one('li.crumb:nth-child(3) > a:nth-child(1)').get_text().strip()
        except:
            cat2 = 'None'
        try:
            cat3 = soup.select_one('li.crumb:nth-child(4) > a:nth-child(1)').get_text().strip()
        except:
            cat3 = 'None'
        all_data.append({'Name' : nme,
                'Street' : street,
                'City' : city,
                'State' : state,
                'Zip' : zip_code,
                'Website' : website,
                'Star': star,
                'Review' : review,
                'Phone' : phone,
                'Category': cat1,
                'SubCat1':cat2,
                'SubCat2':cat3,
                'GrouponUrl':item,
                'Social' : '',
                'Email' : ''})
        
    context.close()
    browser.close()
    return all_data

    

sheet_url = 'https://docs.google.com/spreadsheets/d/1Tri2-pThGLDsaWFXrW9u9aiRWwllAlshDIXyGoLBgB8/edit#gid=1601342187'
url_1 = sheet_url.replace("/edit#gid=", "/export?format=csv&gid=")
df = pd.read_csv(url_1)
for city, state in zip(df['City'], df['State']):
        state = state.upper()
        st = f'{city} {state}'
        with sync_playwright() as playwright:
            lst = run(playwright,st)
            df = pd.DataFrame(lst)
            df.to_csv('groupon.csv', mode='a', index=False, header=False)




