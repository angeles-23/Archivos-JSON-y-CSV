import json, csv, os
os.system('cls')



def mostrar_menu():
    print('*** MENÚ ***')
    print('1. Añadir nuevo empleo')
    print('2. Actualizar el salario')
    print('3. Eliminar las ofertas')
    print('4. Gurdar en json y csv')
    print('5. Salir')


def leer_datos_csv(archivo):

    with open(archivo, 'r' ,newline='', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        datos = list(lector)
    
    return datos


def solicitar_valores_correctos(archivo):

    while True:
        try:
            anio = int(input('Año [2020-2025]: '))

            if anio >= 2020 and anio < 2026:
                break
            else:
                print('Error. Has introducido un año fuera del rango')

        except Exception:
            print('Error. Has introducido un valor incorrecto.')


    while True:  
        try:
            titulo = input('Titulo: ')
            
            if titulo.isnumeric():
                print('Error. Has introducido un número')
            else:
                break

        except Exception:
            print('Error. Has introducido un dato incorrecto')
        

    while True:
        categoria = input('Categoria: ')

        if categoria.isnumeric():
            print('Error. Has introducido un dato incorrecto.')
        else:
            break
           
        
    while True:
        try:
            salario = int(input('Salario: '))

            if salario < 0:
                print('Error. Has introducido un salario incorrecto')
            else:
                break

        except Exception:
            print('Error. Has introducido un valor incorrecto')


    while True:
        residencia = input('Residencia: ')

        if residencia.isnumeric():
            print('Error. Has introducido un dato incorrecto.')
        else:
            break


    while True:
        experiencia = input('Nivel de experiencia: ')

        if experiencia.isnumeric():
            print('Error. Has introducido un dato incorrecto.')
        else:
            break


    while True:
        tipo_empleo = input('Tipo de empleo: ')

        if tipo_empleo.isnumeric():
            print('Error. Has introducido un dato incorrecto.')
        else:
            break

    
    while True:
        entorno_de_trabajo = input('Entorno de trabajo: ')

        if entorno_de_trabajo.isnumeric():
            print('Error. Has introducido un dato incorrecto.')
        else:
            break


    while True:
        ubicacion_empresa = input('Ubicación de la empresa: ')

        if ubicacion_empresa.isnumeric():
            print('Error. Has introducido un dato incorrecto.')
        else:
            break

    
    while True:
        tamanio_empresa = input('Tamaño de la empresa [S-M-L]: ')

        if tamanio_empresa.isnumeric():
            print('Error. Has introducido un dato incorrecto.')
        else:
            match tamanio_empresa:
                case 'S':
                    break
                case 'M':
                    break
                case 'L':
                    break
                case _:
                    print('Error. Has introducido un valor incorrecto')

    return anio, titulo, categoria, salario, residencia, experiencia, tipo_empleo, entorno_de_trabajo, ubicacion_empresa, tamanio_empresa


def anadir_empleado(archivo, nuevo_diccionario):
    
    with open(archivo, 'a', newline='', encoding='utf-8') as f:
        dato_aniadido = csv.writer(f)
        dato_aniadido.writerow(nuevo_diccionario.values())


def actualizar_salario(archivo, lista_datos_csv):
    
    titulo = input('Título: ')
    anio = int(input('Año: '))

    empleos_buscados = list(filter(lambda e: e['job_title'] == titulo and int(e['work_year']) == anio, lista_datos_csv))

    salario_nuevo = int(input('Nuevo salario: '))

    for dato in empleos_buscados:
        dato['salary'] = salario_nuevo  

    with open(archivo, 'w', newline='', encoding='utf-8') as f:
        campos = lista_datos_csv[0].keys()  
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()  
        escritor.writerows(lista_datos_csv)  
    

def eliminar_por_titulo(archivo, lista_datos_csv):
    titulo_a_encontrar = input('Introduce el titulo: ')

    lista_a_borrar = list ( filter ( lambda e: e['job_title'] == titulo_a_encontrar, lista_datos_csv ) )
    
    for empleo in lista_a_borrar:
        if empleo in lista_datos_csv:
            lista_datos_csv.remove(empleo)
    
    with open(archivo, 'w', newline='', encoding='utf-8') as f:
        campos = lista_datos_csv[0].keys()
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(lista_datos_csv)


def guardar_empleos_actualizados_en_csv_y_json(lista_datos_csv):
    with open('./03_CRUD/empleos_actualizados.csv', 'w', newline='', encoding='utf-8') as f:
        campos = lista_datos_csv[0].keys()
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(lista_datos_csv)

    with open('./03_CRUD/empleos_actualizados.json', 'w', encoding='utf-8') as f:
        json.dump(lista_datos_csv, f, indent=4)






if __name__ == '__main__':
    archivo = 'jobs_in_data.csv'
    lista_datos_csv = leer_datos_csv(archivo)


    while True:
        mostrar_menu()
        opcion = int(input('Introduce una opción: '))

        match opcion:
            case 1:
                anio, titulo, categoria, salario, residencia, experiencia, tipo_empleo, entorno_de_trabajo, ubicacion_empresa, tamanio_empresa = solicitar_valores_correctos(lista_datos_csv)
                nuevo_empleo = {'work_year': anio, 'job_title': titulo, 'job_category':categoria, 'salary':salario, 'employee_residence':residencia, 'experience_level':experiencia, 'employment_type':tipo_empleo, 'work_setting':entorno_de_trabajo, 'company_location':ubicacion_empresa, 'company_size':tamanio_empresa}

                anadir_empleado(archivo, nuevo_empleo)

            case 2:
                actualizar_salario(archivo, lista_datos_csv)

            case 3:
                eliminar_por_titulo(archivo, lista_datos_csv)

            case 4:
                guardar_empleos_actualizados_en_csv_y_json(lista_datos_csv)

            case 5:
                print('Saliendo...')
                break
        print()
        