from bs4 import BeautifulSoup
import requests

url = 'https://news.yahoo.co.jp/rss/topics/top-picks.xml'
html = requests.get(url)
bsObj = BeautifulSoup(html.text,'lxml')

items = bsObj.findAll('item')
for item in items:
    print(item.title.text)
