import requests
from csv import writer

url = "https://wiimaxx.com/api/profile/virtual/search-for-tracking"


headers = {
  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0',
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'en-US,en;q=0.5',
  'Accept-Encoding': 'gzip, deflate, br',
  'Content-Type': 'application/json;charset=utf-8',
  'Origin': 'https://wiimaxx.com',
  'Connection': 'keep-alive',
  'Referer': 'https://wiimaxx.com/app/',
  'Cookie': 'auth=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IkZCUCIsInJvbGUiOjEyOCwidXNlcm5hbWUiOiJ0emlvbi5zaGFoemFpYkBtaW51dGVzdGVwLmNvbSIsImZ1bGxuYW1lIjoiMSAxIiwidXNlckFncmVlbWVudFBlbmRpbmciOmZhbHNlLCJhY2NvdW50SWRQcmVmaXgiOiJQQVJULSIsImlzQmxvY2tlZCI6ZmFsc2UsImxvZ2dlZEluSWQiOiJGQlAiLCJsb2dnZWRJblJvbGUiOjEyOCwibG9nZ2VkSW5Vc2VyTmFtZSI6InR6aW9uLnNoYWh6YWliQG1pbnV0ZXN0ZXAuY29tIiwiaXNUd29GYWN0b3JBdXRoUGVuZGluZyI6ZmFsc2UsImRldmljZVRva2VuIjoib2gzblNDYVJvIiwiaWF0IjoxNjY4MjExNjI2LCJleHAiOjE2Njg4MTY0MjYsImF1ZCI6IndpaW1heHguY29tIn0.2jJo_FPOMANhOxAZl4pyPLrFrHI4Ncq7xA3iECAO3cY; _ga=GA1.2.179680227.1668211631; _gid=GA1.2.1136373103.1668442091; io=W46g_UnLGx1ZVUIWAIol; io=KEkmRWYo_SKJpBLxAHfA',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin'
}



for i in range(0,76495,30):
    payload = "{\"isAdult\":true,\"siteId\":\"BG\",\"searchParams\":{\"country\":null,\"gender\":\"Female\",\"lookingFor\":\"Male\"},\"skipCount\":" + str(i) +"}"
    response = requests.request("POST", url, headers=headers, data=payload).json()
    print(f'getting {i}')
    for card in response:
        id = card["_id"]
        name = card["username"]
        ls = [id,name]
        with open('virtualid.csv', 'a') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(ls)
            f_object.close()
