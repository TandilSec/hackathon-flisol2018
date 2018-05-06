#!/bin/bash
         echo >> salida.dat
         SALIDA=''
         COUNTER=00000
         while [  $COUNTER -lt 10000 ]; do
             tarjeta=100
             tarjeta+=$COUNTER
             echo ========== Tarjeta $tarjeta ============
             url="http://www.gpssumo.com/movimientos/get_movimientos/"
             url+=$tarjeta
             SALIDA=$(curl $url)
             echo "${tarjeta}":${SALIDA}, >> salida.dat
            #curl $url | jq '.'
             let COUNTER=COUNTER+1
         done

#find . -name "*.txt" -size -3c -delete
