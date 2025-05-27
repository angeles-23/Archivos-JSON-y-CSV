import os, csv, json
os.system('cls')


def cargar_csv():
    with open('DATA.csv', mode='r', newline='', encoding='utf-8') as f:
        datos = list(csv.DictReader(f))
    return datos



def agrupar_por_consola():
    datos = cargar_csv()
    agrupaciones_consola = set( map(
        lambda juego:juego['console'],
        datos
    ))
    return agrupaciones_consola


def ventas_totales_por_consola():
    consolas = agrupar_por_consola()
    datos = cargar_csv()

    ventas_consola = {}

    for consola in consolas:
        for dato in datos:
            datos_consola = dato['console']

            if consola == datos_consola:
                if consola not in ventas_consola:
                    ventas_consola[consola] = 1
                else:
                    ventas_consola[consola] += 1

    return ventas_consola


if __name__ == '__main__':
    # print(agrupar_por_consola())
    print(ventas_totales_por_consola())