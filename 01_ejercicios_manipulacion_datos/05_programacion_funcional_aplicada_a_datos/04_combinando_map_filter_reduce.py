import os 
os.system('cls')

from functools import reduce



def filtrar_mayores_25(edades):
    mayores_25 = list (filter (lambda edades:edades > 25, edades ) )
    return mayores_25


def elevar_al_cuadrado(edades):
    mayores_25 = filtrar_mayores_25(edades)
    edades_al_cudrado_mayores_25 = (list(map(lambda edades:edades**2, mayores_25)))
    return edades_al_cudrado_mayores_25


def sumar_edades(edades):
    edades_al_cuadrado_mayores_25 = elevar_al_cuadrado(edades)
    suma_edades = reduce(lambda acumulador, edad: acumulador + edad, edades_al_cuadrado_mayores_25)
    return suma_edades



if __name__ == '__main__':
    edades = [18, 20, 30, 50, 60, 15, 45]
    print(filtrar_mayores_25(edades))
    print(elevar_al_cuadrado(edades))
    print(sumar_edades(edades))