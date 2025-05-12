import pandas as pd, os
os.system('cls')


df = pd.read_csv('videogames.csv')
df = df[['title', 'genre']]

generos = df.value_counts('genre')

print('Distribución de videojuegos por género:\n')

for i, j in generos.items():  # items() accede al valor de cada juego
    bloques = int(j / 10)* '█'
    print(f'{i.ljust(20)} {bloques} ({j})')
