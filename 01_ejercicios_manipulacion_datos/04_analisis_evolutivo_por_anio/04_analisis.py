import os, json, csv
os.system('cls')



def cargar_csv():

    with open('jobs_in_data.csv', 'r', newline='', encoding='utf-8') as f:
        datos = csv.DictReader(f)
        lista_datos = list(datos)

    return lista_datos



def conocer_anios():
    cargar_datos = cargar_csv()
    lista_anios = []

    for empleo in cargar_datos:
        anios = int(empleo['work_year'])

        if anios not in lista_anios:
            lista_anios.append(anios)

    return lista_anios



def agrupar_por_anios():

    cargar_datos = cargar_csv()

    diccionario_anios = {}
    lista_anios = []

    for empleo in cargar_datos:
        anio = int(empleo['work_year'])
        
        if anio not in lista_anios:
            lista_anios.append(anio)


    for dato_lista in lista_anios:
        empleos_por_anio = []

        for linea in cargar_datos:
            anio = int(linea['work_year'])

            if dato_lista == anio:
                empleos_por_anio.append(linea)

        diccionario_anios[dato_lista] = empleos_por_anio
        
    return diccionario_anios



def calcular_numero_total_empleos():

    lista_datos_csv = cargar_csv()
    cantidad_empleados = {}

    for empleo in lista_datos_csv:
        anio = int(empleo['work_year'])

        if anio not in cantidad_empleados:
            cantidad_empleados[anio] = 1
        else:
            cantidad_empleados[anio] += 1
    
    return cantidad_empleados



def calcular_salario_total_empleos():

    lista_datos_csv = cargar_csv()
    salarios_medios = {}

    for empleo in lista_datos_csv:
        salario = int(empleo['salary'])
        anio = int(empleo['work_year'])

        if anio not in salarios_medios:
            salarios_medios[anio] = salario
        else:
            salarios_medios[anio] += salario 
        
    return salarios_medios



def calcular_salario_medio():

    cantidades_totales_salarios = calcular_salario_total_empleos()
    cantidades_totales_empleos = calcular_numero_total_empleos()

    salarios_medios = {}

    for salarios in cantidades_totales_salarios:
        for empleos in cantidades_totales_empleos:
            if salarios == empleos:
                salario_medio = cantidades_totales_salarios[salarios] / cantidades_totales_empleos[empleos]
                salarios_medios[salarios] = round(salario_medio, 2)
                
    return salarios_medios



def calcular_distribucion_employment_type():
    cargar_datos = cargar_csv()
    lista_anios = conocer_anios()
    distribuciones_tipo = {}
        
    for empleo in cargar_datos:
        for anios in lista_anios:
            anio_empleo = int(empleo['work_year'])
            tipo_trabajo = empleo['employment_type']

            if anio_empleo == anios:
                if anio_empleo not in distribuciones_tipo:
                    distribuciones_tipo[anio_empleo] = {}
                
                if tipo_trabajo not in distribuciones_tipo[anio_empleo]:
                    distribuciones_tipo[anio_empleo][tipo_trabajo] = 1
                else:
                    distribuciones_tipo[anio_empleo][tipo_trabajo] += 1
            
    return distribuciones_tipo            
    

    
def calcular_dictribucion_work_setting():
    cargar_datos = cargar_csv()
    lista_anios = conocer_anios()
    distribucion_tipos = {}

    for empleo in cargar_datos:
        for anios in lista_anios:

            anio_empleo = int(empleo['work_year'])
            entorno_empleo = empleo['work_setting']

            if anio_empleo == anios:
                if anio_empleo not in distribucion_tipos:
                    distribucion_tipos[anio_empleo] = {}

                if entorno_empleo not in distribucion_tipos[anio_empleo]:
                    distribucion_tipos[anio_empleo][entorno_empleo] = 1
                else:
                    distribucion_tipos[anio_empleo][entorno_empleo] += 1
    
    return distribucion_tipos



def guardar_resultados_csv():

    anios = agrupar_por_anios()
    numero_total_empleos = calcular_numero_total_empleos()
    total_salarios_medios = calcular_salario_medio()

    lista_diccionarios = []
    diccionario_anios = {}

    for anio in anios:
        diccionario_anios = {"anio":anio, "total_empleos": numero_total_empleos[anio], "salario_medio":total_salarios_medios[anio]}
        lista_diccionarios.append(diccionario_anios)
    
    with open('./04_analisis_evolutivo_por_anio/resumen_anual.csv', 'w', newline='', encoding='utf-8') as f:
        campos = {"anio", "total_empleos", "salario_medio"}
        escritor = csv.DictWriter(f, fieldnames=campos)

        escritor.writeheader()
        escritor.writerows(lista_diccionarios)



def guardar_resumen_anual_json():
    
    anios = agrupar_por_anios()
    numero_total_empleos = calcular_numero_total_empleos()
    salarios_medios = calcular_salario_medio()
    tipo_empleo = calcular_distribucion_employment_type()
    entorno_trabajo = calcular_dictribucion_work_setting()

    lista_de_diccionarios = []
    diccionario_resumen_anual = {}

    for anio in anios:
        diccionario_resumen_anual[anio] = {"total_empleos":numero_total_empleos[anio], "salario_medio": salarios_medios[anio], "tipo_empleo": tipo_empleo[anio], "entorno_trabajo": entorno_trabajo[anio]}
        
    lista_de_diccionarios.append(diccionario_resumen_anual)

    with open('./04_analisis_evolutivo_por_anio/resumen_anual.json', 'w', encoding='utf-8') as f:
        json.dump(lista_de_diccionarios, f, indent=4)

    print(diccionario_resumen_anual)





if __name__ == '__main__':
    # print(conocer_anios())
    # print(agrupar_por_anios())
    # print(calcular_numero_total_empleos())
    # print(calcular_salario_total_empleos())
    # print(calcular_salario_medio())
    # print(calcular_distribucion_employment_type())
    # print(calcular_dictribucion_work_setting())
    # guardar_resultados_csv()
    guardar_resumen_anual_json()