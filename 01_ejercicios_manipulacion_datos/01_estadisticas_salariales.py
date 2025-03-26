import json, csv, os
os.system('cls')



def cargar_csv():
    with open("jobs_in_data.csv", "r") as f:
        contenido_csv = csv.DictReader(f)
        lista_csv = list(contenido_csv)

    return lista_csv


def agrupar_por_job_category(lista_csv):
    lista_job_category = []

    for fila in lista_csv:
        job_category = fila["job_category"]

        if job_category not in lista_job_category:
            lista_job_category.append(job_category)

    return lista_job_category


def contar_empleados(lista_csv):
    cantidad_empleados = {}
    contador_empleados = 0

    for empleado in lista_csv:
        categoria_job = empleado["job_category"]

        if categoria_job not in cantidad_empleados:
            contador_empleados = 1
            cantidad_empleados[categoria_job] = contador_empleados
        else:
            contador_empleados += 1
            cantidad_empleados[categoria_job] = contador_empleados

    return cantidad_empleados


def calcular_salario_minimo(lista_csv):
    salarios_minimos = {}
    # salario_minimo = int(lista_csv[0]['salary'])

    # for empleado in lista_csv:
    #     salario = int(empleado['salary'])

    #     if salario < salario_minimo:
    #         salario_minimo = salario

    return salarios_minimos



def calcular_salario_maximo(lista_csv):

    salario_maximo = int(lista_csv[0]['salary'])

    for empleado in lista_csv:
        salario = int(empleado['salary'])

        if salario > salario_maximo:
            salario_maximo = salario

    return salario_maximo


def calcular_salario_medio(lista_csv):
    cantidad_empleados = 0
    salario_total = 0

    for empleado in lista_csv:
        salario = int(empleado['salary'])

        salario_total += salario
        cantidad_empleados += 1

    media_salario = round(salario_total / cantidad_empleados, 2)

    return media_salario


def calcular_rango_salarial(lista_csv):
    salario_minimo = calcular_salario_minimo(lista_csv)
    salario_maximo = calcular_salario_maximo(lista_csv)

    rango_salarial = salario_maximo-salario_minimo

    return rango_salarial


def ordenar_salarios(lista_csv):
    salario_medio = calcular_salario_medio(lista_csv)

    empleados_salario_medio = []

    for empleado in lista_csv:
        salario = int(empleado['salary'])

        if salario < salario_medio:
            empleados_salario_medio.append(empleado)
            
    empleados_salario_medio

    return empleados_salario_medio




if __name__ == '__main__':
    datos_csv = cargar_csv()
    print(agrupar_por_job_category(datos_csv))
    print(contar_empleados(datos_csv))
    print(calcular_salario_minimo(datos_csv))
    print(calcular_salario_maximo(datos_csv))
    print(calcular_salario_medio(datos_csv))
    print(calcular_rango_salarial(datos_csv))
    # print(ordenar_salarios(datos_csv))
