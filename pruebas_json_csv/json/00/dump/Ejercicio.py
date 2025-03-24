import os, json
os.system('cls')


# Guardar un diccionario en un JSON
datos = {"nombre": "Carlos", "edad": 22, "ciudad": "Sevilla"}


# Abrimos el archivo JSON en modo escritura
with open('./dump/salida.json', 'w') as f:
    datos_json = json.dump(datos, f, indent=4)   # Escribimos el diccionario como JSON en el fichero

