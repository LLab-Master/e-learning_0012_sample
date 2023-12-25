import requests

url  = 'https://www.lighthouselab.co.jp/p/data/sample.html'
html = requests.get(url)

print(html.status_code)

print(html.text)