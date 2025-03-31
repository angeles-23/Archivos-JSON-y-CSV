import json, csv, os
os.system('cls')


def cargar_datos(archivo):

    with open(archivo, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        datos = list(lector)

    return datos


def filtrar_empleos_en_remoto_y_salario_igual_100000(lista_csv):

    empleos_remotos_con_salario_100000 = []

    for empleo in lista_csv:
        forma_trabajo = empleo["work_setting"]
        salario = int(empleo['salary'])

        if forma_trabajo == "Remote" and salario == 100000:
            empleos_remotos_con_salario_100000.append(empleo)

    return empleos_remotos_con_salario_100000


def filtrar_empleos_en_persona_y_tiempo_parcial(lista_csv):
    empleos_en_persona_a_tiempo_parcial = []

    for empleo in lista_csv:
        



if __name__ == '__main__':
    archivo = 'jobs_in_data.csv'
    datos_csv = cargar_datos(archivo)
    print(filtrar_empleos_en_remoto_y_salario_igual_100000(datos_csv))

