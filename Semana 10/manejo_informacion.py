import re

lista_estudiantes = []
lista_promedios = []
lista_top3 = []

def ingresar_estudiante():
    global lista_estudiantes
    seccion_flag = True
    note_flag_espanol = True
    note_flag_ingles = True
    note_flag_sociales = True
    note_flag_ciencias = True
    seccion_pat = re.compile(r'^[0-9]{2}[A-Fa-f]$')
    nombre = input("Ingrese el nombre del estudiante: ")
    while seccion_flag:
        try:
            seccion = input("Ingrese la seccion del estudiante: ")
            if re.fullmatch(seccion_pat, seccion) == None:
                raise ValueError("Seccion no Existe")
            else: 
                seccion_flag = False
        except ValueError as error:
            print(f"El dato ingresado no es correcto, debido a: {error}")
    while note_flag_espanol:
        try:
            espanol = int(input("Ingrese la nota de Español: "))
            if espanol < 0 or espanol > 100:
                raise ValueError("Nota no está dentro del rango posible")
            else: 
                note_flag_espanol = False
        except ValueError as error:
            print(f"El dato ingresado no es correcto, debido a: {error}")
    while note_flag_ingles:
        try:
            ingles = int(input("Ingrese la nota de ingles: "))
            if ingles < 0 or ingles > 100:
                raise ValueError("Nota no está dentro del rango posible")
            else:
                note_flag_ingles = False
        except ValueError as error:
            print(f"El dato ingresado no es correcto, debido a: {error}")
    while note_flag_sociales:
        try:
            sociales = int(input("Ingrese la nota de sociales: "))
            if sociales < 0 or sociales > 100:
                raise ValueError("Nota no está dentro del rango posible")
            else:
                note_flag_sociales = False
        except ValueError as error:
            print(f"El dato ingresado no es correcto, debido a: {error}")
    while note_flag_ciencias:
        try:
            ciencias = int(input("Ingrese la nota de ciencias: "))
            if ciencias < 0 or ciencias > 100:
                raise ValueError("Nota no está dentro del rango posible")
            else:
                note_flag_ciencias = False
        except ValueError as error:
            print(f"El dato ingresado no es correcto, debido a: {error}")
    nuevo_estudiante = {
        'Nombre completo': nombre,
        'Sección': seccion,
        'Nota de español': espanol,
        'Nota de inglés': ingles,
        'Nota de sociales': sociales,
        'Nota de ciencias': ciencias
    }
    lista_estudiantes.append(nuevo_estudiante)
    print(f"Estudiante agregado: {nombre}")


def calcular_promedios():
    promedio = 0
    global lista_promedios
    global lista_estudiantes
    for estudiante, dict in enumerate(lista_estudiantes):
        for key, value in dict.items():
            if key == 'Nombre completo':
                dict_promedio = {
                    'Estudiante': value
                }
            if key == "Nota de español":
                promedio += value
            elif key == "Nota de inglés":
                promedio += value
            elif key == "Nota de sociales":
                promedio += value
            elif key == "Nota de ciencias":
                promedio += value
        promedio = promedio / 4
        dict_promedio.update({'Promedio': promedio})
        promedio = 0
    lista_promedios.append(dict_promedio)


def calcular_top3():
    top1 = {'Promedio': 0}
    top2 = {'Promedio': 0}
    top3 = {'Promedio': 0}
    global lista_promedios
    global lista_top3
    for estudiante in lista_promedios:
        promedio = estudiante.get('Promedio')
        if promedio > top1['Promedio']:
            top3 = top2
            top2 = top1
            top1 = estudiante
        elif promedio > top2['Promedio']:
            top3 = top2
            top2 = estudiante
        elif promedio > top3['Promedio']:
            top3 = estudiante
    lista_top3 = [top1]
    if top2['Promedio'] > 0:
         lista_top3.append(top2)
    if top3['Promedio'] > 0:
         lista_top3.append(top3)


if __name__ == '__main__':
	ingresar_estudiante(), calcular_promedios(), calcular_top3()