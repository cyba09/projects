from playwright.sync_api import Playwright, sync_playwright
import time


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    page.goto('https://wiimaxx.com/')
    page.fill("#email", 'tzion.shahzaib@minutestep.com')
    page.fill('#password', 'yexipic')
    page.click('.login-btn')
    time.sleep(4)
    page.click('.item-marketing')
    page.click('div.sidebar-menu-sub-item:nth-child(4) > a:nth-child(1) > div:nth-child(1)') #virtualtracking
    page.click('.grid-button-cell > button:nth-child(1)')   #add new
    page.click('.margin-width15p > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)')#domain
    page.click('#ui-select-choices-row-2-0')
    #page.locator('text=Land To >> visible=true').click()
    #page.locator('text=Land To').click()
    #page.locator('text=Virtual Profile').click()
    #page.locator('.v-btn').click({force: True})
    page.fill('input.inline-form-input', 'AndreaB')
    time.sleep(7)
    page.click('div.virtual-box:nth-child(1)') #card
    page.click('button.btn:nth-child(8)')#save

    time.sleep(5)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)