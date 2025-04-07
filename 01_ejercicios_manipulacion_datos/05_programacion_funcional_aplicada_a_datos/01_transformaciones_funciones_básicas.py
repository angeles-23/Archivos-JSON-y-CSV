import os
os.system('cls')


def encontrar_numeros_mayores_20(numeros):
    '''
    Filtra los números mayores de 20.
    '''
    mayores_20 = list(filter(lambda num:num > 20, numeros))
    return mayores_20


def calcular_mitad_de_numeros_mayores_20(numeros):
    '''
    Devuelve una nueva lista con la mitad de esos números.
    '''
    numeros_mayores_20 = encontrar_numeros_mayores_20(numeros)
    mitad_mayores_20 = list(map(lambda numero: numero/2, numeros_mayores_20))

    # Otra forma de hacerlo (más larga):
    # numeros_mayores_20_2 = list(map(lambda num: num/2, filter(lambda num:num>20, numeros)))

    return mitad_mayores_20


def calcular_el_cuadrado(numeros):
    '''
    Eleva al cuadrado todos los elementos resultantes.
    '''
    mitad_numeros_mayores_20 = calcular_mitad_de_numeros_mayores_20(numeros)
    cuadrado = list(map(lambda numero: numero**2, mitad_numeros_mayores_20))

    # Otra forma de hacerlo (más larga):
    # cuadrado_2 = list(map(lambda num:num**2, map(lambda num:num/2, filter(lambda num:num > 20, numeros))))

    return cuadrado



if __name__ == '__main__':
    numeros = [4, 9, 16, 25, 30, 50, 60]
    print(encontrar_numeros_mayores_20(numeros))
    print(calcular_mitad_de_numeros_mayores_20(numeros))
    print(calcular_el_cuadrado(numeros))