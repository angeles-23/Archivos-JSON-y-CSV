import pandas as pd, os 
os.system('cls')

df = pd.read_csv('videogames.csv')

# Columnas a mostrar
columnas = df[['title', 'genre', 'total_sales']]
print(columnas)