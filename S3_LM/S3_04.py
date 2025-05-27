import os, json, csv
os.system('cls')
from functools import reduce


def filtrar_edades_mayores_25(edades):
    edades_mayores_25 = list(filter ( 
        lambda edad: edad > 25,
        edades
    ))
    return edades_mayores_25


def elevar_al_cuadrado(edades_mayores_25):
    cuadrados = list(map ( 
        lambda edad:edad**2,
        edades_mayores_25
    ))
    return cuadrados


def calcular_suma_total_edades(cuadrados):
    suma_total = reduce(
        lambda acumulador, edad: acumulador + edad,
        cuadrados,
        0
    )
    return suma_total



if __name__ == '__main__':
    edades = [18, 20, 30, 50, 60, 15, 45]
    mayores_25 = filtrar_edades_mayores_25(edades)
    print(mayores_25)
    cuadrdados = elevar_al_cuadrado(mayores_25)
    print(cuadrdados)
    print(calcular_suma_total_edades(cuadrdados))