import os, csv
os.system('cls')

def cargar_csv():
    with open('DATA.csv', mode='r', newline='', encoding='utf-8') as f:
        datos = list(csv.DictReader(f))
    return datos


def transformar_a_enteros():
    datos = cargar_csv()

    transformacion = list(map(
        lambda juego: {**juego, 'critic_score':float(juego['critic_score']).__round__(0)},
        datos
    ))
    return transformacion

from functools import reduce


def calcular_promedio():
    datos = transformar_a_enteros()

    # 1+2+3/3

    suma = reduce(
        lambda acumulador, juego: acumulador + juego['critic_score'],
        datos,
        0
    )
    
    media = suma / len(datos)
    return media.__round__(2)
    


if __name__ == '__main__':
    # print(transformar_a_enteros())
    print(calcular_promedio())