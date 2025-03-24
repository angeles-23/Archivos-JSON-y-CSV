import os, json
os.system('cls')


# Leer cadenas de texto y pasarlo a diccionario
json_string = '{"nombre": "Ana", "edad": 25, "ciudad": "Barcelona"}'

# Convertimos el string JSON en un diccionario
datos = json.loads(json_string)

print(datos)