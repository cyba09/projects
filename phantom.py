import requests
import pandas as pd
import shutil

url = "https://phantombuster.com/api/v1/agent/8558197011716025/launch"

#Dictionary containing all IDs of the phantoms
lnk = {
  1: '8558197011716025',
  2: '746959376642153',
  3: '6001848293522291',
  4: '814145172124514',
  5: '5604628886725367'
}

headers = {
  'X-Phantombuster-Key': 'CSnrI8Om3Ml2Qt1AjXddG1dn0ifKs6gIEBBZElKMxUU'
}
#This request will launch the 'Sales Navigator Search Export' agent
#response = requests.request("GET", url, headers=headers)


json_link1 = 'https://cache1.phantombooster.com/xQSND3CHbqA/RrDrK886pnSqjoVcKU6z9w/result.json'
json_link2 = 'https://cache1.phantombooster.com/xQSND3CHbqA/QTamDvK5pS8EADLYPkodPA/result.json'
json_link3 = 'https://cache1.phantombooster.com/xQSND3CHbqA/gcAWK1Jaxil19M32lf2Isw/result.json'
json_link4 = 'https://cache1.phantombooster.com/xQSND3CHbqA/OZiiqLFI8n9FOFrVcapnow/result.json'
json_link5 = 'https://cache1.phantombooster.com/xQSND3CHbqA/USquIOD9oiT1dWOFCHFVdg/result.json'

csv_link1 = 'https://cache1.phantombooster.com/xQSND3CHbqA/RrDrK886pnSqjoVcKU6z9w/result.csv'
csv_link2 = 'https://cache1.phantombooster.com/xQSND3CHbqA/QTamDvK5pS8EADLYPkodPA/result.csv'
csv_link3 = 'https://cache1.phantombooster.com/xQSND3CHbqA/gcAWK1Jaxil19M32lf2Isw/result.csv'
csv_link4 = 'https://cache1.phantombooster.com/xQSND3CHbqA/OZiiqLFI8n9FOFrVcapnow/result.csv'
csv_link5 = 'https://cache1.phantombooster.com/xQSND3CHbqA/USquIOD9oiT1dWOFCHFVdg/result.csv'
#this response will get the latest data from the phantom i.e data from the above launch
#res = requests.request("GET", csv_link2)

response = requests.get(csv_link2, stream=True)

with open('two.csv', 'wb') as out_file:
  shutil.copyfileobj(response.raw, out_file)

print('done')
