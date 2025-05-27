import pandas as pd
import os 
os.system('cls')


df = pd.read_csv('videogames.csv')
df = df[['title', 'genre']]

cantidad_generos = df['genre'].value_counts()
# print(cantidad_generos)

print('Distribución de videojuegos por género:\n')

for clave, valor in cantidad_generos.items():
    cantidad = valor / 20
    print(f'{clave.ljust(20)} {"█"*int(cantidad)} ({valor})')