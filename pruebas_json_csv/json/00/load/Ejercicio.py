import os, json
os.system('cls')

# Leer el archivo JSON y pasarlo a un diccionario 
with open('./load/datos.json', 'r') as f:
    datos = json.load(f)

print(datos)