from urllib.request import urlopen

url  = 'https://www.lighthouselab.co.jp/p/data/sample.html'
html = urlopen(url)

encode=html.info().get_content_charset(failobj='utf-8')
print(encode)
