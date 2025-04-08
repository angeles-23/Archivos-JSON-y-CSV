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
    nombre_mayuscula = (list (map (lambda linea:linea['nombre'].upper(), datos)))

    return nombre_mayuscula



def obtener_total_de_clientes_mayores():
    '''
    Muestra el total de clientes mayores con reduce().
    '''
    datos = cargar_datos()
    
    personas_mayores_edad = (list (filter (lambda linea: int(linea['edad']) >= 18, datos) ) ) 
    cantidad_personas = reduce(lambda contador, persona: contador + 1, personas_mayores_edad, 0)

    return cantidad_personas




if __name__ == '__main__':
    print(cargar_datos())
    print(buscar_clientes_mayores_de_edad())
    print(obtener_nombre_en_mayuscula())
    print(obtener_total_de_clientes_mayores())
