import os
os.system('cls')

from functools import reduce


def cargar_datos():
    '''
    Carga los datos desde el archivo (sin usar csv).
    '''
    with open('clientes.csv', 'r') as f:
        lineas = f.readlines()
        cabecera = lineas[0].strip().split(',')
        datos = [dict (zip (cabecera, linea.strip().split(',')))   for linea in lineas[1:]]

    return datos


def buscar_clientes_mayores_de_edad():
    '''
    Filtra los clientes mayores de edad (≥18).
    '''
    datos = cargar_datos()
    mayores_de_edad = list(filter(lambda persona:int(persona['edad'])>=18, datos))
    return mayores_de_edad


def obtener_nombre_en_mayuscula():
    '''
    Obtén una lista con los nombres en mayúsculas.
    '''
    datos = cargar_datos()
    nombre = (list (map (lambda linea:linea['nombre'].upper(), datos)))

    return nombre



def obtener_total_de_clientes_mayores():
    '''
    Muestra el total de clientes mayores con reduce().
    '''
    datos = cargar_datos()
    
    total = reduce(lambda x,y: x + y)
    return total



if __name__ == '__main__':
    # print(cargar_datos())
    # print(buscar_clientes_mayores_de_edad())
    print(obtener_nombre_en_mayuscula())
    print(obtener_total_de_clientes_mayores())