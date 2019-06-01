import requests
import json
import pandas as pd  # Import Panda Library


url = "https://api.esios.ree.es/indicators/"
Fecha_Inicial = "2018-06-01"
Fecha_final = '2018-06-02'
a = "?start_date="
b = "T00:00:00&end_date="
t = "&time_trunc=hour"
i = [550, 2]
indicadores = len(i)
headers = {'content-Type': 'application/json', 'Authorization': 'Token token=4ae31570833b25918e54ccbb20fe36f7ccf61767314764a65b9f51d0158e0575'}
for j in range(indicadores):
    Miurl = url+str(i[j])+a+Fecha_Inicial+b+Fecha_final+t
    response = requests.get(Miurl, headers=headers, stream=True)
    print(response)

response.json()

a=0
q=data_dict["indicator"]["values"].__len__()
data_dict = json.loads(response.content.decode('UTF-8'))
print (data_dict["indicator"]["name"],data_dict["indicator"]["values"][00]["datetime_utc"],data_dict["indicator"]["values"][00]["value"])
while a<=q:
    print(data_dict["indicator"]["name"], data_dict["indicator"]["values"][a]["datetime_utc"],data_dict["indicator"]["values"][a]["value"])
    a+=1

a = pd.Series(data_dict, index = Index)


df = pd.DataFrame({"clase": clases, "tipo": tipos, "valor": valores})
pd.concat([df, a]
a=pd.DataFrame(data_dict["indicator"]["values"])

res= pd.DataFrame (columns=('name','datetime','value'))

import os
print (os.getcwd())

fichero=os.getcwd() + '\\' +data_dict["indicator"]["name"]
res.to_csv(fichero,index = None, header=True)