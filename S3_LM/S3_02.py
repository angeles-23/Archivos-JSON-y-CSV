import os, csv, json
os.system('cls')

def cargar_csv():
    with open('clientes.csv', mode='r', newline='', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        datos = list(lector)
        
    return datos


def filtrar_mayores(datos):
    mayores = list( filter(
        lambda persona: int(persona['edad']) >= 18,
        datos
    ))
    return mayores 


def nombres_mayuscula(datos):
    nombres_en_mayuscula = list( map (
        lambda persona: persona['nombre'].upper(),
        datos
    ))
    return nombres_en_mayuscula

from functools import reduce
def total_clientes_mayores(datos):
    total_mayores = reduce(
        lambda contador, persona: contador + 1,
        datos,
        0
    )
    return total_mayores




if __name__ == '__main__':
    datos = cargar_csv()
    mayores_edad = filtrar_mayores(datos)
    # print(mayores_edad)
    nombres_en_mayus = nombres_mayuscula(mayores_edad)
    # print(nombres_en_mayus)

    print(total_clientes_mayores(nombres_en_mayus))

    