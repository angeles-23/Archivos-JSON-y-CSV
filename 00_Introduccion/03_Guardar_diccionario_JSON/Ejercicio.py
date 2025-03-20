import os, json
os.system('cls')


def recibir_datos_correctos():
    nombreCorrecto = False
    edadCorrecta = False
    emailCorrecto = False

    while nombreCorrecto == False or edadCorrecta == False or emailCorrecto == False:
        nombre = input('Nombre: ')
        edad = input('Edad: ')
        email = input('Email: ')

        if nombre.isalpha() == True:
            nombreCorrecto = True

        if edad.isnumeric() == True:
            edad = int(edad)
            if edad > 0 and edad <= 115:
                edadCorrecta = True
        
        posicion_punto = email.find('.')
        posicion_arroba = email.find('@')

        if posicion_punto != -1 and posicion_arroba != -1 and posicion_arroba < posicion_punto:
            emailCorrecto = True

        print()

        if nombreCorrecto == False:
            print('Nombre incorrecto')

        if edadCorrecta == False: 
            print('Edad incorrecta')

        if emailCorrecto == False:
            print('Correo incorrecto')

        if nombreCorrecto == True and edadCorrecta == True and emailCorrecto == True:
            print('Datos correctos')
            break
        
    return nombre, edad, email


def guardar_diccionario(datos):
    f = open('./00_Introduccion/03_Guardar_diccionario_JSON/persona.json', 'w')
    json.dump(datos, f, indent=4)
    f.close()


def leer_contenido(datos):
    f = open('./00_Introduccion/03_Guardar_diccionario_JSON/persona.json', 'r')
    contenido = f.read()
    print(contenido)
    f.close()


if __name__ == '__main__':
    nombre, edad, email = recibir_datos_correctos()
    datos = {'nombre': nombre, 'edad': edad, 'email': email}
    guardar_diccionario(datos)
    leer_contenido(datos)
    