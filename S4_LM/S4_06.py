import os, json, csv
os.system('cls')
from functools import reduce


def cargar_csv():
    with open('DATA.csv', mode='r', newline='', encoding='utf-8') as f:
        datos = list(csv.DictReader(f))
    return datos


def filtrar_ventas():
    datos = cargar_csv()

    ventas_superiores_15_mill = list(filter(
        lambda juego: float(juego['total_sales']) > 15.0,
        datos
    ))

    return ventas_superiores_15_mill


def crear_csv():
    datos = cargar_csv()
    juegos =  filtrar_ventas()

    lista_diccionarios = []

    for juego in juegos:
        juego_a_introducir = {
                                'title':juego['title'], 
                                'console':juego['console'],
                                'total_sales':juego['total_sales']
                            }
        lista_diccionarios.append(juego_a_introducir)


    with open('videojuegos_mas_vendidos.csv', mode='w', newline='', encoding='utf-8') as f:
        campos = ['title', 'console', 'total_sales']
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(lista_diccionarios)









if __name__ == '__main__':
    # print(filtrar_ventas())
    print(crear_csv())
