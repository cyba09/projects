from requests_html import HTMLSession

url = "https://phantombuster.com/api/v1/agent/8558197011716025/launch"
session = HTMLSession()

payload={'output': 'result-object'}

headers = {
  'X-Phantombuster-Key': 'CSnrI8Om3Ml2Qt1AjXddG1dn0ifKs6gIEBBZElKMxUU',
  'output': 'result-object'
}

r = session.get(url, headers=headers, data=payload)
r.html.render()

print(r.text)