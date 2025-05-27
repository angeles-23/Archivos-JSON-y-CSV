import os 
os.system('cls')
import pandas as pd

df = pd.read_csv('videogames.csv')


'''
1. Carga de datos
'''
# 5 primeras lineas
print(df.head())

# Filas, columnas
filas, columnas = df.shape
# filas = sf.shape[0]       columnas = df.shape[1]
print(filas, columnas)

print('\n')



'''
2. Selección de datos
'''
df_filtrado = df[['title', 'genre', 'total_sales']]
print(df_filtrado)
print('\n')



'''
3. Filtrado por condición
'''
condicion = df[df['console'] == 'PS4']
print(condicion)

condicion_2 = df[df['total_sales'] > 5.00]
print(condicion_2)
print('\n')



'''
4. Filtrado con condiciones combinadas
'''
condicion_doble = df[ (df['console'] == 'PS4') & (df['total_sales'] > 5.00)]
print(condicion_doble)
print('\n')



'''
5. Nueva columna derivada
'''
df['ventas_millones'] = df['total_sales'].round(1)
print(df)

df['es_exitoso'] = df['total_sales'] > 1
print(df)
print('\n')



'''
6. Conteo por categoría
'''
cantidad_generos = df['genre'].value_counts()
print(cantidad_generos)

juegos_consola = df['console'].value_counts()
print(juegos_consola)
print('\n')



'''
7. Ordenación
'''
ordenacion_total_sales = df.sort_values('total_sales', ascending=False)
print(ordenacion_total_sales)

juegos_mas_vendidos_10 = ordenacion_total_sales.head(10)
print(juegos_mas_vendidos_10)
print('\n')


'''
8. Estadísticas rápidas
'''
estadisticas = df['total_sales'].describe()
print(estadisticas)

media = df['total_sales'].mean()
maximo = df['total_sales'].max()
minimo = df['total_sales'].min()

print(media, maximo, minimo)
