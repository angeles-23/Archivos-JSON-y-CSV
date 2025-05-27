import os, csv
os.system('cls')

def cargar_csv():
    with open('DATA.csv', mode='r', newline='', encoding='utf-8') as f:
        datos = list(csv.DictReader(f))
    return datos



def filtrar_por_condiciones():
    datos = cargar_csv()

    genero_action_mas_15_mill = list( filter(
        lambda juego: juego['genre'] == 'Action' and float(juego['total_sales']) > 15.0,
        datos
    ))
    return genero_action_mas_15_mill







if __name__ == '__main__':
    print(filtrar_por_condiciones())