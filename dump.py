import json
import requests
import demjson

tarjeta_inicio = 10000000
tarjeta_fin    = 10000100
url = "http://www.gpssumo.com/movimientos/get_movimientos/"

session = requests.session()

tarjetas = {}
for tarjeta in range(tarjeta_inicio, tarjeta_fin):
    response = session.get(url + str(tarjeta))
    tarjetas[tarjeta] = demjson.decode(response.text.strip())

with open("output.json", "w") as f:
    json.dump(tarjetas, f)
