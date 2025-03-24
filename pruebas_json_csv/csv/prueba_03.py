import os, csv
os.system('cls')

with open('prueba_03.csv', 'r') as f:
    lector = csv.DictReader(f)

    for fila in lector:
        print(fila["nombre"],fila['edad'])
        print(f'Nombre: {fila['nombre']}, Gmail: {fila['gmail']}')
