import requests

url = 'http://www.post.japanpost.jp/zipcode/dl/oogaki/zip/13tokyo.zip'
res = requests.get(url,stream=True)
if res.status_code == 200:
    with open('13tokyo.zip', 'wb') as file:
            for chunk in res.iter_content(chunk_size=1024):
                file.write(chunk)
