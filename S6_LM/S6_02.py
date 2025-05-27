import os, csv
os.system('cls')
from functools import reduce

with open('pasajeros.csv', mode='r', newline='', encoding='utf-8') as f:
    datos = list(csv.DictReader(f))


pares = list( map (
    lambda pasajero: (pasajero['nacionalidad'], pasajero['peso_maleta']),
    datos
))

print(pares)

agrupar = reduce(
    lambda acumulador, par: {
        **acumulador, par[0]: acumulador.get(par[0], []) + [par[1]]
    },
    pares,
    {}
)

print(agrupar)

promedios = dict(map(
    lambda item: (item[0], sum(item[1]) / len(item[1])),
    agrupar.items()
))

print(promedios)
