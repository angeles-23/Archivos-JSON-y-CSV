import pandas as pd, os 
os.system('cls')


df = pd.read_csv('videogames.csv')


# Ordena los juegos por total_sales de mayor a menor.
ordenacion = df.sort_values('total_sales', ascending=False)
print(ordenacion)

# Muestra los 10 juegos más vendidos.
primeros_10 = df.head(10)
print(primeros_10)