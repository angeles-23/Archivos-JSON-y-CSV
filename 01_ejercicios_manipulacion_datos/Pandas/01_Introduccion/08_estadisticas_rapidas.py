import pandas as pd, os 
os.system('cls')

df = pd.read_csv('videogames.csv')

# Muestra el resumen estadístico del campo total_sales.
resumen_total_sales = df['total_sales'].describe()
print(resumen_total_sales)

# Imprime la media, el máximo y el mínimo de total_sales.
media = df['total_sales'].mean()
maximo = df['total_sales'].max()
minimo = df['total_sales'].min()

print(f'Media:{media} - Minimo:{minimo} - Maximo:{maximo}')
