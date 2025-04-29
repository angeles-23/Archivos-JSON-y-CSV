import json, csv, os
os.system('cls')


def cargar_csv():
    with open('DATA.csv', mode='r', newline='', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        datos = list(lector)
    return datos


def encontrar_juego_mayor_puntuacion():
    datos = cargar_csv()
    videojuego_mayor_puntuacion = max(datos, key=lambda juego: float(juego['critic_score']) )
    return videojuego_mayor_puntuacion


def guardar_datos_juego_formato_json():
    mejor_juego = encontrar_juego_mayor_puntuacion()

    json_juego = {
        'title': mejor_juego['title'],
        'console': mejor_juego['console'],
        'genre': mejor_juego['genre'],
        'critic_score': mejor_juego['critic_score'],
        'total_sales':mejor_juego['total_sales']
    }

    return json_juego


def imprimir_json_resultante():
    juego_en_json = guardar_datos_juego_formato_json()
    print(json.dumps(juego_en_json, indent=4))



if __name__ == '__main__':
    # print(encontrar_juego_mayor_puntuacion())
    # print(guardar_datos_juego_formato_json())
    imprimir_json_resultante()