import csv, os
os.system('cls')

with open('prueba_01.csv', 'r') as f:
    lector = csv.reader(f)
    
    for fila in lector:
        print(fila)