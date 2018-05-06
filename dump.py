import sys
import json
import requests
import demjson


if len(sys.argv) == 3:
    tarjeta_inicio = int(sys.argv[1])
    delta = int(sys.argv[2])
else:
    tarjeta_inicio = 10000000
    delta = 100

tarjeta_fin = tarjeta_inicio + delta

url = "http://www.gpssumo.com/movimientos/get_movimientos/"


try:
    with open("output.json", "r") as f:
        tarjetas = json.load(f)
except:
    tarjetas = {}


session = requests.session()

for tarjeta in range(tarjeta_inicio, tarjeta_fin):
    if str(tarjeta) not in tarjetas:
        response = session.get(url + str(tarjeta))
        tarjetas[tarjeta] = demjson.decode(response.text.strip())


with open("output.json", "w") as f:
    json.dump(tarjetas, f)
