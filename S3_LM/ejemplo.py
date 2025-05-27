'''
el reduce no es una lista, se colocan 3 argumentos
en caso de elegir ciertos argumentos para enseñar despues del lambda x: {}, datos

archivos csv da cadenas de texto:
    - transformaciones a cada valor correcto
    - quitar caracteres de un valor 150€: 
        valor = '150€'
        if valor.endswith('€')
            valor = valor[-1:]
        valor = round(float(valor), 2)

        valor = '$150'
        if valor.startswith('$')
            valor = valor[1:]
        
        valor = round(float(valor), 2)

        como pasar de:
            valor = '$150' -> 150.00
            valor = '150€' -> 150.00

1. Tipo test:10-15min                                   (1 pto)
2. Scripts programacion funcional: 1, 2: 55-80 min      (3, 2 pto = 5)
3. Pandas 1,2,3                                         (4 pto)
'''

import pandas as pd

# Leer CSV
df = pd.read_csv('precios.csv')

# Función para limpiar y convertir precio
def limpiar_precio(valor):
    valor = str(valor).strip()
    if valor.startswith('$'):
        valor = valor[1:]          # Quita '$' al inicio
    if valor.endswith('€'):
        valor = valor[:-1]         # Quita '€' al final
    return round(float(valor), 2)  # Convierte a float y redondea

# Aplicar función a la columna 'precio'
df['precio_limpio'] = df['precio'].map(limpiar_precio)

print(df)
'''
     producto   precio  precio_limpio
0  Producto A     $150         150.00
1  Producto B     150€         150.00
2  Producto C   $200.5         200.50
3  Producto D  300.75€         300.75
'''