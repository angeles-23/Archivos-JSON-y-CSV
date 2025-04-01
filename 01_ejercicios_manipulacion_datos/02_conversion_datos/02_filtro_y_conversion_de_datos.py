import json, csv, os
os.system('cls')


def cargar_datos(archivo):

    with open(archivo, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        datos = list(lector)

    return datos



def filtrar_empleos_en_remoto_y_salario_igual_100000(lista_csv):
    # USANDO LAMBDA
    empleos_remotos_con_salario_mayor_100000 = list(filter(lambda e:e['work_setting'] == 'Remote' and int(e['salary']) > 100000, lista_csv))
    return empleos_remotos_con_salario_mayor_100000

    # USANDO BUCLES
    empleos_remotos_con_salario_mayor_100000 = []

    for empleo in lista_csv:
        forma_trabajo = empleo["work_setting"]
        salario = int(empleo['salary'])

        if forma_trabajo == "Remote" and salario > 100000:
            empleos_remotos_con_salario_100000.append(empleo)

    return empleos_remotos_con_salario_mayor_100000



def filtrar_empleos_en_persona_y_tiempo_parcial(lista_csv):
    # USANDO LAMBDA
    empleos_en_persona_a_tiempo_parcial = list(filter(lambda e:e['work_setting'] == 'In-person' and e['employment_type'] == 'Part-time', lista_csv))
    return empleos_en_persona_a_tiempo_parcial

    # USANDO BUCLES
    empleos_en_persona_a_tiempo_parcial = []

    for empleo in lista_csv:
        forma_trabajo = empleo['work_setting']
        timpo_empleo = empleo['employment_type']

        if forma_trabajo == 'In-person' and timpo_empleo == 'Part-time':
            empleos_en_persona_a_tiempo_parcial.append(empleo)
        
    return empleos_en_persona_a_tiempo_parcial        



# Con conversion
def guardar_remoto_salario_alto_csv_y_json(lista_csv):

    empleos_en_remoto_y_salario_mayor_100000 = filtrar_empleos_en_remoto_y_salario_igual_100000(lista_csv)

    with open('./02_conversion_datos/remoto_salario_alto.csv', 'w', newline='', encoding='utf-8') as f:
        campos = lista_csv[0].keys()
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(empleos_en_remoto_y_salario_mayor_100000)


    with open('./02_conversion_datos/remoto_salario_alto.json', 'w', encoding='utf-8') as f:
        json.dump(empleos_en_remoto_y_salario_mayor_100000, f, indent=4)



# Sin conversion
def guardar_remoto_salario_csv_a_json(lista_csv):
    
    conversion_csv_a_json = guardar_remoto_salario_alto_csv_y_json(lista_csv)

    with open('./02_conversion_datos/remoto_salario_alto.json', 'w', encoding='utf-8') as f:
        json.dump(conversion_csv_a_json, f, indent=4)
    


# Con conversion
def guardar_presencial_parcial_csv(lista_csv):

    datos_filtrados = filtrar_empleos_en_persona_y_tiempo_parcial(lista_csv)

    with open('./02_conversion_datos/presencial_parcial.csv', 'w', newline='', encoding='utf-8') as f:
        campos = lista_csv[0].keys()
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(datos_filtrados)


    with open('./02_conversion_datos/presencial_parcial.json', 'w', encoding='utf-8') as f:
        json.dump(datos_filtrados, f, indent=4)



# Sin conversion
def guardar_presencial_parcial_csv_a_json(lista_csv):
    
    conversion_csv_a_json = filtrar_empleos_en_persona_y_tiempo_parcial(lista_csv)

    with open('./02_conversion_datos/presencial_parcial.json', 'w', encoding='utf-8') as f:
        json.dump(conversion_csv_a_json, f, indent=4)




if __name__ == '__main__':
    archivo = 'jobs_in_data.csv'
    datos_cargados = cargar_datos(archivo)

    empleos_en_remoto = filtrar_empleos_en_remoto_y_salario_igual_100000(datos_cargados)
    empleos_en_persona = empleos_en_persona = filtrar_empleos_en_persona_y_tiempo_parcial(datos_cargados)
    
    guardar_remoto_salario_alto_csv_y_json(datos_cargados)    # Con conversión
    ## guardar_remoto_salario_csv_a_json(datos_cargados)        Sin conversión

    guardar_presencial_parcial_csv(datos_cargados)            # Con conversión
    ## guardar_presencial_parcial_csv_a_json(datos_cargados)    Sin conversión
