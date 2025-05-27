import os, json
os.system('cls')

persona = {'nombre': 'Carlos', 'edad': 28, 'email':'carlos@email.com'}

with open('persona.json', mode='w', newline='', encoding='utf-8') as f:
    json.dump(persona, f, ensure_ascii=False, indent=4)


with open('persona.json', mode='r', newline='', encoding='utf-8') as f:
    contenido_json = json.load(f)
    print(contenido_json)