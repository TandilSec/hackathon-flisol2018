import sys
import csv
import requests
import demjson

reload(sys)
sys.setdefaultencoding('utf-8')

if len(sys.argv) == 3:
    tarjeta_inicio = int(sys.argv[1])
    delta = int(sys.argv[2])
else:
    tarjeta_inicio = 10000000
    delta = 100

tarjeta_fin = delta + tarjeta_inicio

url = "http://www.gpssumo.com/movimientos/get_movimientos/"

tarjetas = {}

session = requests.session()

with open('tarjetas.csv', 'wb') as myfile:
    out = csv.writer(myfile, quoting=csv.QUOTE_ALL)

    for tarjeta in range(tarjeta_inicio, tarjeta_fin):
        if str(tarjeta) not in tarjetas:
            response = session.get(url + str(tarjeta))
            transacciones_tarjeta = demjson.decode(response.text.strip())
            try:
                iterator = iter(transacciones_tarjeta)
            except TypeError:
                print tarjeta,' no existente o error'
            else:
                print tarjeta
                for transaccion in transacciones_tarjeta:
                    row = [tarjeta]
                    for key, value in transaccion.iteritems():
                        row.append(value)
                    out.writerow(row)
