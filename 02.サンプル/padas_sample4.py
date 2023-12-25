import requests
import pandas as pd

param = { 'method': 'getStations', 'line' : 'JR山手線'}
URL = 'http://express.heartrails.com/api/json'

  
data = requests.get(URL,param).json()

stations = pd.DataFrame(data['response']['station'])

print(stations)
