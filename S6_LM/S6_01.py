import os, csv
os.system('cls')
from functools import reduce

with open('pasajeros.csv', mode='r', newline='', encoding='utf-8') as f:
    datos = list(csv.DictReader(f))


pares = list(map(
    lambda pasajero: (pasajero['nombre_pasajero'], pasajero['color_maleta']),
    datos
))

agrupados = reduce(
    lambda acumulador, par:{
        **acumulador, par[0]: acumulador.get(par[0],[]) + [par[1]]
    },
    pares,
    {}
)

print(agrupados)