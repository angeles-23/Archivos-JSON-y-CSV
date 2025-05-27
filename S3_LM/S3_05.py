import os, csv
os.system('cls')


def cargar_csv():
    with open('empleados.csv', mode='r', newline='', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        datos = list(lector)
    return datos


def empleados_activos(datos):
    activos = list (filter (
        lambda empleado:empleado['activo'] == 'True',
        datos
    ))
    return activos


def aumento_10(datos):
    aumento = list(map(
        lambda persona: int(persona['salario']) + (int(persona['salario'])*10/100),
        datos
    ))
    return aumento


def mostrar_formato(activos, salarios_nuevos):
    
    formato = list(map(
        lambda persona: f"{persona[0]['nombre']}: {persona[1]}",
        zip(activos, salarios_nuevos)
    ))
    return formato
    


if __name__ == '__main__':
    datos = cargar_csv()
    activos = empleados_activos(datos)
    aumento = aumento_10(activos)
    print(mostrar_formato(activos, aumento))