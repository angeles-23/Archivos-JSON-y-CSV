import pandas as pd, os
os.system('cls')


df = pd.read_csv('videogames.csv')

# Cuál es la consola con más videojuegos en el dataset
consola_con_mas_videojuegos = df.value_counts('console').idxmax()
cantidad_videojuegos = df.value_counts('console').max()

# Cuál es el juego más vendido de esa consola
juego_mas_vendido = df[df['console'] == consola_con_mas_videojuegos].sort_values('total_sales', ascending=False).head(1).iloc[0]['title']
cantidad_ventas = df[(df['console'] == consola_con_mas_videojuegos) & (df['title'] == juego_mas_vendido)].sum().iloc[5].round(1)

# Cuál es el género más frecuente en esa consola
genero_mas_frecuente = df[ df['console'] == consola_con_mas_videojuegos].value_counts('genre').idxmax()

# Qué porcentaje de juegos tienen más de 1 millón de ventas (exitosos)
cantidad_videojuegos_total = len(df)
cantidad_juegos_exitosos = len(df[ df['total_sales'] > 1])
porcentaje_final = ((cantidad_juegos_exitosos / cantidad_videojuegos_total) * 100).__round__(1)

''' Porcentaje de ventas de X360'''
# cantidad_ventas_mayor_a_1_mill = len(df [(df['console'] == consola_con_mas_videojuegos) & (df['total_sales']>=1)])
# porcentaje = ((cantidad_ventas_mayor_a_1_mill/cantidad_videojuegos)*100).round(1)



print(f'--- INFORME DE VENTAS DE VIDEOJUEGOS ---')
print(f'Consola más popular: {consola_con_mas_videojuegos} ({cantidad_videojuegos} juegos)')
print(f'Juego más vendido en {consola_con_mas_videojuegos}: "{juego_mas_vendido}" ({cantidad_ventas}M)')
print(f'Género más frecuente en {consola_con_mas_videojuegos}: {genero_mas_frecuente}')
print(f'Porcentaje de juegos exitosos: {porcentaje_final}%')
