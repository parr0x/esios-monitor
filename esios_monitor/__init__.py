import requests
import json
import sqlite3
import urllib


def get_values(start_date, end_date, indicators):
    print(start_date, end_date, indicators)
    urltemplate = "https://api.esios.ree.es/indicators/{indicator}?{query}"
    headers = {'content-Type': 'application/json',
               'Authorization': 'Token token=4ae31570833b25918e54ccbb20fe36f7ccf61767314764a65b9f51d0158e0575'}
    for an_indicator in indicators:
        query = urllib.parse.urlencode({
            'start_date': start_date,
            'end_date': end_date,
            'time_trunc': 'hour'
        })
        url = urltemplate.format(indicator=str(an_indicator), query=query)
        print(url)
        response = requests.get(url, headers=headers, stream=True)
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


indicators = [10167,10131,10122,10113,10104,10095,10086,10077,10074,10073,10064,25,20,14,15,9,2,1,3,4]
get_values('2019-06-01', '2019-06-02', indicators)
