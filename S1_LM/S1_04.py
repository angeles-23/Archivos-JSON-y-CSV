import os, json
os.system('cls')

personas = [ 
    {'nombre':'Carlos', 'edad': 28, 'email':'carlos@gmail.com'}, 
    {'nombre':'Ana', 'edad':  24, 'email':'ana@gmail.com'}, 
    {'nombre':'Luis', 'edad': 29 , 'email':'luis@gmail.com'}
]

with open('personas.json', mode='w', newline='', encoding='utf-8') as f:
    json.dump(personas, f, ensure_ascii=False, indent=4)


with open('personas.json', mode='r', newline='', encoding='utf-8') as f:
    contenido = json.load(f)

    print('Personas registradas:')
    for persona in contenido:
        print(f'- {persona['nombre']}')