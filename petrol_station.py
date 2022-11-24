import requests
import pandas as pd
import csv
url = "https://www.wexinc.com/wp-content/themes/motorpass/inc/ajax/get-locations.php"

#
headers = {
  'authority': 'www.wexinc.com',
  'accept': 'application/xml, text/xml, */*; q=0.01',
  'accept-language': 'en-ZA,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'cookie': 'visid_incap_2221829=0L6ZDeAbQxGjJmFS1l7pcTvhZGMAAAAAQUIPAAAAAAA906jHUuie33N5XmIuDFgZ; nlbi_2221829=ObLXGaYXEn6zrmXHmggihAAAAABxZkyefjCJTcZDquHYlWAJ; incap_ses_6548_2221829=bsoKCgLiXxAHExXncyvfWjvhZGMAAAAA0T80YQahTMfeMfQ6DrAmfQ==; _gcl_au=1.1.1493386685.1667555646; _gid=GA1.2.826546398.1667555647; ln_or=d; _clck=b6ey6b|1|f6a|0; visitor_id565402=855045912; visitor_id565402-hash=6e091154aa6a1214309e064df84480d04a6344c0dd802ec1e4ea02ef525d818e297525e090eb7ed5f4350903b3688f3a998cac61; intercom-id-wzs1m06w=3f68389d-91a9-4318-9fd4-a24427e8b74a; intercom-session-wzs1m06w=; _ga=GA1.2.1218286211.1667555647; _uetsid=9f761a205c2611ed9dcf5dff31e12f6f; _uetvid=9f7648c05c2611edaa14df32d699c69d; _dc_gtm_UA-1416034-1=1; _clsk=1urlbla|1667556487244|13|1|j.clarity.ms/collect; _ga_HEMWX1F6HP=GS1.1.1667555647.1.1.1667556513.34.0.0; incap_ses_490_2221829=9wwqTtWxnCXDeev+KtXMBobnZGMAAAAAOGTKEVGmgx0+m5uIP4JgqQ==',
  'origin': 'https://www.wexinc.com',
  'referer': 'https://www.wexinc.com/motorpass/motorpass-locations/?loc=Acton%20ACT%202601%2C%20Australia&lat=-35.2799312&lng=149.1193233&customize_changeset_uuid=',
  'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
  'sec-ch-ua-mobile': '?1',
  'sec-ch-ua-platform': '"Android"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36',
  'x-requested-with': 'XMLHttpRequest'
}

#

#print(response.text)
with open('pp.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

for i in data:
  long = i[0]
  lat = i[1]
  payload = f"lat={lat}&lng={long}&radius=5"
  response = requests.request("POST", url, headers=headers, data=payload)
