import requests, csv
from csv import writer

url = "https://juicy-adult.com/api/profile/private/open-profile"


headers = {
  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0',
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'en-US,en;q=0.5',
  'Accept-Encoding': 'gzip, deflate, br',
  'Content-Type': 'application/json;charset=utf-8',
  'Origin': 'https://juicy-adult.com',
  'Connection': 'keep-alive',
  'Referer': 'https://juicy-adult.com/',
  'Cookie': '_ga=GA1.2.1910300408.1668310579; lopubp=HJSZzRbbylW; glink=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0cmFja2luZ0xpbmtJZCI6IkZCUDUzIiwiYSI6eyJpcCI6IjQxLjEzLjIwOC4xMTAiLCJkYXRlIjoxNjY4NDQzNjgxNDA2fSwiaWF0IjoxNjY4NDQzNjgxLCJleHAiOjE5ODM4MDM2ODEsImF1ZCI6Imp1aWN5LWFkdWx0LmNvbSJ9.19pkqqJaC1mrlw3gFHjs8GvECk3Sn39a6eYUxT_HOpw; plink=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2Njg0NDM2ODEsImV4cCI6MTk4MzgwMzY4MSwiYXVkIjoianVpY3ktYWR1bHQuY29tIn0.avlkd-vwh0vdBCJxrVhbPdbsmUAZ-ojiljpk7coZqGM; smid=s9Ablc-BR; auth-0=true; _gcl_au=1.1.1032555787.1668310766; _gid=GA1.2.977476774.1668442006; pu-22-62385=1; clink=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0cmFja2luZ0xpbmtJZCI6Ik5PTkUiLCJpYXQiOjE2Njg0NDM3MDgsImV4cCI6MTk4MzgwMzcwOCwiYXVkIjoianVpY3ktYWR1bHQuY29tIn0.SguznJeAQxG_YpfXUGFQTA0pTUulQhCcHdZicdrj26A; auth=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6InM5QWJsYy1CUiIsInJvbGUiOjEsInVzZXJuYW1lIjoiY3liYTA5IiwiY291bnRyeSI6IlpBIiwiYWZmaWxpYXRlSWQiOiJGQlAiLCJ0cmFja0xpbmtJZCI6IkZCUDUxIiwidHJhY2tpbmdMaW5rUGFyYW1zIjpudWxsLCJxdWV1ZUxhbmd1YWdlIjoiRU4iLCJpc0VtYWlsVmVyaWZpZWQiOmZhbHNlLCJlbWFpbCI6Im1wb2Z1bXVueWE5QGdtYWlsLmNvbSIsImFjY291bnRJZFByZWZpeCI6IkNMLSIsInVpTGFuZ3VhZ2UiOiJFTiIsImxvZ2dlZEluSWQiOiJzOUFibGMtQlIiLCJsb2dnZWRJblJvbGUiOjEsImxvZ2dlZEluVXNlck5hbWUiOiJjeWJhMDkiLCJpc1R3b0ZhY3RvckF1dGhQZW5kaW5nIjpmYWxzZSwiaWF0IjoxNjY4NDQzNzMyLCJleHAiOjE2NjkwNDg1MzIsImF1ZCI6Imp1aWN5LWFkdWx0LmNvbSJ9.MErr2ugmH2IWiCyoc1XlLD0iPvpE3OAfPBHsdsM6E1g; _gat=1',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin'
}

#

with open('juicy.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

for nme in data:
    namee = nme[1]
    payload = "{\"username\":\"" + str(namee) + "\",\"skipView\":true}"
    #body = body.encode(encoding='utf-8')
    payload = payload.encode(encoding='utf-8')
    response = requests.request("POST", url, headers=headers, data=payload).json()
    username = response['username']
    age = 2022 - int(response['mainInfo']['birthDayYear'])
    location = response['mainInfo']['location']
    about = response['mainInfo']['aboutMe']
    height = response['appearance']['height']
    hair = response['appearance']['hairColor']
    art = response['appearance']['bodyArt']
    link = response['id']
    link = 'https://juicy-adult.com/#/public/' + link
    ls = [username, age, location,link, about, height,hair, art]
    with open('profile.csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(ls)
        f_object.close()
