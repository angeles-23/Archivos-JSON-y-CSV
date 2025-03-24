import os, json, csv
os.system('cls')

def mostrar_menu():
    print('\nMENÚ PRINCIPAL')
    print('1. Agregar')
    print('2. Ver')
    print('3. Eliminar')
    print('4. Salir')


def elegir_formato_texto():
    print('\nMENÚ FORMATO')
    print('1. JSON')
    print('2. CSV')
    print('3. Volver al menú principal')


def cargar_json(archivo):
    """
    Carga datos desde un archivo JSON si existe.

    Returns:
        list: Lista de diccionarios con los datos almacenados en el archivo JSON.
    """
    lista_datos = []

    try:
        with open(archivo, 'r') as f:
            datos_json = json.load(f)
    except FileNotFoundError:
        return 'No se ha encontrado el fichero JSON'
    else:
        for datos in datos_json:
            lista_datos.append(datos)
        
    return lista_datos


def cargar_csv(archivo):
    """
    Carga datos desde un archivo CSV si existe.

    Returns:
        list: Lista de diccionarios con los datos almacenados en el archivo CSV.
    """
    lista_datos = []

    try:
        with open(archivo, 'r') as f:
            datos_csv = csv.reader(f)

            for dato in datos_csv:
                lista_datos.append(dato)

    except FileNotFoundError:
        return 'No se ha encontrado el fichero CSV'

    return lista_datos


def agregar_dato():
    """
    Permite al usuario agregar un nuevo dato y elegir si desea guardarlo en JSON o CSV.
    
    Args:
        Ninguno (los datos se solicitan mediante `input()`).

    Returns:
        None
    """
    print('\n***AGREGAR DATO***')

    id = input('ID: ')
    nombre = input('Nombre: ')
    precio = input('Precio: ')
    stock = input('Stock: ')

    print('\nTipo de formato:')
    print('1. JSON')
    print('2. CSV')
    tipo_formato = int(input('Introduce el tipo de formato: '))

    match tipo_formato:
        case 1:
            nuevo_producto = {"id":id, "nombre":nombre, "precio":precio, "stock": stock}

            with open('./08/8.json', 'r') as f:
                contenido_json = json.load(f)
            
            contenido_json.append(nuevo_producto)

            with open('./08/8.json', 'w') as f:
                json.dump(contenido_json,f, indent=4)


        case 2:
            with open('./08/8.csv', 'a', newline="") as f:
                escritor = csv.writer(f)
                escritor.writerow([id, nombre, precio, stock])

        case _:
            print('Opción inválida. Vuelve a intentarlo')



def ver_datos():
    """
    Permite visualizar los datos almacenados en JSON o CSV.

    Args:
        Ninguno (solicita al usuario elegir el formato a visualizar).

    Returns:
        None
    """
    pass

def eliminar_dato():
    """
    Permite al usuario eliminar un dato de un archivo JSON o CSV.

    Args:
        Ninguno (se solicita la entrada del usuario para seleccionar el dato a eliminar).

    Returns:
        None
    """
    pass





if __name__ == "__main__":
    # Desarrollar el menú de opciones.

    archivo_json = './08/8.json'
    archivo_csv = './08/8.csv'

    cargar_json(archivo_json)
    cargar_csv(archivo_csv)

    opcion_menu = 0
    opcion_formato = 0

    while opcion_menu != 4:
        try:
            mostrar_menu()
            opcion_menu = int(input('Introduce una opción: '))

            match opcion_menu:
                case 1:
                    agregar_dato()
                case 2:
                    ver_datos()
                case 3:
                    eliminar_dato()
                case 4:
                    print('Saliendo...')
                    break
                case _:
                    print('Has introducido una opción que no existe')
        except Exception:
            print('Error. Has introducido un valor incorrecto')