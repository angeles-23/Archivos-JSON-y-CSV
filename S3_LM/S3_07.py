import os, csv
os.system('cls')

def cargar_csv():
    with open('jobs_in_data.csv', mode='r', newline='', encoding='utf-8') as f:
        datos = list(csv.DictReader(f))
    return datos


def cantidad_niveles(datos):
    niveles = set( map (
        lambda empleo:empleo['experience_level'],
        datos
        ))
    return niveles


from functools import reduce
def cantidad_empleados(datos, niveles):
    array_diccionario = list(map(
        lambda nivel: {
            "nivel":nivel,
            "media": round(
                reduce(                                             
                    # Sumatorio de salario por nivel de categoria
                    lambda acarreo, dato: acarreo + int(dato["salary"]), 
                    list(filter(lambda dato: dato["experience_level"] == nivel, datos)),0
                ) 
                # Dividido entre numero total de trabajadores 
                / len(list(filter(lambda dato: dato["experience_level"] == nivel, datos)))
            ,2) # Numero de decimales
        },
        niveles
    ))
    return array_diccionario

if __name__ == '__main__':
    datos = cargar_csv()
    niveles = cantidad_niveles(datos)
    print(cantidad_empleados(datos, niveles))