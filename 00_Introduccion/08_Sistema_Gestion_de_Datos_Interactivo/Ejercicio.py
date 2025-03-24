import os, json, csv
os.system('cls')


def mostrar_opciones():
    print('\nMENÚ PRINCIPAL')
    print('1. Agregar')
    print('2. Ver')
    print('3. Eliminar')
    print('4. Convertir datos')
    print('5. Salir')


def elegir_formato_texto():
    print('\nMENÚ FORMATO')
    print('1. JSON')
    print('2. CSV')
    print('3. Salir')


def solicitar_datos():
    
    es_nombre_correcto = False
    es_edad_correcta = False
    es_activo_correcto = False
    es_activo = False
    son_hobbies_correcto = False
    es_direccion_correcta = False
    es_calle_correcto = False
    es_ciudad_correcto = False


    while True:

        while es_nombre_correcto == False:
            try:
                nombre = input('Nombre: ')

                if nombre.isalpha() == True:
                    es_nombre_correcto = True
                elif ' ' in nombre:
                    for caracter in nombre:
                        es_nombre_correcto = True

                if es_nombre_correcto == False:
                    print('Nombre incorrecto. Vuelve a intentarlo')

            except Exception:
                print('Error nombre. Has introducido un valor incorrecto')

        while es_edad_correcta == False:
            try:
                edad = int(input('Edad: '))

                if edad > 0 and edad < 130:
                    es_edad_correcta = True
                else:
                    print('Error valor numérico. La edad no está en el rango establecido')

                if es_edad_correcta == False:
                    print('Error. La edad es incorrecta. Vuelve a intentarlo')
            except Exception:
                print('Error edad. Has introducido un valor incorrecto')
            
        while es_activo_correcto == False:
            activo = input('Activo [S/N]: ').upper()

            if activo == 'S':
                es_activo = True
                es_activo_correcto = True
            elif activo == 'N':
                es_activo = False
                es_activo_correcto = True
            elif activo.isalpha() == True:
                print('Error activo. Has introducido un valor incorrecto. Vuelve a intentarlo')
            
        while son_hobbies_correcto == False:
            try:
                hobbies = input('Hobbies [separados por coma]: ')
                if ',' in hobbies and not hobbies.isnumeric():
                    lista_hobbies = []
                    lista_hobbies.append(hobbies)
                    son_hobbies_correcto = True
                else:
                    print('Error separación de hobbies')
                    
            except Exception:
                print('Error hobbies. Se ha producido un error. Vuelve a intentarlo')

        while es_direccion_correcta == False:
            direccion = {}

            calle = input('Calle: ')

            if calle.isnumeric() == False:
                es_calle_correcto = True
            else:
                print('Error calle. Se ha introducido un valor incorrecto')

            ciudad = input('Ciudad: ')
            if ciudad.isalpha() == True:
                es_ciudad_correcto = True
            elif ' ' in ciudad:
                for caracter in ciudad:
                    es_ciudad_correcto = True
                
            if es_ciudad_correcto == False:
                print('Error ciudad. Se ha introducido un valor incorrecto')

            if es_calle_correcto == True and es_ciudad_correcto == True:
                es_direccion_correcta = True
                direccion['calle'] = calle
                direccion['ciudad'] = ciudad
                
        return  nombre, edad, activo, hobbies, direccion


def agregar_json(fichero, nombre, edad, activo, hobbies, direccion):

    nuevo_dato = {"nombre":nombre, "edad":edad, "activo": activo, "hobbies":hobbies, "direccion":direccion}

    with open(fichero, 'w') as f:
        personas = []
        persona = json.dump(nuevo_dato, f, indent=4)
        personas.append(persona)
        print(persona)

def agregar_csv():
    ...

def ver_json():
    ...

def ver_csv():
    ...

def elimnar_json():
    ...

def eliminar_csv():
    ...

def convertir_json():
    ...

def convertir_csv():
    ...



if __name__ == '__main__':

    fichero_csv = './08/personas.csv'
    fichero_json = '/08/personas.json'

    # nombre, edad, activo, hobbies, direccion = solicitar_datos()
    nombre = 'Ana'
    edad = 15
    activo = True
    hobbies = ["futbol", "ajedrez"]
    direccion = {
        "calle": "Av. Adolfo Suárez",
        "ciudad": "Lorca"
    }


    opcion_menu = 0
    opcion_submenu = 0

    while opcion_menu != 5:
        try:
            mostrar_opciones()
            opcion_menu = int(input('Introduce una opción: '))

            match opcion_menu:
                case 1:
                    while opcion_submenu != 3:
                        try:
                            elegir_formato_texto()
                            opcion_submenu = int(input('Elige el tipo de formato: '))
                        except Exception:
                            print('Error submenú. Opción inválida')
                        else:
                            match opcion_submenu:
                                case 1:
                                    agregar_json(fichero_json, nombre, edad, activo ,hobbies, direccion)
                                case 2:
                                    agregar_csv(fichero_csv)
                        
                case 2:
                    while opcion_submenu != 3:
                        try:
                            elegir_formato_texto()
                            opcion_submenu = int(input('Elige el tipo de formato: '))
                        except Exception:
                            print('Error submenú. Opción inválida')
                        match opcion_submenu:
                            case 1:
                                ...
                            case 2:
                                ...
                            case 3:
                                ...
                            case _:
                                ...
                case 3:
                    while opcion_submenu != 3:
                        try:
                            elegir_formato_texto()
                            opcion_submenu = int(input('Elige el tipo de formato: '))
                        except Exception:
                            print('Error submenú. Opción inválida')
                        match opcion_submenu:
                            case 1:
                                ...
                            case 2:
                                ...
                            case 3:
                                ...
                            case _:
                                ...
                case 5:
                    print('Saliendo...')
                
            print()
        except Exception:
            print('Error menú. Opción inválida')
        
