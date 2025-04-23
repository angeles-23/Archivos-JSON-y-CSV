import os, csv, functools
os.system('cls')


def cargar_datos():
    '''
    Carga el archivo CSV y lee los datos.
    '''
    with open('DATA.csv', mode='r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, quotechar='"')
        datos = list(reader)

        for linea in reader:
            print(linea)
    
    return datos
        


def convertir_puntuaciones_a_enteros():
    datos = cargar_datos()
    return datos




if __name__ == '__main__':
    print(convertir_puntuaciones_a_enteros())