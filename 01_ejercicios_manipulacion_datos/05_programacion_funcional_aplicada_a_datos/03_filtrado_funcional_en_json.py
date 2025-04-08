import os, json
os.system('cls')

from functools import reduce



def cargar_datos():
    '''
    Carga los datos usando eval().
    '''
    with open('productos.json', 'r', encoding='utf-8') as f:
        texto = f.read() 
        texto = texto.replace('true','True').replace('false', 'False')
        datos = eval(texto)

    return datos
    

def filtrar_prductos_True():
    '''
    Filtra los productos con stock = true
    '''
    datos = cargar_datos()
    productos_True = list(filter(lambda producto:producto['stock'] == True, datos))
    return productos_True


def incrementar_IVA():
    datos = cargar_datos()

    nombres = (list(map(lambda producto:producto['nombre'], datos)))

    # precios_sin_IVA = reduce(lambda precios, producto: precios + int(producto['precio'])*0.21, datos, 0) 
    # print(precios_sin_IVA)
    precios_incrementados = reduce(lambda acumulador, producto: acumulador + producto['precio'] * 0.21, datos, 0)
    
    return nombres



if __name__ == '__main__':
    # print(cargar_datos())
    # print(filtrar_prductos_True())
    print(incrementar_IVA())
