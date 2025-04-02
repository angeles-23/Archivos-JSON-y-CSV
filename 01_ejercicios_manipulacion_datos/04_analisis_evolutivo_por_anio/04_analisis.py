import os, json, csv
os.system('cls')



def cargar_csv(archivo_csv):

    with open(archivo_csv, 'r', newline='', encoding='utf-8') as f:
        datos = csv.DictReader(f)
        lista_datos = list(datos)

    return lista_datos


def agrupar_por_anios(lista_datos_csv):

    diccionario_anios = {}
    lista_anios = []

    for empleo in lista_datos_csv:
        anio = int(empleo['work_year'])
        
        if anio not in lista_anios:
            lista_anios.append(anio)


    for dato_lista in lista_anios:
        empleos_por_anio = []

        for linea in lista_datos_csv:
            anio = int(linea['work_year'])

            if dato_lista == anio:
                empleos_por_anio.append(linea)

        diccionario_anios[dato_lista] = empleos_por_anio
        
    return diccionario_anios


def calcular_numero_total_empleos(archivo):

    lista_datos_csv = cargar_csv(archivo)
    cantidad_empleados = {}

    for empleo in lista_datos_csv:
        anio = int(empleo['work_year'])

        if anio not in cantidad_empleados:
            cantidad_empleados[anio] = 1
        else:
            cantidad_empleados[anio] += 1
    
    return cantidad_empleados


def calcular_salario_total_empleos(archivo):

    lista_datos_csv = cargar_csv(archivo)
    salarios_medios = {}

    for empleo in lista_datos_csv:
        salario = int(empleo['salary'])
        anio = int(empleo['work_year'])

        if anio not in salarios_medios:
            salarios_medios[anio] = salario
        else:
            salarios_medios[anio] += salario 
        
    return salarios_medios


def calcular_salario_medio(archivo):

    lista_datos_csv = cargar_csv(archivo)
    cantidades_totales_salario = calcular_salario_total_empleos(lista_datos_csv)
    cantidades_totales_empleos = calcular_numero_total_empleos(lista_datos_csv)

    salarios_medios = {}

    for empleo in cantidades_totales_empleos:
        for salario in cantidades_totales_salario:
            salarios = ...



if __name__ == '__main__':
    archivo_csv = 'jobs_in_data.csv'
    lista_datos_csv = cargar_csv(archivo_csv)
    # print(agrupar_por_anios(lista_datos_csv))
    print(calcular_numero_total_empleos(archivo_csv))
    print(calcular_salario_total_empleos(archivo_csv))
