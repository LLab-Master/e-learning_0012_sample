from bs4 import BeautifulSoup

html_text = '''
<html>
    <head><title>Sample</title></head>
    <body>
        <a href='http://www.yahoo.co.jp'>Yahoo</a>
        <a href='http://www.amazon.co.jp'>Amazon</a>
        <a href='http://www.rakuten.co.jp'>楽天</a>
    </body>
</html>
'''
bsObj = BeautifulSoup(html_text,'lxml')
anchors = bsObj.findAll('a')
for a in anchors:
    print(a)
