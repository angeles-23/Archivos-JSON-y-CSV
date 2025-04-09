import os, json
os.system('cls')



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

    lista = (list(map(lambda productos: f'{productos['nombre']}, {productos['precio'] + (productos['precio']*0.21)}', datos)))

    # Otra forma de hacerlo:
    # nombres = (list(map(lambda producto:producto['nombre'], datos)))
    # precios_con_IVA = (list(map(lambda productos:productos['precio'] + (productos['precio']*0.21), datos)))

    # lista = []

    # for i in range(len(nombres)):
    #     lista.append(f'{nombres[i]}, {precios_con_IVA[i]}')

    return lista



if __name__ == '__main__':
    print(cargar_datos())
    print(filtrar_prductos_True())
    print(incrementar_IVA())
