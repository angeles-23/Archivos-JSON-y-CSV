import os, csv, json
os.system('cls')

def cargar_csv():
    with open('DATA.csv', mode='r', newline='', encoding='utf-8') as f:
        datos = list(csv.DictReader(f))
    return datos


def juego_mejor_puntuacion_critica():
    datos = cargar_csv()
    mayor_puntuacion = max(datos, key=lambda juego: float(juego['critic_score']))
    return mayor_puntuacion


def crear_json():
    mejor_juego = juego_mejor_puntuacion_critica()
    dict_json = {
                    'title':mejor_juego['title'],
                    'console':mejor_juego['console'],
                    'total_sales':mejor_juego['total_sales']
                }
    
    with open('mejor_juego.json', mode='w', newline='', encoding='utf-8') as f:
        json.dump(dict_json, f, ensure_ascii=False, indent=4)


def mostrar_json():
    with open('mejor_juego.json', mode='r', newline='', encoding='utf-8') as f:
        contenido = json.load(f)
        print(contenido)



if __name__ == '__main__':
    # print(juego_mejor_puntuacion_critica())
    crear_json()
    mostrar_json()