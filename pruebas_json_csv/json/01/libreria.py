import os, json
os.system('cls')

archivo = 'hola.json'

try:
    with open(archivo, 'r') as f:
        leer_archivo = json.load(f)
except FileNotFoundError:
    texto = 'Hola'
    with open(archivo, 'w') as f:
        json.dump(texto, f)
else:
    print(leer_archivo)