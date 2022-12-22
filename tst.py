import requests

headers = {
  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0',
  'Accept': '*/*',
  'Accept-Language': 'en-US,en;q=0.5',
  'Accept-Encoding': 'gzip, deflate, br',
  'Alt-Used': 'www.airhead.com',
  'Connection': 'keep-alive',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'TE': 'trailers',
  'Cookie': '_s=f2e9960a-d602-418f-83a2-faeb34bfc813; _shopify_s=f2e9960a-d602-418f-83a2-faeb34bfc813; _shopify_y=02edd703-98e7-448e-a216-4981ce293d66; _y=02edd703-98e7-448e-a216-4981ce293d66; secure_customer_sig='
}

my_file = open("links.txt", "r")
data = my_file.read()
data_into_list = data.split("\n")
my_file.close()

def get_link(link):
    
    try:
        r = requests.request("GET", link, headers=headers).json()
        if r['title']:
            with open('url.txt', "a+") as fhandle:
                        fhandle.write(f'{link}\n')
    except:
        pass

for link in data_into_list:
    get_link(link)