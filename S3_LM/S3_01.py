import os
os.system('cls')

def filtar_mayores_20(numeros):
    mayores_20 = list ( filter ( 
        lambda numero: numero > 20,
        numeros
    ))
    return mayores_20

def mitad_numeros(mayores_20):
    mitad_20 = list( map (
        lambda numero: numero/2,
        mayores_20
    ))
    return mitad_20


def elevar_al_cuadrado(mitad_numeros):
    cuadrados = list( map ( 
        lambda numero: numero**2,
        mitad_numeros
    ))
    return cuadrados



if __name__ == '__main__':
    numeros = [4, 9, 16, 25, 30, 50, 60]
    mayores_20 = filtar_mayores_20(numeros)
    mitad_20 = mitad_numeros(mayores_20)
    cuadrados = elevar_al_cuadrado(mitad_20)