import pandas as pd, os 
os.system('cls')

df =  pd.read_csv('videogames.csv')

# Cuál es la consola con más videojuegos en el dataset
consola_mas_videojuegos = df['console'].value_counts().idxmax()
print(consola_mas_videojuegos)

# Cuál es el juego más vendido de esa consola


# Cuál es el género más frecuente en esa consola


# Qué porcentaje de juegos tienen más de 1 millón de ventas (exitosos)
