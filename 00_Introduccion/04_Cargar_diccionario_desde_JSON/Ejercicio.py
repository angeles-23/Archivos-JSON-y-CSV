import os, json
os.system('cls')


def solicitar_datos_correctos():
    es_nombre_correcto = False
    es_edad_correcta = False
    es_email_correcto = False

    while es_nombre_correcto == False or es_edad_correcta == False or es_email_correcto == False:

        nombre = input('Nombre: ')
        edad = input('Edad: ')
        email = input('Email: ')

        if nombre.isalpha() == True:
            es_nombre_correcto = True

        if edad.isnumeric() == True:
            edad = int(edad)
            if edad >= 1 and edad <= 120:
                es_edad_correcta = True
        
        posicion_punto = email.find('.')
        posicion_arroba = email.find('@')

        if posicion_punto != -1 and posicion_arroba != -1 and posicion_punto > posicion_arroba:
            es_email_correcto = True

        if es_nombre_correcto == False:
            print('Nombre incorrecto')

        if es_edad_correcta == False:
            print('Edad incorrecto')
        
        if es_email_correcto == False:
            print('Email incorrecto')

        if es_nombre_correcto == False or es_edad_correcta == False or es_email_correcto == False:
            print('Valores incorrectos. Vuelve a introducirlos\n')

    return nombre, edad, email
    

def guardar_lista_en_diccionario(personas, fichero):
    f = open(fichero, 'w')
    json.dump(personas,f, indent=4)
    f.close()


def mostrar_nombre_personas(fichero):

    with open(fichero, 'r') as f:
        contenido = f.read()
        print('\nPersonas registradas: ')
        print(contenido)

        


if __name__ == '__main__':
    
    fichero = './04_Cargar_diccionario_desde_JSON/personas.json'
    personas = {}

    for i in range(3):
        print(f'Datos persona {i+1}: ')
        nombre, edad, email = solicitar_datos_correctos()
        personas[i] = {'nombre': nombre, 'edad':edad, 'email':email}
        print()

    guardar_lista_en_diccionario(personas, fichero)
    mostrar_nombre_personas(fichero)