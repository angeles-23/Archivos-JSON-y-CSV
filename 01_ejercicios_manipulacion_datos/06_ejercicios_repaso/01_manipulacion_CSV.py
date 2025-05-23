import csv, json, os
os.system('cls')


def cargar_y_leer_datos_csv():
    '''
    Carga el archivo CSV y lee los datos.
    '''
    with open('DATA.csv', mode='r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, quotechar='"')    
        datos = list(reader)

    return datos


def cambiar_titulos_a_mayuscula():
    '''
    Transforma los títulos de los videojuegos a mayúsculas utilizando map().
    '''
    datos = cargar_y_leer_datos_csv()

    # SOLO TITULOS EN MAYÚSCULA
    titulos_mayuscula = list( map (lambda videojuego: videojuego['title'].upper(), datos) )

    # TITULOS EN MAYUSCULA Y DEMÁS INFORMACIÓN
    titulos_e_informacion = list( map( lambda videojuego:{**videojuego, 'title': videojuego['title'].upper()}, datos ) )

    return titulos_e_informacion


def encontrar_videojuego_con_puntuacion_mayor_9():
    '''
    Filtra solo los videojuegos que tengan una puntuación de crítica superior a 9.0 usando filter()
    '''
    datos = cargar_y_leer_datos_csv()
    puntuacion_mayor_9 = list( filter( lambda videojuego: float(videojuego['critic_score']) > 9.0, datos) )
    return puntuacion_mayor_9


def mostrar_videojuegos_filtrados():
    '''
    Muestra los videojuegos filtrados.
    '''
    datos = cargar_y_leer_datos_csv()
    datos_formato = list( map( lambda videojuego: {'title':videojuego['title'].upper(), 
                                                    'console':videojuego['console'], 
                                                    'genre':videojuego['genre'], 
                                                    'critic_score':videojuego['critic_score'], 
                                                    'total_sales':videojuego['total_sales']
                                                    }, datos ) ) 
    
    datos_filtrados = list( filter (lambda videojuego: float(videojuego['critic_score']) > 9.0, datos_formato ) )
    
    for videojuego in datos_filtrados:
        print(videojuego)


if __name__ == '__main__':
    # print(cargar_y_leer_datos_csv())
    # print(cambiar_titulos_a_mayuscula())
    # print(encontrar_videojuego_con_puntuacion_mayor_9())
    mostrar_videojuegos_filtrados()