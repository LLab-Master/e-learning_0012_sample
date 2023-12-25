import requests
import pandas as pd
import time

param = { 'method': 'getStations', 'line' : 'JR山手線'}
URL = 'http://express.heartrails.com/api/json'

  
data = requests.get(URL,param).json()

URL2 = 'https://zipcloud.ibsnet.co.jp/api/search'

stations = data['response']['station']
for station in stations:
    postal = station['postal']
    address = requests.get(URL2, {'zipcode':postal } )
    address = address.json()
    print("駅名:",station['name']) 
    print("住所：",address['results'][0]['address1'], 
          address['results'][0]['address2'],
          address['results'][0]['address3'])
    
    time.sleep(1)
