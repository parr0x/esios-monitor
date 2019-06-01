import requests
import json
import sqlite3
import urllib

def descarga(datei, datef, ind):
    print(datei, datef, ind)


    url = "https://api.esios.ree.es/indicators/{indicator}?{query}"


    Fecha_Inicial = datei
    Fecha_final = datef
    aurl = "?start_date="
    b = "T00:00:00&end_date="
    t = "&time_trunc=hour"
    i = ind
    indicadores = len(i)
    headers = {'content-Type': 'application/json',
               'Authorization': 'Token token=4ae31570833b25918e54ccbb20fe36f7ccf61767314764a65b9f51d0158e0575'}
    for j in range(indicadores):
        query=urllib.parse.urlencode({
            'start_date': Fecha_Inicial,
            'end_date': Fecha_final,
            'time_trunc': 'hour'
        })
        Miurl = url.format(indicator=str(i[j]), query=query)
        print(Miurl)
        response = requests.get(Miurl, headers=headers, stream=True)
        print(response)
        data_dict = json.loads(response.content.decode('UTF-8'))
        _save_data(_interesting_values(data_dict), 'data.db')


def _save_data(data, db_path):

    conn = sqlite3.connect(db_path)
    conn.executemany('INSERT OR IGNORE INTO PBFSchedule VALUES (?,?,?)', data)
    conn.commit()
    conn.close()


def _interesting_values(source):
    name = source["indicator"]["name"]
    for record in source["indicator"]["values"]:
        yield (name, record["datetime"], record["value"])

descarga('2018-05-12', '2018-05-18', [10167])