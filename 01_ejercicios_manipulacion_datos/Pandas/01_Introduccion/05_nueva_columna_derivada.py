import pandas as pd, os 
os.system('cls')

df = pd.read_csv('videogames.csv')

# Añade una nueva columna llamada ventas_millones que redondee total_sales a 1 decimal.
df['ventas_millones'] = df['total_sales'].round(1)
print(df)

# Añade una columna llamada es_exitoso que valga True si total_sales es mayor que 1.
df['es_exitoso'] = df['total_sales'] > 1
print(df)