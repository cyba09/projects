import requests
import brotli


url = [
  "https://corralwwtx.com/products/ariat-mens-hand-tooled-western-belt-a1020467.js",
  'https://www.russells.com/products/ariat-mens-challenger-branding-iron-brown-brindle-western-cowboy-boots-10018695.js',
  'https://capitanboots.com/collections/western-boots/products/matador.js',
  'https://www.skipsboots.com/collections/womens-dresses/products/womens-dotted-mini-dress-md1542l.js',
  'https://www.airhead.com/products/wake-shaker-kneeboard.js',
  'https://euphoricequestrian.com/products/the-soleil-long-sleeve.js',
  'https://shopvitality.com/collections/restocked/products/the-tenacity-pant-midnight-silver-triangle-logo.js',
  'https://shopvitality.com/collections/restocked/products/the-tenacity-pant-midnight-silver-triangle-logo.js',
  'https://www.bucketculture.com/products/ycgm-imessage-t-shirt.js',
  'https://www.jambys.com/products/heather-gray-air-short-short.js',
  'https://www.leagueoutfitters.com/products/4-kg-8-8-lb-cast-iron-shot-put.js',
  'https://www.buffbunny.com/products/routeins.js'
]

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

r = requests.request("GET", url, headers=headers).json()
title = r['title']
price = r["price"]
image = r["featured_image"]

