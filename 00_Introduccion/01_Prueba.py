import os
os.system('cls')

import json

data = {'nombre': 'Pedro', 'edad': 30, 'activo': True}

# Escribir de forma ordenada
with open('./00_Introduccion/datos.json', 'w') as f:
    json.dump(data, f, indent=4)


# Leer
with open('./00_Introduccion/datos.json', 'r') as f:
    json.load(f)