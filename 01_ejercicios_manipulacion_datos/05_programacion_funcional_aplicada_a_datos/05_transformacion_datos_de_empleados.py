import os
os.system('cls')


def cargar_datos_sin_librerias():
    '''
    Carga los datos manualmente (sin librerías).
    
    '''
    with open('empleados.csv', 'r') as f:
        lineas = f.readlines()
        cabecera = lineas[0].strip().split(',')
        datos = [ dict (zip (cabecera, linea.strip().split(',') ) )   for linea in lineas[1:] ]
        

    return datos



def filtrar_empleados_activos():
    '''
    Filtra los empleados activos.
    '''
    datos = cargar_datos_sin_librerias()
    empleados_activos = list (filter (lambda empleado:empleado['activo'] == 'True', datos) ) 
    return empleados_activos



def aumentar_salario_10_porciento():
    '''
    Aumenta su salario un 10% usando map.
    '''
    datos = cargar_datos_sin_librerias()
    aumentar_salario_10_porciento = (list( map( lambda empleados: int(empleados['salario']) + (int(empleados['salario'])*0.10), datos) ) )
    return aumentar_salario_10_porciento


def mostrar_datos_con_formato():
    '''
    Muestra sus nombres y su nuevo salario en formato:
    ["Eva: 1650.0", "Lara: 1980.0"]
    '''
    empleados_activos = filtrar_empleados_activos()
    salario_aumentado = aumentar_salario_10_porciento()
    empleados_activos_y_salario_aumentado = (list( map( lambda empleado, salario: f'{empleado['nombre']}: {salario}', empleados_activos, salario_aumentado) ) )
    return empleados_activos_y_salario_aumentado
    
    


if __name__ == '__main__':
    print(filtrar_empleados_activos())
    print(aumentar_salario_10_porciento())
    print(mostrar_datos_con_formato())