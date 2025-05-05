import pandas as pd, os 
os.system('cls')

df = pd.read_csv('videogames.csv')

# Muestra los juegos de la consola PS4 que hayan vendido más de 5 millones de unidades totales.
juegos_PS4_y_ventas_mayor_5_mill = df[ (df['console'] == 'PS4') & (df['total_sales'] > 5) ]
print(juegos_PS4_y_ventas_mayor_5_mill)