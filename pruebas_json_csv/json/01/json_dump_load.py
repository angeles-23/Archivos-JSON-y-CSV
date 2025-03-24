# json.dump(): Guarda información en JSON
import json

numeros = [14,5,7,35]

with open('lista.json', 'w') as f:
    contenido_escrito = json.dump(numeros, f, indent=4)

# json.load(f): Lee la información del JSON
with open('lista.json', 'r') as f:
    contenido_leido = json.load(f)
    print(contenido_leido)