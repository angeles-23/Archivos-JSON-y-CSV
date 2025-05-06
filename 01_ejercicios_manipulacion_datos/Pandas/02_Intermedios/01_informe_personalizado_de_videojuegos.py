import pandas as pd, os 
os.system('cls')

df =  pd.read_csv('videogames.csv')

# Cuál es la consola con más videojuegos en el dataset
consola_mas_videojuegos = df['console'].value_counts().idxmax()
# print(consola_mas_videojuegos)

# Cuál es el juego más vendido de esa consola
juego_mas_vendido = df[(df['console'] == consola_mas_videojuegos)].sort_values('total_sales', ascending=False).head(1).iloc[0]['title']
# print(juego_mas_vendido)

# Cuál es el género más frecuente en esa consola
genero_mas_frecuente = df[df['console'] == consola_mas_videojuegos].value_counts()
print(genero_mas_frecuente)

# Qué porcentaje de juegos tienen más de 1 millón de ventas (exitosos)
