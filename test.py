from seleniumwire import webdriver  # Import from seleniumwire
from selenium.webdriver import ChromeOptions
fireFoxOptions = ChromeOptions()
fireFoxOptions.headless = True
import pandas as pd


# Create a new instance of the Chrome driver
driver = webdriver.Chrome('/usr/local/bin/chromedriver',options=fireFoxOptions)
tst = False
# Go to the Google home page
def get(link):
    driver.get(link)
    for request in driver.requests:
        if request.response:
            link = request.url
            if link.endswith('.js'):
                ls = ['cdn','shopify','klaviyo','ajax','googleadservices', 'aspetnetcdn', 'amazon','static', 'static','google','youttube','facebook','gstatic', 'iframe','analytics', 'salebox'
                'afterpay', 'staticconnect','facebook','google-analytics', 'cart','googleapis']
                for word in ls:
                    if word in link:
                        tst = True
                if not tst:
                    with open('links.txt', "a+") as fhandle:
                        fhandle.write(f'{request.url}\n')
            tst = False

df = pd.read_excel('to_do_newlink.xlsx')
for link in df["url"]:
    get(link)
