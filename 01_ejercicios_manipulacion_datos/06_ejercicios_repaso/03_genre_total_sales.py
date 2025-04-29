import os, csv
os.system('cls')


def cargar_datos():
    with open('DATA.csv', mode='r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, quotechar='"')
        datos = list(reader)

    return datos


def filtrar_por_genero():
    datos = cargar_datos()
    juegos_de_accion = list( filter (lambda juego:juego['genre'] == "Action" 
                                     and  
                                     float(juego['total_sales']) > 15.00
                                     , datos)
                                     )

    return juegos_de_accion


if __name__ == '__main__':
    print(filtrar_por_genero())