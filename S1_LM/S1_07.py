import os, csv, json
os.system('cls')


def cargar_datos_json():
    with open('personas.json', mode='r', newline='', encoding='utf-8') as f:
        datos = json.load(f)
    return datos


def pedir_datos():
    nombre = input('Introduce el nombre: ')
    edad = int(input('Introduce la edad: '))
    email = input('Introduce el email: ')

    nueva_persona = {'nombre':nombre, 'edad':edad, 'email':email}
    return nueva_persona


def añadir_persona():
    lista_personas = cargar_datos_json()
    lista_personas.append(pedir_datos())

    with open('personas.json', mode='w', newline='', encoding='utf-8') as f:
        json.dump(lista_personas, f, ensure_ascii=False, indent=4)

    print('\nNueva persona agregada con éxito.')


def listar_personas_registradas():
    lista_personas = cargar_datos_json()
    print('Lista de personas registradas:')

    for persona in lista_personas:
        print(f'- {persona['nombre']}')


if __name__ == '__main__':
    lista_personas = cargar_datos_json()
    añadir_persona()
    listar_personas_registradas()
    
