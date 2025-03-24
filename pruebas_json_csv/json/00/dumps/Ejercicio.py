import os, json
os.system('cls')

# Diccionario a cadena JSON
datos = {"nombre": "Laura", "edad": 29, "ciudad": "Valencia"}

json_string = json.dumps(datos, indent=4)

print(json_string)
