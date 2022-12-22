from seleniumwire import webdriver  # Import from seleniumwire
from selenium.webdriver import ChromeOptions
fireFoxOptions = ChromeOptions()
fireFoxOptions.headless = True

driver = webdriver.Chrome('/usr/local/bin/chromedriver',options=fireFoxOptions)

def interceptor(request):
    #del request.headers['Referer']  # Delete the header first
    request.headers['X-Phantombuster-Key'] = 'CSnrI8Om3Ml2Qt1AjXddG1dn0ifKs6gIEBBZElKMxUU'

# Set the interceptor on the driver
driver.request_interceptor = interceptor
driver.get("https://phantombuster.com/api/v1/agent/8558197011716025/launch?output=result-object")
print(driver.page_source)