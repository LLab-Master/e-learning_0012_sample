from urllib.request import urlopen

url  = 'https://www.lighthouselab.co.jp/p/data/sample.html'
html = urlopen(url)

print(html.getcode())  


text_byte = html.read()

text = text_byte.decode('utf-8')
print(text)
