import os, csv
os.system('cls')

productos = [
    {'nombre':'Laptop', 'precio':1200, 'stock':5},
    {'nombre':'Mouse', 'precio':25, 'stock':20},
    {'nombre':'Teclado', 'precio':45, 'stock':15}
]


with open('productos.csv', mode='w', newline='', encoding='utf-8') as f:
    escritor = csv.writer(f)
    escritor.writerow(productos[0])
    
    for producto in productos:
        escritor.writerow([producto['nombre'], producto['precio'], producto['stock']])
    

with open('productos.csv', mode='r', newline='', encoding='utf-8') as f:
    lector = csv.reader(f)
    
    for linea in lector:
        print(f'{linea[0]},{linea[1]},{linea[2]}')