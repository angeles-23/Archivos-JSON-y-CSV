import csv, json, os
os.system('cls')

def cargar_datos():
    with open('DATA.csv', mode='r', newline='', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        datos = list(lector)
    return datos


def filtrar_videojuegos():
    datos = cargar_datos()
    videojuegos_superiores_a_15 = list( filter (lambda juego: float(juego['total_sales']) > 15.00, datos) )
    return videojuegos_superiores_a_15


def crear_csv():
    datos_filtrados = filtrar_videojuegos()

    with open('videjuegos_filtrados.csv', mode='w', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f)
        escritor.writerow(['title', 'console', 'total_sales'])

        for linea in datos_filtrados:
            escritor.writerow([linea['title'], linea['console'], linea['total_sales']])
    


if __name__ == '__main__':
    print(filtrar_videojuegos())
    crear_csv()