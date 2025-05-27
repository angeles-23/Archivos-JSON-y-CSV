import os 
os.system('cls')


texto = input('Introduce un mensaje: ')

with open('mensaje.txt', mode='w') as f:
    f.write(texto)


with open('mensaje.txt', mode='r') as f:
    contenido = f.read()

    print(f'Contenido del archivo: {contenido}')

