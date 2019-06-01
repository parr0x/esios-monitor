import requests

url = "https://api.esios.ree.es/indicators"

headers = {'content-Type': 'application/json', 'Authorization': 'Token token=4ae31570833b25918e54ccbb20fe36f7ccf61767314764a65b9f51d0158e0575'}
response = requests.get(url, headers=headers, stream=True)
print(response)