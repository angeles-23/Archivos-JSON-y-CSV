import os, json
os.system('cls')

'''
Json in Python
json.loads(): cadena JSON -> diccionario
json.load(): lee JSON -> diccionario   (cargar un archivo JSON)
json.dumps(): 
json.dump():
'''

# String con formato JSON
json_str = '{"nombre": "Juan", "edad":30, "city": "Madrid"}'

# Convertir el string JSON en un diccionario en Python
json_str_a_diccionario = json.loads(json_str)
print(json_str_a_diccionario)
print(type(json_str_a_diccionario))

nombre = json_str_a_diccionario['nombre']
print(nombre)
print()









# Supongamos que tenemos un archivo llamado 'datos.json' con el siguiente contenido:
# {"name": "Ana", "age": 25, "city": "Barcelona"}

# Abrimos el archivo JSON
with open('./03/datos.json', 'r') as f:
    contenido = json.load(f)
    print(contenido)

    for clave in contenido:
        print(clave)

    print(contenido['name'])
    print(contenido['age'])
    print(contenido['city'])
    print()








# Diccionario de Python
data = {'name': 'Carlos', 'age': 28, 'city': 'Sevilla'}

# Convertir un diccionario a un string en formato JSON
json_string = json.dumps(data)
print(json_string)
print(type(json_string))








        

# Diccionario de Python
datos_2 = {'name': 'Luci', 'age': 22, 'city': 'Valencia'}

# Abrir un archivo en modod escritura
with open('./03/datos_2.json', 'w') as f:
    contenido_2 = json.dump(datos_2,f, indent=4)
    print(contenido_2)

# El archivo 'datos_2.json' contendrá el siguiente contenido:
# {"name": "Luci", "age": 22, "city": "Valencia"}