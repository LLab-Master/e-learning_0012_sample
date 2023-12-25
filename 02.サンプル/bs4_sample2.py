from bs4 import BeautifulSoup
import requests

url = 'https://www.lighthouselab.co.jp/p/data/sample.html' 
html = requests.get(url)
bsObj = BeautifulSoup(html.text,'lxml')

data = bsObj.findAll('tr')
for row in data:
    cells = row.findAll('td') 
    for cell in cells:
        print(cell.text + ', ', end='')
    print()
