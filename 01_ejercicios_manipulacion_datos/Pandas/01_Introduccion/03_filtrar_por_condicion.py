import pandas as pd, os 
os.system('cls')


df = pd.read_csv('videogames.csv')

# Filtra y muestra los videojuegos cuya consola sea PS4.
consola_PS4 = df[df['console'] == 'PS4']
print(consola_PS4)

# Filtra y muestra los juegos que hayan vendido más de 5 millones de unidades.
videojuegos_mas_5_mill = df[df['total_sales'] > 5]
print(videojuegos_mas_5_mill)
