import pandas as pd, os 
os.system('cls')


df = pd.read_csv('videogames.csv')
df = df[['title', 'genre', 'critic_score', 'total_sales']]

generos_agrupados = df.groupby(['genre']).agg(
    cantidad_juegos = ('title', 'count'),
    media_ventas = ('total_sales', 'mean'),
    media_nota_critica = ('critic_score', 'mean')
)


# generos_agrupados_mayores_5_juegos = generos_agrupados[cantidad_juegos >= 5]
# print(generos_agrupados_mayores_5_juegos)
# print(generos_agrupados.sort_values('media_ventas', ascending=False))  # Entre comillas la variable media_ventas


# print('--- COMPARATIVA DE GÉNEROS DE VIDEOJUEGOS ---\n')
# print(f'{'Género'.ljust(20)} {'Juegos'.ljust(20)} {'Ventas medias'.ljust(20)} {'Nota media'.ljust(20)}')
# print('-'*75)
