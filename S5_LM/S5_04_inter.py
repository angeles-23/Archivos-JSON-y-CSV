import pandas as pd
import os
os.system('cls')

df = pd.read_csv('videogames.csv')

df = df[['title', 'genre', 'critic_score', 'total_sales']]

agrupaciones = df.groupby('genre').agg({
    'title':'count',
    'total_sales':'mean',
    'critic_score':'mean'
})

# Renombrar columnas
agrupaciones.columns = ['Juegos', 'Ventas medias', 'Nota media']

# Ordenar por ventas medias
ordenados = agrupaciones.sort_values('Ventas medias', ascending=False)

print('--- COMPARATIVA DE GÉNEROS DE VIDEOJUEGOS ---')
print(f"{'Género'.ljust(25)} {'Juegos'.ljust(10)} {'Ventas medias'.ljust(15)} {'Nota media'.ljust(15)}")
print('-'*65)

for i, fila in ordenados.iterrows():
    print(f"{i.ljust(25)} {str(round(fila['Juegos'])).ljust(10)} {str(round(fila['Ventas medias'], 1)).rjust(5)} M {str(round(fila['Nota media'],1)).rjust(15)}")

