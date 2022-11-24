import requests

url = "https://juicy-adult.com/api/profile/public/open-profile"

payload = "{\"accessKey\":\"FBP53R0zwyVGiv\",\"picWidth\":600}"
headers = {
  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0',
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'en-US,en;q=0.5',
  'Accept-Encoding': 'gzip, deflate, br',
  'Content-Type': 'application/json;charset=utf-8',
  'Origin': 'https://juicy-adult.com',
  'Connection': 'keep-alive',
  'Referer': 'https://juicy-adult.com/',
  'Cookie': '_ga=GA1.2.1910300408.1668310579; lopubp=HJSZzRbbylW; glink=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0cmFja2luZ0xpbmtJZCI6IkZCUDUzIiwiYSI6eyJpcCI6IjE1NC4xMTkuNTEuMTY0IiwiZGF0ZSI6MTY2ODQ5NjAxMDUxMX0sImlhdCI6MTY2ODQ5NjAxMCwiZXhwIjoxOTgzODU2MDEwLCJhdWQiOiJqdWljeS1hZHVsdC5jb20ifQ.Qty_cEe914tBblh3Npxka6g-ZmFULDNa0fUqExv6gqI; plink=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2Njg0OTYwMTAsImV4cCI6MTk4Mzg1NjAxMCwiYXVkIjoianVpY3ktYWR1bHQuY29tIn0.vL5CLAnPa83Bp2iJn3AtjvKA7-AqtizNbUO92TMUcAk; smid=s9Ablc-BR; auth-0=true; _gcl_au=1.1.1032555787.1668310766; _gid=GA1.2.977476774.1668442006; clink=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0cmFja2luZ0xpbmtJZCI6Ik5PTkUiLCJpYXQiOjE2Njg0NDM3MDgsImV4cCI6MTk4MzgwMzcwOCwiYXVkIjoianVpY3ktYWR1bHQuY29tIn0.SguznJeAQxG_YpfXUGFQTA0pTUulQhCcHdZicdrj26A; auth=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6InM5QWJsYy1CUiIsInJvbGUiOjEsInVzZXJuYW1lIjoiY3liYTA5IiwiY291bnRyeSI6IlpBIiwiYWZmaWxpYXRlSWQiOiJGQlAiLCJ0cmFja0xpbmtJZCI6IkZCUDUxIiwidHJhY2tpbmdMaW5rUGFyYW1zIjpudWxsLCJxdWV1ZUxhbmd1YWdlIjoiRU4iLCJpc0VtYWlsVmVyaWZpZWQiOmZhbHNlLCJlbWFpbCI6Im1wb2Z1bXVueWE5QGdtYWlsLmNvbSIsImFjY291bnRJZFByZWZpeCI6IkNMLSIsInVpTGFuZ3VhZ2UiOiJFTiIsImxvZ2dlZEluSWQiOiJzOUFibGMtQlIiLCJsb2dnZWRJblJvbGUiOjEsImxvZ2dlZEluVXNlck5hbWUiOiJjeWJhMDkiLCJpc1R3b0ZhY3RvckF1dGhQZW5kaW5nIjpmYWxzZSwiaWF0IjoxNjY4NDQzNzMyLCJleHAiOjE2NjkwNDg1MzIsImF1ZCI6Imp1aWN5LWFkdWx0LmNvbSJ9.MErr2ugmH2IWiCyoc1XlLD0iPvpE3OAfPBHsdsM6E1g; notification-offer=0%3A%3A%5B%5D%3A%3A4; pu-22-62385=1; _gat=1; glink=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0cmFja2luZ0xpbmtJZCI6IkZCUDUzIiwiYSI6eyJpcCI6IjU0Ljg2LjUwLjEzOSIsImRhdGUiOjE2Njg0OTY2Nzk5Njd9LCJpYXQiOjE2Njg0OTY2NzksImV4cCI6MTk4Mzg1NjY3OSwiYXVkIjoianVpY3ktYWR1bHQuY29tIn0.W6TjjpBH-x00xiK7ppBuLCYE4k7XGcaHTfaCTuN1z_E; lopubp=HJSZzRbbylW; plink=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2Njg0OTY2NzksImV4cCI6MTk4Mzg1NjY3OSwiYXVkIjoianVpY3ktYWR1bHQuY29tIn0.GBaCDU1lO8NgpbU4j8k9R0a82Ie4dcKE1DaLQEcwJ68',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin'
}

response = requests.request("POST", url, headers=headers, data=payload).json()

for link in response['links']:
    print(link["fileId"])

