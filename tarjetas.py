import sys
import json

with open(sys.argv[1]) as f:
    data = json.load(f)

agregados_tarjeta = {}
agregados_tipo = {}
for tarjeta, transacciones in data.items():
    tipos = {}
    try:
        for transaccion in transacciones:
            tipo = transaccion["tipo"]
            importe = float(transaccion["importe"].split("$", 2)[1].strip())
            if tipo not in tipos:
                tipos[tipo] = {"importe": 0.0, "cantidad": 0}
            tipos[tipo]["importe"] += importe
            tipos[tipo]["cantidad"] += 1
    except TypeError:
        pass

    for tipo in tipos:
        tipos[tipo]["promedio"] = tipos[tipo]["importe"] / tipos[tipo]["cantidad"]
        if tipo not in agregados_tipo:
            agregados_tipo[tipo] = {"importe": 0.0, "cantidad": 0}
        agregados_tipo[tipo]["importe"] += importe
        agregados_tipo[tipo]["cantidad"] += 1

    agregados_tarjeta[tarjeta] = tipos

for tipo in agregados_tipo:
    agregados_tipo[tipo]["promedio"] = agregados_tipo[tipo]["importe"] / agregados_tipo[tipo]["cantidad"]

print agregados_tipo
