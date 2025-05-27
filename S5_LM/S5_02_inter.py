import pandas as pd
import os 
os.system('cls')


df = pd.read_csv('videogames.csv')
df = df[['title','console','genre','total_sales']]


genero_input = 'Shooter'  # input('Género: ')

lista_generos = []

for genero in df['genre']:
    if genero not in lista_generos:
        lista_generos.append(genero)


print('\n')
print(f'Top 5 videojuegos del género {genero_input}:')

if genero_input not in lista_generos or genero_input == '':
    print('Género incorrecto')
else:
    genero = df[ df['genre'] == genero_input]
    ordenados = genero.sort_values('total_sales', ascending=False)

    for i,(_, fila) in enumerate(ordenados.iterrows(), start=1):
        if i < 6:
            print(f'{i}. {fila['title']} ({fila['total_sales']:.1f}M)')
        else:
            break




# print('1. Call of Duty: Modern Warfare 3 (15.2M)')
# print('2. Call of Duty: Black Ops II (14.9M)')
# print('3. Call of Duty: Ghosts (13.4M)')

