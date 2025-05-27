import os, csv
os.system('cls')



def cargar_csv():
    with open('jobs_in_data.csv', mode='r', newline='', encoding='utf-8') as f:
        datos = list(csv.DictReader(f))
    return datos

def filtrar_remote(datos):
    filtrar_remote = list( filter(
        lambda empleo:empleo['work_setting'] == 'Remote',
        datos
    ))
    return filtrar_remote

def excluir_categoria(datos):
    filtrar_categoria = list (filter (
        lambda empleo:empleo['job_category'] != 'Data Science and Research',
        datos
    ))
    return filtrar_categoria


def list_dict(datos):
    europeos = ['Andorra', 'Armenia', 'Austria', 'Belgium', 'Bosnia and Herzegovina', 'Croatia', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Gibraltar', 'Greece', 'Ireland', 'Israel', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Netherlands', 'Poland', 'Portugal', 'Romania', 'Russia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Turkey', 'Ukraine', 'United Kingdom']
    cambio = 1.07
    lista_diccionarios = []
    titulos_añadidos  = set()

    for dato in datos:
        localizacion = dato['company_location']
        salario = float(dato['salary'])
        titulo = dato['job_title']

        if titulo in titulos_añadidos:
            continue

        if localizacion in europeos:
            salario = round(salario / cambio / 1000, 2)
        elif localizacion == 'United States':
            salario = round(salario / 1000, 2)
        else:
            continue

        lista_diccionarios.append({'job_title':titulo, 'salary':salario.__round__(2)})
        titulos_añadidos.add(titulo)
    
    lista_diccionarios = sorted(lista_diccionarios, key=lambda x:x['salary'], reverse=True)[:5]

    return lista_diccionarios

    


if __name__ == '__main__':
    datos = cargar_csv()
    remote = filtrar_remote(datos)
    categoria_excluida = excluir_categoria(remote)
    print(list_dict(categoria_excluida))

