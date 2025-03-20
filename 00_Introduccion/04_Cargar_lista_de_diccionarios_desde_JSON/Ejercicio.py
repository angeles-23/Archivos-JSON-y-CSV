import os, json
os.system('cls')


def recibir_datos_correctos():
    
    es_nombre_correcto = False
    es_edad_correcto = False
    es_email_correcto = False

    while es_nombre_correcto == False or es_edad_correcto == False or es_email_correcto == False:
        nombre = input('Nombre: ')
        edad = input('Edad: ')
        email = input('Email: ')

        if nombre.isalpha() == True:
            es_nombre_correcto = True

        if edad.isnumeric() == True:
            edad = int(edad)
            if edad > 0 and edad < 120:
                es_edad_correcto = True

        posicion_punto =  email.find('.')
        posicion_arroba =  email.find('@')
            
        if posicion_punto != -1 and posicion_arroba != -1 and posicion_arroba < posicion_punto:
            es_email_correcto = True

        if es_nombre_correcto == False:
            print('Nombre incorrecto')

        if es_edad_correcto == False:
            print('Edad incorrecto')

        if es_email_correcto == False:
            print('Email incorrecto')
        
        if es_nombre_correcto == False or es_edad_correcto == False or es_email_correcto == False:
            print('Vuelve a intentarlo\n')
        else:
            print('Valores correctos\n')
            break

    return nombre, edad, email


def crear_lista_con_tres_diccionarios():
    personas = []

    for i in range(3):
        nombre, edad, email = recibir_datos_correctos()
        personas.append({'nombre':nombre, 'edad': edad, 'email': email})

    return personas


def anadir_lista_a_JSON(archivo, lista_personas):
    with open(archivo, 'w') as f:
        json.dump(lista_personas, f ,indent=4)


def mostrar_nombre_personas(archivo):
    with open(archivo, 'r') as f:
        contenido = json.load(f)

        print('Personas registradas:')
        for persona in contenido:
            print(f'- {persona['nombre']}')




if __name__ == '__main__':
    archivo = './00_Introduccion/04_Cargar_lista_de_diccionarios_desde_JSON/personas.json'

    lista_personas = crear_lista_con_tres_diccionarios()
    anadir_lista_a_JSON(archivo, lista_personas)
    mostrar_nombre_personas(archivo)
    