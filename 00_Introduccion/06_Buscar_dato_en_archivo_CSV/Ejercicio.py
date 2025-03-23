import os, csv
os.system('cls')

def pedir_nombre():
    nombre = input('Introduce el nombre del producto: ')
    return nombre


def buscar_producto(fichero):
    nombre_producto = pedir_nombre().lower()
    producto_encontrado = False
    
    with open(fichero, 'r') as f:
        contenido = csv.DictReader(f)

        for fila in contenido:
            nombre = fila['nombre'].lower()

            if nombre == nombre_producto:
                producto_encontrado = True
                nombre_producto_buscado = fila['nombre']
                precio_producto_buscado = fila['precio']
                stock_producto_buscado = fila['stock']

    if producto_encontrado == False:
        return f'No se ha encontrado el producto {nombre_producto}'    
    else:
        return f'Producto encontrado: {nombre_producto_buscado} - Precio: {precio_producto_buscado}€ - Stock: {stock_producto_buscado} unidades'



if __name__ == '__main__':
    fichero = './00_Introduccion/05_Escribir_y_leer_CSV/productos.csv'
    print(buscar_producto(fichero))
