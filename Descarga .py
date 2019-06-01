import requests
import json
import pandas as pd  # Import Panda Library
import os

url = "https://api.esios.ree.es/indicators/"
Fecha_Inicial = "2019-01-01"
Fecha_final = '2019-04-22'
aurl = "?start_date="
b = "T00:00:00&end_date="
t = "&time_trunc=hour"
i = [10167,10131,10122,10113,10104,10095,10086,10077,10074,10073,10064,25,20,14,15,9,2,1,3,4]
indicadores = len(i)
headers = {'content-Type': 'application/json', 'Authorization': 'Token token=4ae31570833b25918e54ccbb20fe36f7ccf61767314764a65b9f51d0158e0575'}
for j in range(indicadores):
    Miurl = url+str(i[j])+aurl+Fecha_Inicial+b+Fecha_final+t
    response = requests.get(Miurl, headers=headers, stream=True)
    print(response)
    a = 0
    data_dict = json.loads(response.content.decode('UTF-8'))
    q = data_dict["indicator"]["values"].__len__()
    res = pd.DataFrame(columns=('name', 'datetime', 'value'))
    while a < q:
        res.loc[a, 'name'] = data_dict["indicator"]["name"]
        res.loc[a, 'datetime'] = data_dict["indicator"]["values"][a]["datetime"]
        res.loc[a, 'value'] = data_dict["indicator"]["values"][a]["value"]
        a += 1
    fichero = os.getcwd() + '\\ficheros\\' + data_dict["indicator"]["name"] +' ' + Fecha_Inicial + ' '+ Fecha_final
    print(fichero)
    res.to_csv(fichero, index=None, header=True)
