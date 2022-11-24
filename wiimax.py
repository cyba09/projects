import requests
import csv
from csv import writer

url = "https://wiimaxx.com/api/profile/virtual/get"


headers = {
  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0',
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'en-US,en;q=0.5',
  'Accept-Encoding': 'gzip, deflate, br',
  'Content-Type': 'application/json;charset=utf-8',
  'Origin': 'https://wiimaxx.com',
  'Connection': 'keep-alive',
  'Referer': 'https://wiimaxx.com/app/',
  'Cookie': 'auth=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IkZCUCIsInJvbGUiOjEyOCwidXNlcm5hbWUiOiJ0emlvbi5zaGFoemFpYkBtaW51dGVzdGVwLmNvbSIsImZ1bGxuYW1lIjoiMSAxIiwidXNlckFncmVlbWVudFBlbmRpbmciOmZhbHNlLCJhY2NvdW50SWRQcmVmaXgiOiJQQVJULSIsImlzQmxvY2tlZCI6ZmFsc2UsImxvZ2dlZEluSWQiOiJGQlAiLCJsb2dnZWRJblJvbGUiOjEyOCwibG9nZ2VkSW5Vc2VyTmFtZSI6InR6aW9uLnNoYWh6YWliQG1pbnV0ZXN0ZXAuY29tIiwiaXNUd29GYWN0b3JBdXRoUGVuZGluZyI6ZmFsc2UsImRldmljZVRva2VuIjoib2gzblNDYVJvIiwiaWF0IjoxNjY4MjExNjI2LCJleHAiOjE2Njg4MTY0MjYsImF1ZCI6IndpaW1heHguY29tIn0.2jJo_FPOMANhOxAZl4pyPLrFrHI4Ncq7xA3iECAO3cY; _ga=GA1.2.179680227.1668211631; _gid=GA1.2.1136373103.1668442091; io=7Fv3FGd6smymf_XXAABP; io=KEkmRWYo_SKJpBLxAHfA',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin'
}


count = 0
with open('virtualid.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

for prof in data:
    count += 1
    print(count)
    vid = prof[0]
    #payload = "{\"profileId\":\"" + str(vid)   + " \"}"
    #payload = "{\"profileId\":\"EyeDP8Oyx\"}"
    payload = "{\"profileId\":\""+ str(vid) +"\"}"
    response = requests.request("POST", url, headers=headers, data=payload).json()
    #name,age,location, link, about, height, weight, hair color, body art, img)
    namee = response['username']
    vid = vid
    abt = response['profile']['mainInfo']['aboutMe']
    lctn = response['profile']['mainInfo']["location"]
    age = 2022 - int(response['profile']['mainInfo']["birthDayYear"])
    height = response['profile']["appearance"]["height"]
    weight = response['profile']["appearance"]["weight"]
    hair = response['profile']["appearance"]["hairColor"]
    body = response['profile']["appearance"]["bodyArt"]
    ls = [namee, vid, abt, lctn, age, height, weight,hair,body]
    with open('wiimax.csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(ls)
        f_object.close()


