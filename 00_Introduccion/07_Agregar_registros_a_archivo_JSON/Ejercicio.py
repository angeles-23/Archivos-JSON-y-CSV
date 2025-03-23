import os
import json


os.system('cls')

def solicitar_datos():
    es_nombre_correcto = False
    es_edad_correcta = False
    es_email_correcto = False

    while es_nombre_correcto == False or es_edad_correcta == False or es_email_correcto == False:
        nombre = input('Introduce el nombre: ')
        edad = input('Introduce la edad: ')
        email = input('Introduce el email: ')

        if nombre.isalpha() == True:
            es_nombre_correcto = True

        if edad.isnumeric() == True:
            edad = int(edad)
            if edad > 0 and edad < 130:
                es_edad_correcta = True

        posicion_punto = email.find('.')
        posicion_arroba = email.find('@')

        if posicion_punto != -1 and posicion_arroba != -1 and posicion_arroba < posicion_punto:
            es_email_correcto = True
        
        if es_nombre_correcto == False:
            print('Nombre incorrecto')
        
        if es_edad_correcta == False:
            print('Edad incorrecta')
        
        if es_email_correcto == False:
            print('Email incorrecto')

        if es_nombre_correcto == False or es_edad_correcta == False or es_email_correcto == False:
            print('Existe algún elemento incorrecto. Vuelve a intentarlo')
        
    return nombre, edad, email


def agregar_persona(fichero):
    nombre, edad, email = solicitar_datos()

    nueva_persona = {'nombre': nombre, 'edad': edad, 'email': email}

    with open(fichero, 'r') as f:
        contenido_json = json.load(f)

    contenido_json.append(nueva_persona)

    # Guarda la lista actualizada en el archivo JSON
    with open(fichero, 'w') as f:
        json.dump(contenido_json, f, indent=4)

    print('\nNueva persona agregada con éxito.')


def mostrar_personas(fichero):
    with open(fichero, 'r') as f:
        personas = json.load(f)
    
    print('Lista de personas registradas:')
    for persona in personas:
        print(f'- {persona["nombre"]}')  


if __name__ == '__main__':
    fichero = './00_Introduccion/07_Agregar_registros_a_archivo_JSON/personas.json'
    agregar_persona(fichero)
    mostrar_personas(fichero)
