import requests
import pandas as pd

url = 'https://www.lighthouselab.co.jp/p/data/sample.html'
html = requests.get(url)

tables = pd.read_html( html.text)

table = tables[0]

table.to_csv( 'items.csv', encoding='shift_jis' )
