import pandas as pd, os 
os.system('cls')

df = pd.read_csv('videogames.csv')
df = df[['title', 'console', 'genre', 'total_sales']]


lista_generos = []

for genero in df['genre']:
    if genero not in lista_generos:
        lista_generos.append(genero)


genero_input = input('Género: ')


if genero_input not in lista_generos or genero_input == '':
    print('El género introducido es incorrecto')

else:
    filas = df[ df['genre'] == genero_input].sort_values('total_sales', ascending=False)
    print(f'Top 5 videojuegos del género {genero_input}:')

    for i, (_, fila) in enumerate(filas.iterrows(), start=1):
        if i < 6:
            print(f'{i}. {fila['title']} ({fila['total_sales']:.1f}M)')
        else:
            break
