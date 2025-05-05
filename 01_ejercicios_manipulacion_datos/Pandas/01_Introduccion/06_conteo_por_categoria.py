import os, pandas as pd, os
os.system('cls')

df = pd.read_csv('videogames.csv')

# Muestra cuántos juegos hay de cada género (genre).
cantidad_juegos_genre = df['genre'].value_counts()
print(cantidad_juegos_genre)

# Muestra cuántos juegos hay por cada consola (console).
cantidad_juegos_consola = df['console'].value_counts()
print(cantidad_juegos_consola)