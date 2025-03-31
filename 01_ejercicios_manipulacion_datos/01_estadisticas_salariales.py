import json, csv, os
os.system('cls')



def cargar_csv():
    with open("jobs_in_data.csv", newline='', encoding='utf-8') as f:
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

    for empleado in lista_csv:
        categoria_job = empleado["job_category"]

        if categoria_job not in cantidad_empleados:
            cantidad_empleados[categoria_job] = 1
        else:
            cantidad_empleados[categoria_job] += 1

    return cantidad_empleados


def calcular_salario_minimo(lista_csv):
    salarios_minimos = {}

    for empleado in lista_csv:
        categoria = empleado['job_category']
        salario = int(empleado['salary'])

        if categoria not in salarios_minimos:
            salarios_minimos[categoria] = salario
        else:
            if salarios_minimos[categoria] > salario:
                salarios_minimos[categoria] = salario

    return salarios_minimos


def calcular_salario_maximo(lista_csv):

    salarios_maximos = {}

    for empleado in lista_csv:
        categoria = empleado['job_category']
        salario = int(empleado['salary'])

        if categoria not in salarios_maximos:
            salarios_maximos[categoria] = salario
        else:
            if salarios_maximos[categoria] < salario:
                salarios_maximos[categoria] = salario

    return salarios_maximos


def calcular_salario_medio(lista_csv):

    salarios_medios = {}
    cantidad_empleados = contar_empleados(lista_csv)
    cantidad_salarios = calcular_salario_total_categorias(lista_csv)

    for categoria in cantidad_salarios:

        if categoria in cantidad_empleados:
            total_salarios = cantidad_salarios[categoria]
            empleados_categoria = cantidad_empleados[categoria]

            if empleados_categoria > 0:
                salario_medio = total_salarios / empleados_categoria
                salarios_medios[categoria] = salario_medio
            else:
                salarios_medios[categoria] = 0
        
        else:
            salarios_medios[categoria] = 0

    return salarios_medios


def calcular_salario_total_categorias(lista_csv):

    salarios_totales = {}

    for empleado in lista_csv:
        categoria = empleado['job_category']
        salario = int(empleado['salary'])

        if categoria not in salarios_totales:
            salarios_totales[categoria] = salario
        else:
            salarios_totales[categoria] += salario

    return salarios_totales


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
    # print(agrupar_por_job_category(datos_csv))
    # print(contar_empleados(datos_csv))
    # print(calcular_salario_minimo(datos_csv))
    # print(calcular_salario_maximo(datos_csv))
    #print(calcular_salario_total_categorias(datos_csv))
    print(calcular_salario_medio(datos_csv))
    # print(calcular_rango_salarial(datos_csv))
    # print(ordenar_salarios(datos_csv))
