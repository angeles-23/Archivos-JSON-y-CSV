import os, csv, json
os.system('cls')




def mostrar_menu():
    print('   MENU')
    print('1. Agregar')
    print('2. Ver')
    print('3. Eliminar datos')
    print('4. Salir')

def cargar_json():
    """
    Carga datos desde un archivo JSON si existe.

    Returns:
        list: Lista de diccionarios con los datos almacenados en el archivo JSON.
    """
    try:
        with open('S1_08.json', mode='r', newline='', encoding='utf-8') as f:
            datos = json.load(f)
    except FileNotFoundError as e:
        print('Fihero JSON no encontrado')
    return datos

def cargar_csv():
    """
    Carga datos desde un archivo CSV si existe.

    Returns:
        list: Lista de diccionarios con los datos almacenados en el archivo CSV.
    """
    try:
        datos = []

        with open('S1_08.csv', mode='r', newline='', encoding='utf-8') as f:
            lector = csv.DictReader(f)
            datos = list(lector)

    except FileNotFoundError:
        print('Fichero CSV no encontrado')
    return datos

def agregar_dato():
    """
    Permite al usuario agregar un nuevo dato y elegir si desea guardarlo en JSON o CSV.
    
    Args:
        Ninguno (los datos se solicitan mediante `input()`).

    Returns:
        None
    """
    
    nombre = input('Nombre: ')
    precio = float(input('Precio: '))
    stock = int(input('Stock: '))
    
    tipo_archivo = input('CSV o JSON: ').upper()

    match tipo_archivo:
        case 'CSV':
            datos_csv = cargar_csv()  
            id = len(datos_csv)+1
            
            diccionario_nuevo_dato = {"id": id, "nombre": nombre, "precio": precio, "stock": stock}
        
            with open('S1_08.csv', mode='a', newline='', encoding='utf-8') as f:
                campos = datos_csv[0].keys()
                escritor = csv.DictWriter(f, fieldnames=campos)
                escritor.writerow(diccionario_nuevo_dato)
        
        case 'JSON':
            datos_json = cargar_json()
            id = len(datos_json)+1
            diccionario_nuevo_dato = {"id": id, "nombre": nombre, "precio": precio, "stock": stock}

            datos_json.append(diccionario_nuevo_dato)

            with open('S1_08.json', mode='w', newline='', encoding='utf-8') as f:
                json.dump(datos_json, f, ensure_ascii=False, indent=4)

        case _:
            print('Opción incorrecta')

def ver_datos():
    """
    Permite visualizar los datos almacenados en JSON o CSV.

    Args:
        Ninguno (solicita al usuario elegir el formato a visualizar).

    Returns:
        None
    """
    
    opcion_tipo = input('CSV o JSON: ').upper()
    match opcion_tipo:
        case 'CSV':
            with open('S1_08.csv', mode='r', newline='', encoding='utf-8') as f:
                lector = csv.DictReader(f)

                for fila in lector:
                    print(fila)

        case 'JSON':
            with open('S1_08.json', mode='r', newline='', encoding='utf-8') as f:
                contenido = json.load(f)

                for linea in contenido:
                    print(linea)

        case _:
            print('Opción incorrecta del tipo de formato')

def eliminar_dato():
    """
    Permite al usuario eliminar un dato de un archivo JSON o CSV.

    Args:
        Ninguno (se solicita la entrada del usuario para seleccionar el dato a eliminar).

    Returns:
        None
    """
    tipo = input('CSV o JSON: ').upper()
    id_buscado = int(input('ID del producto a borrar: '))
    match tipo:
        case 'JSON':
            lista_json = []
            datos_json = cargar_json()

            for dato in datos_json:
                id = dato['id']
                if(id != id_buscado):
                    lista_json.append(dato)

            with open('S1_08.json', mode='w', newline='', encoding='utf-8') as f:
                json.dump(lista_json,f, ensure_ascii=False, indent=4)

        case 'CSV':
            lista_csv = []
            with open('S1_08.csv', mode='r', newline='', encoding='utf-8') as f:
                datos = csv.DictReader(f)

                for dato in datos:
                    id = int(dato['id'])
                    if(id != id_buscado):
                        lista_csv.append(dato)
            
            with open('S1_08.csv', mode='w', newline='', encoding='utf-8') as f:
                campos = lista_csv[0].keys()
                escritor = csv.DictWriter(f, fieldnames=campos)
                escritor.writeheader()
                escritor.writerows(lista_csv)


if __name__ == '__main__':
    salir = True
    while salir != False:
        try:
            mostrar_menu()
            opcion = int(input('Opción: '))

            if opcion > 0 and opcion < 5:
                match opcion:
                    case 1:
                        agregar_dato()
                    case 2:
                        ver_datos()
                    case 3:
                        eliminar_dato()
                    case 4:
                        salir = False
                print('')
            else:
                print('Error: opción fuera del rango [1-4]')

        except Exception as e:
            print(e)