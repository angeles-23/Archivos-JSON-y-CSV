import os, json, csv
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
            precio = float(precio)
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



if __name__ == '__main__':
    archivo = './05_escribir_y_leer_CSV/productos.csv'

    productos = solicitar_productos()