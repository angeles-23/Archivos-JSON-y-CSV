import json, csv, os
os.system('cls')



def cargar_archivo(archivo):

    with open(archivo, newline='', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        lista_csv = list(lector)

    return lista_csv



def agrupar_por_categoria(datos_csv):
    
    categorias = []
    
    for empleado in datos_csv:
        categoria = empleado['job_category']

        if categoria not in categorias:
            categorias.append(categoria)

    return categorias



def contar_empleados_por_categoria(datos_csv):
    categorias = {}

    for empleado in datos_csv:
        categoria = empleado['job_category']

        if categoria not in categorias:
            categorias[categoria] = 1
        else:
            categorias[categoria] += 1
    
    return categorias



def calcular_salarios_minimos(datos_csv):

    salarios_minimos = {}

    for empleado in datos_csv:
        categoria = empleado['job_category']
        salario = int(empleado['salary'])

        if categoria not in salarios_minimos:
            salarios_minimos[categoria] = salario
        else:
            if salarios_minimos[categoria] > salario:
                salarios_minimos[categoria] = salario

    return salarios_minimos



def calcular_salarios_maximos(datos_csv):

    salarios_maximos = {}

    for empleado in datos_csv:
        categoria = empleado['job_category']
        salario = int(empleado['salary'])

        if categoria not in salarios_maximos:
            salarios_maximos[categoria] = salario
        else:
            if salarios_maximos[categoria] < salario:
                salarios_maximos[categoria]= salario

    return salarios_maximos



def calcular_total_salarios(datos_csv):
    total_salarios = {}

    for empleado in datos_csv:
        categoria = empleado['job_category']
        salario = int(empleado['salary'])
        
        if categoria not in total_salarios:
            total_salarios[categoria] = salario
        else:
            total_salarios[categoria] += salario

    return total_salarios



def calcular_media_salarial_por_categorias(datos_csv):

    medias_salariles_por_categorias = {}
    
    total_salarios_categorias = calcular_total_salarios(datos_csv)
    cantidad_empleados_categorias = contar_empleados_por_categoria(datos_csv)

    for categoria in total_salarios_categorias:
    
        for empleado in cantidad_empleados_categorias:
            if categoria == empleado:
                media = total_salarios_categorias[categoria] / cantidad_empleados_categorias[empleado]
                medias_salariles_por_categorias[categoria] = round(media, 2)

    return medias_salariles_por_categorias



def calcular_rango_salarial_categorias(datos_csv):

    rangos_salariales_categorias = {}
    salarios_maximos = calcular_salarios_maximos(datos_csv)
    salarios_minimos = calcular_salarios_minimos(datos_csv)

    for salario_minimo in salarios_minimos:
        for salario_maximo in salarios_maximos:
            if salario_minimo == salario_maximo:
                diferencia_salarial = salarios_maximos[salario_maximo] - salarios_minimos[salario_maximo]
                rangos_salariales_categorias[salario_minimo] = diferencia_salarial

    return rangos_salariales_categorias



def ordenar_salarios_medios_decendentemente(datos_csv):

    medias_salariales_ordenadas_descendentemente = []
    medias_salariales_ordendas_crecientemente = []

    medias_salariales = calcular_media_salarial_por_categorias(datos_csv)
    
    for categoria in medias_salariales:
        media = medias_salariales[categoria]
        medias_salariales_ordendas_crecientemente.append(media)
    
    medias_salariales_ordendas_crecientemente.sort()

    for i in range(len(medias_salariales_ordendas_crecientemente)-1, -1, -1):
        medias_salariales_ordenadas_descendentemente.append(medias_salariales_ordendas_crecientemente[i])
    
    return medias_salariales_ordenadas_descendentemente



def guardar_estadisticas_salarios_en_csv(datos_csv):

    categorias_agrupadas = agrupar_por_categoria(datos_csv)
    total_trabajadores = contar_empleados_por_categoria(datos_csv)
    salarios_maximos = calcular_salarios_maximos(datos_csv)
    salarios_minimos = calcular_salarios_minimos(datos_csv)
    salarios_medios = calcular_media_salarial_por_categorias(datos_csv)
    rangos_salariales = calcular_rango_salarial_categorias(datos_csv)

    with open("./01_estadisticas_salariales/estadisticas_salarios.csv", "w", newline="") as f:
        escritor = csv.writer(f)
        escritor.writerow(["job_category","total_workers", "max_salary" ,"min_salary", "mean_salary", "range_salary"])

        for categoria in categorias_agrupadas:
            escritor.writerow([categoria, total_trabajadores[categoria], salarios_maximos[categoria], salarios_minimos[categoria], salarios_medios[categoria], rangos_salariales[categoria]])
        


def guardar_estadisticas_salarios_en_json(datos_csv):

    categorias_agrupadas = agrupar_por_categoria(datos_csv)
    total_trabajadores = contar_empleados_por_categoria(datos_csv)
    salarios_maximos = calcular_salarios_maximos(datos_csv)
    salarios_minimos = calcular_salarios_minimos(datos_csv)
    salarios_medios = calcular_media_salarial_por_categorias(datos_csv)
    rangos_salariales = calcular_rango_salarial_categorias(datos_csv)

    lista_diccionarios = []
    diccionario_estadisticas = {}

    for categoria in categorias_agrupadas:
        diccionario_estadisticas = {"job_category": categoria, "total_workers": total_trabajadores[categoria], "max_salary": salarios_maximos[categoria], "min_salary": salarios_minimos[categoria], "mean_salary":salarios_medios[categoria], "range_salary": rangos_salariales[categoria]}

        lista_diccionarios.append(diccionario_estadisticas)

    with open("./01_estadisticas_salariales/estadisticas_salarios.json", "w") as f:
        estadisticas = json.dump(lista_diccionarios, f, indent=4)






if __name__ == '__main__':
    archivo = 'jobs_in_data.csv'
    datos_csv = cargar_archivo(archivo)
    # print(agrupar_por_categoria(datos_csv))
    # print(contar_empleados_por_categoria(datos_csv))
    # print(calcular_salarios_minimos(datos_csv))
    # print(calcular_salarios_maximos(datos_csv))
    # print(calcular_total_salarios(datos_csv))
    # print(calcular_media_salarial_por_categorias(datos_csv))
    # print(calcular_rango_salarial_categorias(datos_csv))
    # print(ordenar_salarios_medios_decendentemente(datos_csv))
    guardar_estadisticas_salarios_en_csv(datos_csv)
    guardar_estadisticas_salarios_en_json(datos_csv)
