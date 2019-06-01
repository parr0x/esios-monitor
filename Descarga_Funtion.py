def descarga(datei, datef, ind):
    print(datei, datef, ind)
    import requests
    import json

    url = "https://api.esios.ree.es/indicators/"
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
        Miurl = url + str(i[j]) + aurl + Fecha_Inicial + b + Fecha_final + t
        response = requests.get(Miurl, headers=headers, stream=True)
        print(response)
        data_dict = json.loads(response.content.decode('UTF-8'))
        _save_data(interesting_values(data_dict), 'data.db')
    return


def _save_data(data, db_path):
    import sqlite3
    conn = sqlite3.connect(db_path)
    conn.executemany('INSERT OR IGNORE INTO PBFSchedule VALUES (?,?,?)', data)
    conn.commit()
    conn.close()


def interesting_values(source):
    name = source["indicator"]["name"]
    for record in source["indicator"]["values"]:
        yield (name, record["datetime"], record["value"])

descarga('2018-10-12', '2018-10-18', [10167])