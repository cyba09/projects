import requests
code = 'U16ECE697'
url = f"https://www.betway.co.za/BookABet/internal/GetClientSideBetslipForBookingCode?bookingCode={code}"

payload={}
headers = {
  'authority': 'www.betway.co.za',
  'accept': '*/*',
  'accept-language': 'en-ZA,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
  'cookie': 'Language=en-ZA; _gcl_au=1.1.1560753441.1665162983; MT=eb0cf472-bbcc-428f-8a53-b3cba50b9b30; _ga=GA1.3.492904608.1665162985; selectedSport~00000000-0000-0000-da7a-000000580001~sport=00000000-0000-0000-da7a-000000550001; selectedSport~00000000-0000-0000-da7a-000000580003~sport=00000000-0000-0000-da7a-000000550001; ASP.NET_SessionId=tb5vfptmvy1obx03ux4twpkz; __RequestVerificationToken=GskdORHI6Y2yXFef4vC_0z_nE0q2i9tHXlazOxah64zaEQUDKGVMMGp69BnNFZssxlT3j4n1I8R8ym4VGFoJ4qAAXZo1; __cf_bm=VbdQuVcx6ZFMk2DvL8jaqyZRQDfwCNZ1ftTsXgL4aLg-1666681563-0-ARCstbwcZEDun96+/e2LkHHmpwHeq1LKme30rFpcNKgf5qhBY1QiUgO/UFZoLwwNu1jbNxX5vUIRHYivN3yv5AY=; OriginalQueryString=/; FilterCount=0; InCashoutPoller=false; ActivateCashoutPolling=false; BTAGCOOKIE=P57471-PR347-CM26005-TS187894; ST=290963032415411935; _gid=GA1.3.932436895.1666681579; __cf_bm=hlPjzgRl72bYXpGEC3Hz_0asEv8XWCPmhlJXW6b.Kzw-1666682188-0-AVvlAYxvXo/I02fXKj/7WTw26+GgfbRQYrKxtjotu/lAuCaWf1Y9n0IcW64o5LieUBbhKPZRVzo6Sd29uzVy0U4=',
  'referer': 'https://www.betway.co.za/sport',
  'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
  'sec-ch-ua-mobile': '?1',
  'sec-ch-ua-platform': '"Android"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload).json()

print(response)
