import os, csv, json
os.system('cls')


def cargar_json():
    with open('productos.json', mode='r', newline='', encoding='utf-8') as f:
        contenido = json.load(f)

    return contenido


def filtrar_stock_True(datos):
    filtrado_True = list( filter(
        lambda producto: producto['stock'] == True,
        datos
    ))
    return filtrado_True


def precio_incrementado(datos):
    precio_incrementado = list( map (
        lambda producto:
            {'nombre':producto['nombre'], 
            'precio_con_iva':float(producto['precio']) + (producto['precio'] * 21 / 100)
            },
        datos
    ))
    return precio_incrementado



if __name__ == '__main__':
    datos = cargar_json()
    print(filtrar_stock_True(datos))
    print(precio_incrementado(datos))