import os, csv
os.system('cls')
from functools import reduce
import  pandas as pd 

df = pd.read_csv('pasajeros.csv')

# Agrupar por 'avion_id' y obtener el índice del peso máximo
id_peso_maximo = df.groupby('avion_id')['peso_maleta'].idxmax()


# Seleccionar las filas con esos índices
resultado = df.loc[id_peso_maximo, ['avion_id', 'modelo', 'nombre_pasajero', 'peso_maleta']]

#  Opcional: resetear el índice para que quede limpio
resultado = resultado.reset_index(drop=True)
print(resultado)
