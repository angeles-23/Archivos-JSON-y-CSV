import pandas as pd, os 
os.system('cls')


df = pd.read_csv('videogames.csv')
df = df[['title', 'console', 'genre', 'total_sales']]


lista_generos = []

for genero in df['genre']:
    if genero not in lista_generos:
        lista_generos.append(genero)
    
genero_input = input('Género: ')


if(genero_input == '' or genero_input not in lista_generos):
    print(f'El género introducido: "{genero_input}" es incorrecto')
else:
    df_filtrado = df [df['genre'] == genero_input].sort_values('total_sales', ascending=False)

    for i, (_, fila) in enumerate(df_filtrado.head().iterrows(), start=1):
        print(f"{i}. {fila['title']} ({fila['total_sales']:.1f}M)")
