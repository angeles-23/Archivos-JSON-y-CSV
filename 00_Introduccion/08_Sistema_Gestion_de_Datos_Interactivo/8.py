import os, csv, json
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
    formato_texto = int(input('Elige el formato de texto: '))

    return formato_texto

def cargar_json():
    """
    Carga datos desde un archivo JSON si existe.

    Returns:
        list: Lista de diccionarios con los datos almacenados en el archivo JSON.
    """
    try:
        with open('./00_Introduccion/08_Sistema_Interactivo/8.json', 'r') as f:
            contenido_json = json.load(f)
    except FileNotFoundError:
        return []

    return contenido_json

def cargar_csv():
    """
    Carga datos desde un archivo CSV si existe.

    Returns:
        list: Lista de diccionarios con los datos almacenados en el archivo CSV.
    """
    lista_csv = []

    try:
        with open('./00_Introduccion/08_Sistema_Interactivo/8.csv', 'r') as f:
            contenido_csv = csv.reader(f)
            
            for fila in contenido_csv:
                lista_csv.append(fila)

        return lista_csv
    
    except FileNotFoundError:
        return lista_csv

def agregar_dato():
    """
    Permite al usuario agregar un nuevo dato y elegir si desea guardarlo en JSON o CSV.
    
    Args:
        Ninguno (los datos se solicitan mediante `input()`).

    Returns:
        None
    """
    id = int(input('ID: '))
    nombre = input('Nombre: ')
    precio = int(input('Precio: '))
    stock = int(input('Stock: '))

    nuevo_producto = {"id": id, "nombre": nombre, "precio": precio, "stock": stock}

    formato_texto = elegir_formato_texto()
    
    match formato_texto:
        case 1:
            with open('./00_Introduccion/08_Sistema_Interactivo/8.json', 'r') as f:
                contenido_json = json.load(f)
                
            contenido_json.append(nuevo_producto)

            with open('./00_Introduccion/08_Sistema_Interactivo/8.json', 'w') as f:
                json.dump(contenido_json, f, indent=4)
            
        case 2:
            with open('./00_Introduccion/08_Sistema_Interactivo/8.csv', 'a', newline='') as f: 
                contenido_csv = csv.writer(f)
                contenido_csv.writerow([id,nombre,precio,stock])

def ver_datos():
    """
    Permite visualizar los datos almacenados en JSON o CSV.

    Args:
        Ninguno (solicita al usuario elegir el formato a visualizar).

    Returns:
        None
    """
    formato = elegir_formato_texto()

    match formato:
        case 1:
            with open('./00_Introduccion/08_Sistema_Interactivo/8.json', 'r') as f:
                datos_json = json.load(f)

                for producto in datos_json:
                    print(producto)

        case 2:
            with open('./00_Introduccion/08_Sistema_Interactivo/8.csv', 'r') as f:
                datos_csv = csv.reader(f)
                
                for fila in datos_csv:
                    print(fila)

def eliminar_dato():
    """
    Permite al usuario eliminar un dato de un archivo JSON o CSV.

    Args:
        Ninguno (se solicita la entrada del usuario para seleccionar el dato a eliminar).

    Returns:
        None
    """
    producto_encontrado = False
    id_a_borrar = int(input('ID a eliminar: '))

    formato = elegir_formato_texto()

    match formato:
        case 1:
            with open('./00_Introduccion/08_Sistema_Interactivo/8.json', 'r') as f:
                contenido_json = json.load(f)

            for producto in contenido_json:
                id_producto = producto["id"]

                if id_producto == id_a_borrar:
                    contenido_json.remove(producto)
                    producto_encontrado = True

            with open('./00_Introduccion/08_Sistema_Interactivo/8.json', 'w') as f:
                json.dump(contenido_json, f, indent=4)        

            if producto_encontrado == True:
                print(f'Se ha borrado el producto con id {id_a_borrar}')
            else:
                print(f'No se ha encontrado el producto con id {id_a_borrar}')


        case 2:
            with open('./00_Introduccion/08_Sistema_Interactivo/8.csv', 'r') as f:
                contenido_csv = csv.reader(f)
                contenido_csv = list(contenido_csv)

            for producto in contenido_csv:
                id_producto = producto[0]
                id_producto = int(id_producto)

                if id_producto == id_a_borrar:
                    contenido_csv.remove(producto)
                    producto_encontrado = True
                    
            with open('./00_Introduccion/08_Sistema_Interactivo/8.csv', 'w', newline='') as f:
                escritor = csv.writer(f)
                escritor.writerows(contenido_csv)
                
            if producto_encontrado == True:
                print(f'Se ha borrado el producto con id {id_a_borrar}')
            else:
                print(f'No se encontró el producto con id {id_a_borrar}')



if __name__ == "__main__":
    cargar_json()
    cargar_csv()

    while True:
        try:
            mostrar_menu()
            opcion_menu = int(input('Opción menú: '))

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

        except Exception:
            print('Se ha producido un error. Vuelve a intentarlo')