import pandas as pd 
import os 
os.system('cls')


df = pd.read_csv('videogames.csv')

df = df[['title', 'console', 'genre', 'critic_score', 'total_sales']]

consola = df['console'].value_counts().idxmax()
cantidad_juegos = df['console'].value_counts().max()

juego_mas_vendido = df[ df['console'] == consola].iloc[0]['title']

total_ventas = df[(df['console'] == consola) & (df['title'] == juego_mas_vendido)].iloc[0]['total_sales'].round(1)

genero = df[ (df['console'] == consola)].value_counts('genre', ascending=False).idxmax()

exitosos = len(df[df['total_sales'] > 1])
juegos_totales = len(df['console'])
porcentaje = ((exitosos / juegos_totales)*100).__round__(1)


print('--- INFORME DE VENTAS DE VIDEOJUEGOS ---')
print(f'Consola más popular: {consola} ({cantidad_juegos} juegos)')
print(f'Juego más vendido en {consola}: {juego_mas_vendido} ({total_ventas}M)')
print(f'Género más frecuente en {consola}: {genero}')
print(f'Porcentaje de juegos exitosos: {porcentaje}%')