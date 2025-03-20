import os, csv
os.system('cls')


def solicitar_productos():
    
    es_nombre_correcto = False
    es_precio_correcto = False
    es_stock_correcto = False
    

    while es_nombre_correcto == False or es_precio_correcto == False or es_stock_correcto == False:
        nombre = input('Nombre: ')
        precio = input('Precio: ')
        stock = input('Stock: ')

        if nombre.isalpha() == True:
            es_nombre_correcto = True

        if precio.isnumeric() == True:
            precio = int(precio)
            if precio > 0:
                es_precio_correcto = True

        if stock.isnumeric() == True:
            stock = int(stock)
            if stock > 0:
                es_stock_correcto = True

        if es_nombre_correcto == False:
            print('Nombre incorrecto')
            
        if es_precio_correcto == False:
            print('Precio incorrecto')

        if es_stock_correcto == False:
            print('Stock incorrecto')

        if es_nombre_correcto == False or es_precio_correcto == False or es_stock_correcto == False:
            print('Valores incorrectos. Vuelve a intentarlo\n')

    return nombre, precio, stock


def crear_lista_productos():

    lista_productos = []

    for producto in range(3):
        nombre, precio, stock = solicitar_productos()
        lista_productos.append({'nombre': nombre, 'precio': precio, 'stock': stock})
        print()

    return lista_productos

def guardar_productos(productos, archivo):
    with open(archivo, 'w', newline='') as f:
        escritor = csv.writer(f)
        escritor.writerow(['nombre', 'precio', 'stock'])
        
        for producto in productos:
            escritor.writerows(producto['nombre'])


def mostrar_productos(archivo):
    with open(archivo, 'r') as f:
        lector = csv.reader(f)
        for fila in lector:
            print(fila)


if __name__ == '__main__':
    archivo = './00_Introduccion/05_escribir_y_leer_CSV/productos.csv'

    productos = crear_lista_productos()
    guardar_productos(productos, archivo)
    mostrar_productos(archivo)


