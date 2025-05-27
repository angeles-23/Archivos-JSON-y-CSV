import os, json, csv
os.system('cls')


def cargar_csv():
    with open('jobs_in_data.csv', mode='r', newline='', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        datos = list(lector)
    return datos


def añadir_nuevo_empleo():
    años, titulos, categorias, salarios, residencias, niveles, tipos, entornos, localizaciones, tamaños = filtrado_genérico()

    año_introducido = int(input('Año: '))
    titulo_introducido = input('Titulo: ')
    categoria_introducido = input('Categoria: ')
    salario_introducido = int(input('Salario: '))
    residencia_introducido = input('Residencia: ')
    nivel_introducido = input('Nivel experiencia: ')
    tipo_introducido = input('Tipo: ')
    entorno_introducido = input('Entorno: ')
    localizacion_introducido = input('Localizacion: ')
    tamaño_introducido = input('Tamaño: ')

    año_correcto = False
    titulo_correcto = False
    categoria_correcta = False
    salario_correcto = False
    residencia_correcta = False
    nivel_correcto = False
    tipo_correcto = False
    entorno_correcto = False
    localizacion_correcta = False
    tamaño_correcto = False

    for año in años:
        if int(año) == año_introducido:
            año_correcto = True
            break

    for titulo in titulos:
        if titulo == titulo_introducido:
            titulo_correcto = True
            break

    for categoria in categorias:
        if categoria == categoria_introducido:
            categoria_correcta = True
            break
    
    for salario in salarios:
        if int(salario) == salario_introducido:
            salario_correcto = True
            break
    
    for residencia in residencias:
        if residencia == residencia_introducido:
            residencia_correcta = True
            break

    for nivel in niveles:
        if nivel == nivel_introducido:
            nivel_correcto = True
            break

    for tipo in tipos:
        if tipo == tipo_introducido:
            tipo_correcto = True
            break
    
    for entorno in entornos:
        if entorno == entorno_introducido:
            entorno_correcto = True
            break
    
    for localizacion in localizaciones:
        if localizacion == localizacion_introducido:
            localizacion_correcta = True
            break

    for tamaño in tamaños:
        if tamaño == tamaño_introducido:
            tamaño_correcto = True
            break

    datos_correctos = True
    if año_correcto == False:
        print('Año incorrecto')
        datos_correctos = False
    if titulo_correcto == False:
        print('Titulo incorrecto')
        datos_correctos = False
    if categoria_correcta == False:
        print('Categoria incorrecta')
        datos_correctos = False
    if salario_correcto == False:
        print('Salario incorrecto')
    if residencia_correcta == False:
        print('Residencia incorrecta')
        datos_correctos = False
    if nivel_correcto == False:
        print('Nivel incorrecto')
        datos_correctos = False
    if tipo_correcto == False:
        print('Tipo incorrecto')
        datos_correctos = False
    if entorno_correcto == False:
        print('Entorno incorrecto')
        datos_correctos = False
    if localizacion_correcta == False:
        print('Localizacion incorrecta')
        datos_correctos = False
    if tamaño_correcto == False:
        print('Tamaño incorrecto')
        datos_correctos = False
        
    if datos_correctos == True:
        dict_nuevo_empleo = {
            'work_year':año_introducido,
            'job_title':titulo_introducido,
            'job_category':categoria_introducido,
            'salary':salario_introducido,
            'employee_residence':residencia_introducido,
            'experience_level':nivel_introducido,
            'employment_type':tipo_introducido,
            'work_setting':entorno_introducido,
            'company_location':localizacion_introducido,
            'company_size':tamaño_introducido
            }

        datos = cargar_csv()

        with open('jobs_in_data.csv', mode='a', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f)
            escritor.writerow(dict_nuevo_empleo.values())


def filtrado_genérico():
    datos = cargar_csv()

    años = []
    titulos = []
    categorias = []
    salarios = []
    residencias = []
    niveles = []
    tipos = []
    entornos = []
    localizaciones = []
    tamaños = []

    for dato in datos:
        año = dato['work_year']
        titulo = dato['job_title']
        categoria = dato['job_category']
        salario = dato['salary']
        residencia = dato['employee_residence']
        nivel = dato['experience_level']
        tipo = dato['employment_type']
        entorno = dato['work_setting']
        localizacion = dato['company_location']
        tamaño = dato['company_size']

        if año not in años:
            años.append(año)
        
        if titulo not in titulos:
            titulos.append(titulo)
        
        if categoria not in categorias:
            categorias.append(categoria)
        
        if salario not in salarios:
            salarios.append(salario)

        if residencia not in residencias:
            residencias.append(residencia)

        if nivel not in niveles:
            niveles.append(nivel)
        
        if tipo not in tipos:
            tipos.append(tipo)
        
        if entorno not in entornos:
            entornos.append(entorno)
        
        if localizacion not in localizaciones:
            localizaciones.append(localizacion)

        if tamaño not in tamaños:
            tamaños.append(tamaño)
        
    return años, titulos, categorias, salarios, residencias, niveles, tipos, entornos, localizaciones, tamaños


def actualizar_salario():
    datos = cargar_csv()
    titulo = input('Titulo: ')
    año = int(input('Año: '))

    datos_filtrados = list ( filter (  
        lambda empleo:empleo['job_title'] == titulo and int(empleo['work_year']) == año,
        datos
    ))

    salario_nuevo = int(input('Salario nuevo: '))

    for dato in datos_filtrados:
        dato['salary'] = salario_nuevo

    with open('jobs_in_data.csv', mode='w', newline='', encoding='utf-8') as f:
        campos = datos[0].keys()
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(datos)


def eliminar_ofertas():
    datos = cargar_csv()

    titulo = input('Titulo: ')
    lista_nueva = []

    for dato in datos:
        if dato['job_title'] != titulo:
            lista_nueva.append(dato)
    
    with open('jobs_in_data.csv', mode='w', newline='', encoding='utf-8') as f:
        campos = datos[0].keys()
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(lista_nueva)


def guardar_cambios():
    datos = cargar_csv()

    with open('empleos_actualizados.csv', mode='w', newline='', encoding='utf-8') as f:
        campos = datos[0].keys()
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(datos)
    
    with open('empleos_actualizados.json', mode='w', newline='', encoding='utf-8') as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)


def mostrar_menu():
    print('1. Añadir un nuevo empleo')
    print('2. Actualizar el salario')
    print('3. Eliminar todas las ofertas')
    print('4. Guardar_cambios')
    print('5. Salir')



if __name__ == '__main__':
    seguir = True
    while seguir == True:
        try:
            mostrar_menu()
            opcionMenu = int(input('Opción menu: '))

            if opcionMenu > 0 and opcionMenu < 6:
                match opcionMenu:
                    case 1:
                        añadir_nuevo_empleo()
                    case 2:
                        actualizar_salario()
                    case 3:
                        eliminar_ofertas()
                    case 4:
                        guardar_cambios()
                    case 5:
                        print('Saliendo...')
                        seguir = False
                print()
            else:
                print('Error: Fuera del rango establecido[1-6]')

        except ValueError:
            print('Error: Tipo formato')
        except Exception as e:
            print(f'Error: {e}')