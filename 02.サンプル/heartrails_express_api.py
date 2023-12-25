import requests

param = { 'method': 'getStations', 'line' : 'JR山手線'}
URL = 'http://express.heartrails.com/api/json'

  
jsonData = requests.get(URL,param)

data = jsonData.json()
for s in data['response']['station']:
    print(s['name'])
