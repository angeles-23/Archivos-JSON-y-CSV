import json, os
os.system('cls')

datos = {'nombre': 'David Nicanor', 'Correo':'david@gmail.com', 'numero':225487545}

# Escritura
with open('./02/david.json', 'w') as f:
    json.dump(datos,f,indent=4)
    

#Lectura
with open('./02/david.json', 'r') as f:
    datos = json.load(f)
    print(datos)
    del(datos['nombre'])    # Borrado momentaneo
    print(datos)



gato = {'nombre':'Misifus', 'color':'naranja'}

with open('./02/gato.json', 'w') as f:
    contenido = json.dump(gato, f, indent=4)
    

with open('./02/gato.json', 'r') as f:
    contenido = json.load(f)
    print(contenido)