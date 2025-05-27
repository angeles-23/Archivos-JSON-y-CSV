import os 
os.system('cls')

frutas =  ['Manzana', 'Pera', 'Plátano', 'Fresa', 'Kiwi']

with open('frutas.txt', mode='w', newline='', encoding='utf-8') as f:
    for fruta in frutas:
        f.write(f'{fruta}\n')



with open('frutas.txt', mode='r', newline='', encoding='utf-8') as f:
    contenido = f.readlines()
    
    print(f'Frutas guardadas: {contenido}')