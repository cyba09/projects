import requests

all_data = []

link = 'https://openreview.net'
url = "https://api.openreview.net/notes?content.venue=NeurIPS+2022+Accept&details=replyCount&offset=300&limit=50&invitation=NeurIPS.cc%2F2022%2FConference%2F-%2FBlind_Submission"

payload={}
headers = {
  'authority': 'api.openreview.net',
  'accept': 'application/json, text/javascript, */*; q=0.01',
  'accept-language': 'en-ZA,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
  'access-control-allow-origin': '*',
  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'cookie': '_ga=GA1.2.1253157466.1669944730; _gid=GA1.2.690092507.1669944730; _gat_gtag_UA_108703919_1=1',
  'origin': 'https://openreview.net',
  'referer': 'https://openreview.net/',
  'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
  'sec-ch-ua-mobile': '?1',
  'sec-ch-ua-platform': '"Android"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload).json()


for item in response["notes"]:
    all_data.append(link + item["content"]["pdf"])

with open('pdf.txt', 'a+') as f:
    for line in all_data:
        f.write(f"{line}\n")
