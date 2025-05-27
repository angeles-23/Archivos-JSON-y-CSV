import os, json, csv
os.system('cls')



def cargar_csv():
    with open('jobs_in_data.csv', mode='r', newline='', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        datos = list(lector)
    return datos


def filtrar_empleos():
    datos = cargar_csv()

    empleos_filtrados = list( filter ( 
        lambda empleo:empleo['work_setting'] == 'Remote' and int(empleo['salary']) < 100_000, 
        datos 
        ) )
    return empleos_filtrados


def guardar_csv_y_json():
    datos_csv = cargar_csv()
    empleos_filtrados = filtrar_empleos()

    with open('remoto_salario_alto.csv', mode='w', newline='', encoding='utf-8') as f:
        campos = datos_csv[0].keys()
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(empleos_filtrados)

    with open('remoto_salario_alto.json', mode='w', newline='', encoding='utf-8') as f:
        json.dump(empleos_filtrados, f, ensure_ascii=False, indent=4)


def filtrar_empleos_2():
    datos_csv = cargar_csv()

    datos_filtrados = list( filter ( 
        lambda empleo: empleo['work_setting'] == 'In-person' and empleo['employment_type'] == 'Part-time', 
        datos_csv
    ) )

    return datos_filtrados


def guardar_json_csv():
    datos = cargar_csv()
    datos_filtrados = filtrar_empleos_2()

    with open('presencial_parcial.json', mode='w', newline='', encoding='utf-8') as f:
        json.dump(datos_filtrados, f, ensure_ascii=False, indent=4)

    with open('presencia_parcial.csv', mode='w', newline='', encoding='utf-8') as f:
        campos = datos[0].keys()
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(datos_filtrados)


if __name__ == '__main__':
    guardar_csv_y_json()
    guardar_json_csv()