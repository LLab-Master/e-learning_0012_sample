import requests

url = 'https://www.python.org/static/community_logos/python-logo.png'
res = requests.get(url,stream=True)
if res.status_code == 200:
    with open('python-logo.png', 'wb') as file:
            for chunk in res.iter_content(chunk_size=1024):
                file.write(chunk)
