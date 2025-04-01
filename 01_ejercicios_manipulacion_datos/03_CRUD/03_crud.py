import json, csv, os
os.system('cls')


def leer_datos(archivo):

    with open(archivo, newline='', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        datos = list(lector)



def son_datos_correctos():
    ...


def anadir_empleado(datos):
    ...


def actualizar_salario(datos):
    ...


def eliminar_ofertas_especificas(datos):
    ...


def guardar_empleos_actualizados_en_csv_y_json(datos):
    ...


if __name__ == '__main__':
    archivo = 'jobs_in_data.csv'
    datos = leer_datos(archivo)
    leer_datos(datos)