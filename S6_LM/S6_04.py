import pandas as pd

# 1. Leer el CSV
df = pd.read_csv('pasajeros.csv')

# 2. Agrupar por nombre_pasajero y sumar el peso de las maletas
peso_total = df.groupby('nombre_pasajero')['peso_maleta'].sum().reset_index()

# 3. Crear columna 'exceso' que indique 'Sí' si peso_total > 20, 'No' si no
peso_total['exceso'] = peso_total['peso_maleta'].apply(lambda x: 'Sí' if x > 20 else 'No')

# 4. Renombrar columna para que quede claro
peso_total = peso_total.rename(columns={'peso_maleta': 'peso_total'})

# 5. Ordenar por peso_total descendente
peso_total = peso_total.sort_values(by='peso_total', ascending=False).reset_index(drop=True)

print(peso_total)