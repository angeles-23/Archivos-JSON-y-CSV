import os, csv
os.system('cls')

def cargar_csv():
    with open('DATA.csv', mode='r', newline='', encoding='utf-8') as f:
        datos = list(csv.DictReader(f))
    return datos


def titulos_mayus():
    datos = cargar_csv()

    titulos_mayuscula = list(map(
        lambda juego: juego['title'].upper(),
        datos
    ))

    titulo_e_informacion = list(map(
        lambda juego:{**juego, 'title':juego['title'].upper()},
        datos
    ))

    return titulo_e_informacion


def puntuacion_mayor_9():
    datos = titulos_mayus()
    mayor_9 = list( filter (
        lambda juego: float(juego['critic_score']) > 9.0,
        datos
    ))
    return mayor_9


def mostrar_filtrados():
    datos = puntuacion_mayor_9()
    datos_formato = list (map (
        lambda juego: {'title': juego['title'],
                        'console': juego['console'],
                        'genre':juego['genre'],
                        'critic_score': juego['critic_score'],
                        'total_sales':juego['total_sales']
                       },
        datos
    ))
    return datos_formato

def guardar_csv(datos_finales):
    datos = cargar_csv()
    with open('guardado.csv', mode='w', newline='', encoding='utf-8') as f:
        campos = ['title', 'console', 'genre', 'critic_score', 'total_sales']
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(datos_finales)

if __name__ == '__main__':
    # print(titulos_mayus())
    print(mostrar_filtrados())
    filtrados = mostrar_filtrados()
    guardar_csv(filtrados)