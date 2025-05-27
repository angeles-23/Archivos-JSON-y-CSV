import os, json, csv
os.system('cls')


def cargar_csv():
    with open('jobs_in_data.csv', mode='r', newline='', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        datos = list(lector)
    return datos

def agrupar_categorias():
    datos = cargar_csv()
    lista_categorias = []
    for linea in datos:
        categoria = linea['job_category']
        if categoria not in lista_categorias:
            lista_categorias.append(categoria)

    return lista_categorias

def numero_total_empleos():
    datos = cargar_csv()
    dict_total_empleos = {}

    for linea in datos:
        categoria = linea['job_category']

        if categoria not in dict_total_empleos:
            dict_total_empleos[categoria] = 1
        else:
            dict_total_empleos[categoria] += 1
        
    return dict_total_empleos

def calcular_minimo():
    datos = cargar_csv()

    dict_minimo_sueldo = {}
    salario_minimo = 1_000_000_000
    
    for linea in datos:
        categoria = linea['job_category']
        salario = int(linea['salary'])

        if categoria not in dict_minimo_sueldo:
            dict_minimo_sueldo[categoria] = salario
        else:
            if salario < dict_minimo_sueldo[categoria]:
                salario_minimo = salario
                dict_minimo_sueldo[categoria] = salario_minimo
            
    return dict_minimo_sueldo

def calcular_maximo():
    datos_csv = cargar_csv()

    dict_salarios_maximos = {}

    for linea in datos_csv:
        categoria = linea['job_category']
        salario = int(linea['salary'])
        
        if(categoria not in dict_salarios_maximos):
            dict_salarios_maximos[categoria] = salario
        else:
            if salario > dict_salarios_maximos[categoria]:
                dict_salarios_maximos[categoria] = salario

    return dict_salarios_maximos

def calcular_medio():
    datos = cargar_csv()

    dict_salarios_sumas = {}
    dict_salarios_medios = {}
    # Suma todos los salarios / numero total de salarios
    salario_total = 0
    numero_empleos = numero_total_empleos()
    salario_medio = 0

    for linea in datos:
        categoria = linea['job_category']
        salario = int(linea['salary'])

        if categoria not in dict_salarios_sumas:
            dict_salarios_sumas[categoria] = salario
        else:
            dict_salarios_sumas[categoria] +=  salario
    
    for categoria in dict_salarios_sumas:
        media = dict_salarios_sumas[categoria] / numero_empleos[categoria]
        dict_salarios_medios[categoria] = (media).__round__(2)
        
    return dict_salarios_medios

def calcular_rango_salarial():
    dict_rangos = {}
    maximos = calcular_maximo()
    minimos = calcular_minimo()

    for categoria in maximos:
        dict_rangos[categoria] = maximos[categoria] - minimos[categoria]
        
    return dict_rangos

def ordenar_salarios_descendientemente():
    dict_salarios_desc = {}
    salarios_medios = calcular_medio()

    lista_ordenada = sorted( salarios_medios.items(), key=lambda x:x[1], reverse=True )

    for categoria, salario in lista_ordenada:
        dict_salarios_desc[categoria] = salario

    return dict_salarios_desc

def guardar_en_csv_y_json():
    categorias = agrupar_categorias()
    total_trabajadores = numero_total_empleos()
    maximo_salario = calcular_maximo()
    minimo_salario = calcular_minimo()
    media_salario = calcular_medio()
    rango_salarial = calcular_rango_salarial()

    
    with open('estadisticas_salarios.csv', mode='w', newline='', encoding='utf-8') as f:
        campos = (['job_category','total_workers', 'max_salary' ,'min_salary', 'mean_salary', 'range_salary'])
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        
        for categoria in categorias:
            escritor.writerow(
                {
                    'job_category':categoria, 
                    'total_workers':total_trabajadores[categoria], 
                    'max_salary':maximo_salario[categoria], 
                    'min_salary':minimo_salario[categoria], 
                    'mean_salary':media_salario[categoria], 
                    'range_salary':rango_salarial[categoria]
                }
            )


    with open('estadisticas_salarios.json', mode='w', newline='', encoding='utf-8') as f:
        lista_estadisticas = []
        for categoria in categorias:
            lista_estadisticas.append(
                {
                    'job_category':categoria,
                    'total_workers':total_trabajadores[categoria], 
                    'max_salary':maximo_salario[categoria], 
                    'min_salary':minimo_salario[categoria], 
                    'mean_salary':media_salario[categoria], 
                    'range_salary':rango_salarial[categoria]
                    }
                )

        json.dump(lista_estadisticas, f, ensure_ascii=False, indent=4)
            




if __name__ == '__main__':
    # categorias = print(agrupar_categorias())
    # print(numero_total_empleos())
    # print(calcular_minimo())
    # print(calcular_maximo())
    # print(calcular_medio())
    # print(calcular_rango_salarial())
    # print(ordenar_salarios_descendientemente())
    guardar_en_csv_y_json()
