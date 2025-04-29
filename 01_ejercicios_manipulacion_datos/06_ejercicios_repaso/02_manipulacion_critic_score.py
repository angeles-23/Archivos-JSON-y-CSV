import os, csv
from functools import reduce

os.system('cls')


def cargar_datos():
    '''
    Carga el archivo CSV y lee los datos.
    '''
    with open('DATA.csv', mode='r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, quotechar='"')
        datos = list(reader)

    return datos
        


def convertir_puntuaciones_a_enteros():
    '''
    Convertir las puntuaciones de los críticos a enteros (por ejemplo, convertir 9.4 a 9).
    '''
    datos = cargar_datos()
    puntuaciones_transformadas = list( map (
                                lambda videojuego: {
                                    **videojuego, 
                                    'critic_score': round(float(videojuego['critic_score'])) 
                                }, datos) )
    
    return puntuaciones_transformadas



def calcular_media():
    '''
    Calcular el promedio de las puntuaciones de los críticos.
    '''
    datos = convertir_puntuaciones_a_enteros()

    suma = reduce(lambda total, videojuego: total + int(videojuego['critic_score']), datos, 0)
    media = suma / len(datos)

    return media



if __name__ == '__main__':
    # print(convertir_puntuaciones_a_enteros())
    print(calcular_media())