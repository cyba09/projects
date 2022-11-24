import requests
import pandas as pd

url = "http://chucklorre.com/card-json.php"

payload={}
headers = {
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'Accept-Language': 'en-ZA,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
  'Connection': 'keep-alive',
  'Content-Length': '0',
  'Origin': 'http://chucklorre.com',
  'Referer': 'http://chucklorre.com/?e=1433',
  'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
  'X-Requested-With': 'XMLHttpRequest'
}

response = requests.request("POST", url, headers=headers, data=payload).json()
lst = []
for i in range(762):
    try:
        air_date = response[str(i)]["episodes"]['0']["air_date_eng"]
    except:
        air_date = 'null'
    card = response[str(i)]["search_txt"]
    dct = {
        
        'air_date' : air_date,
        'card' : card
    }
    lst.append(dct)

df = pd.DataFrame(lst)
df.to_csv('chuck.csv', index= False)

    





