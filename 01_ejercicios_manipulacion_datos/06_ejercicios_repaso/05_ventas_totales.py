import json, csv, os
os.system('cls')


def cargar_datos():
    with open('DATA.csv', mode='r', newline='', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        datos = list(lector)
    return datos


def agrupar_por_consola():
    datos = cargar_datos()
    consolas = set( map (lambda juego:juego['console'], datos) )

    ventas_consola = []

    for consola in consolas:
        ventas = 0.0
        for juego in datos:
            if(juego['console'] == consola):
                ventas += float(juego['total_sales'])
        ventas_consola.append({'console':consola, 'total_sales':round(ventas, 2)})

    return ventas_consola


if __name__ == '__main__':
   consolas = agrupar_por_consola()
   for consola in consolas:
       print(consola)