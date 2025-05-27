import os, csv
os.system('cls')


nombre_buscado = input('Nombre producto: ')

with open('productos.csv', mode='r', newline='', encoding='utf-8') as f:
    lector = csv.reader(f)
    
    for fila in lector:
        nombre = fila[0]
        precio = fila[1]
        stock = fila[2]

        if(nombre.lower() == nombre_buscado.lower()):
            producto_encontrado = True
            break
        else:
            producto_encontrado = False
            
    if(producto_encontrado == True):
        print(f'Producto encontrado: {nombre} - Precio: {precio}€ - Stock:{stock} unidades')
    else:
        print(f'No se ha encontrado el producto {nombre_buscado}')