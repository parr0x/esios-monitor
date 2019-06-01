import requests
import json
import pandas as pd  # Import Panda Library
import os
import wget

url = "https://api.esios.ree.es/archives/87/download"
Fecha_Inicial = "2018-06-01"
aurl = "?date="
burl = "T00:00:00"
Miurl = url+aurl+Fecha_Inicial+burl

headers = {'content-Type': 'application/json', 'Authorization': 'Token token=4ae31570833b25918e54ccbb20fe36f7ccf61767314764a65b9f51d0158e0575'}
response = requests.get(Miurl, headers=headers, stream=True)
print(response)

https://api.esios.ree.es/archives/87/download
url = "https://api.esios.ree.es/archives/110/download"
fichero = os.getcwd() + '\\' + 'descarga'
wget.download(url, fichero)