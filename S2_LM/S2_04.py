import os, csv, json
os.system('cls')

def cargar_csv():
    with open('jobs_in_data.csv', mode='r', newline='', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        datos = list(lector)
    return datos


def agrupar_por_año():
    datos = cargar_csv()
    años = {}

    for empleo in datos:
        año = int(empleo['work_year'])

        if año not in años:
            años[año] = [empleo]
        else:
            años[año].append(empleo)

    return años


def buscar_numero_total_empleos():
    años_agrupados = agrupar_por_año()
    cantidad_por_año = {}

    for año in años_agrupados:
        cantidad = len(años_agrupados[año])
        cantidad_por_año[año] = cantidad

    return cantidad_por_año


def salario_medio():
    datos = cargar_csv()
    dict_salario = {}
    dict_salario_medio = {}

    for empleo in datos:
        salario = int(empleo['salary'])
        año = int(empleo['work_year'])
        
        if año not in dict_salario:
            dict_salario[año] = salario
        else:
            dict_salario[año] += salario

    total_empleos = buscar_numero_total_empleos()

    for empleo in total_empleos:
        for salario in dict_salario:
            if empleo == salario:
                salario_medio = dict_salario[salario] / total_empleos[empleo]
                dict_salario_medio[salario] = salario_medio.__round__(2)

    return dict_salario_medio


def frecuencia_tipo():
    datos = cargar_csv()
    dict_frecuencia = {}

    for empleo in datos:
        año = int(empleo['work_year'])
        tipo = empleo['employment_type']
        
        if año not in dict_frecuencia:
            dict_frecuencia[año] = {}
        
        if tipo not in dict_frecuencia[año]:
            dict_frecuencia[año][tipo] = 1
        else:
            dict_frecuencia[año][tipo] += 1

    return dict_frecuencia


def mostrar_distribucion():
    dict_work_setting = {}
    datos = cargar_csv()

    for empleo in  datos:
        año = int(empleo['work_year'])
        tipo = empleo['work_setting']

        if año not in dict_work_setting:
            dict_work_setting[año] = {}
        
        if tipo not in dict_work_setting[año]:
            dict_work_setting[año][tipo] = 1
        else:
            dict_work_setting[año][tipo] += 1
        
    return dict_work_setting

    
def exportar_archivos():

    años = agrupar_por_año()
    total_empleos = buscar_numero_total_empleos()
    salarios_medios = salario_medio()

    frecuencia_por_tipo = frecuencia_tipo()
    distribucion = mostrar_distribucion()

    lista_dict = []
    dict_años = {}

    for año in años:
        dict_años = {'año':año, 'total_empleos':total_empleos[año], 'salario_medio':salarios_medios[año]}
        lista_dict.append(dict_años)


    with open('resumen_anual.csv', mode='w', newline='', encoding='utf-8') as f:
        campos = ['año','total_empleos', 'salario_medio']
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(lista_dict)
        
        
def resumen_anual_completo():

    años = agrupar_por_año()
    total_empleos = buscar_numero_total_empleos()
    salarios = salario_medio()
    frecuencias = frecuencia_tipo()
    distribuciones = mostrar_distribucion()

    list_dict = []
    dict_años = {}

    for año in años:
        dict_años[año] = {'año':año, 'total_empleos':total_empleos[año], 'salario':salarios[año], 'frecuencia':frecuencias[año], 'distribuciones':distribuciones[año]}
        list_dict.append(dict_años[año])

    with open('resumen_anual.json', mode='w', newline='', encoding='utf-8') as f:
        json.dump(list_dict, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    # print(agrupar_por_año())
    # print(buscar_numero_total_empleos())
    # print(salario_medio())
    # print(frecuencia_tipo())
    # print(mostrar_distribucion())
    # exportar_archivos()
    resumen_anual_completo()