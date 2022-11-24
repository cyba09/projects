from requests_html import HTMLSession

url = 'http://house.speakingsame.com/p.php?q=Lavington%2C+NSW'
session = HTMLSession()

r = session.get(url)
r.html.render()

items = about = r.html.find('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > b:nth-child(1)')
#items is the list of all divs with product info
print(items)