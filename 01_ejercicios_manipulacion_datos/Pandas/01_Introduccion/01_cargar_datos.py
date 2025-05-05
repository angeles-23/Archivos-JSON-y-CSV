import pandas as pd
import os
os.system('cls')


# Cargar CSV
df = pd.read_csv('videogames.csv')

# Mostrar 5 primeras líneas
primeras_5_lineas = df.head()
print(primeras_5_lineas)

# Mostrar número de filas y columnas
filas, columnas = df.shape
print(f'Filas: {filas} - Columnas: {columnas}')