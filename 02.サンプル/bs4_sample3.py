from bs4 import BeautifulSoup
import requests

url = 'https://ja.wikipedia.org/wiki/Python'
html = requests.get(url)
bsObj = BeautifulSoup(html.text,'lxml')

table = bsObj.findAll('table',{'class':'wikitable'})[1]

rows = table.findAll('tr')
for row in rows:
    for cell in row.findAll(['td', 'th']):
        print(cell.get_text().strip() +  ',', end='' )
    print()
