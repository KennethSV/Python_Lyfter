import re

lista_estudiantes = []
lista_promedios = []
lista_top3 = []

class Estudiante:
    def __init__(self, nombre, seccion, espanol, ingles, sociales, ciencias):
        self.nombre = nombre
        self.seccion = seccion
        self.espanol = espanol
        self.ingles = ingles
        self.sociales = sociales
        self.ciencias = ciencias
    

    def crear_estudiante(self):
        global lista_estudiantes
        seccion_flag = True
        note_flag_espanol = True
        note_flag_ingles = True
        note_flag_sociales = True
        note_flag_ciencias = True
        seccion_pat = re.compile(r'^[0-9]{2}[A-Fa-f]$')
        self.nombre = input("Ingrese el nombre del estudiante: ")
        
        while seccion_flag:
            try:
                self.seccion = input("Ingrese la seccion del estudiante (Formato: 2 numeros y una letra, ej: 12B)\n >> ")
                if re.fullmatch(seccion_pat, self.seccion) == None:
                    raise ValueError("Seccion no Existe")
                else:
                    seccion_flag = False
            except ValueError as error:
                print(f"El dato ingresado no es correcto, debido a: {error}")
        while note_flag_espanol:
            try:
                self.espanol = int(input("Ingrese la nota de Español: "))
                if self.espanol < 0 or self.espanol > 100:
                    raise ValueError("Nota no está dentro del rango posible")
                else:
                    note_flag_espanol = False
            except ValueError as error:
                print(f"El dato ingresado no es correcto, debido a: {error}")
        while note_flag_ingles:
            try:
                self.ingles = int(input("Ingrese la nota de ingles: "))
                if self.ingles < 0 or self.ingles > 100:
                    raise ValueError("Nota no está dentro del rango posible")
                else:
                    note_flag_ingles = False
            except ValueError as error:
                print(f"El dato ingresado no es correcto, debido a: {error}")
        while note_flag_sociales:
            try:
                self.sociales = int(input("Ingrese la nota de sociales: "))
                if self.sociales < 0 or self.sociales > 100:
                    raise ValueError("Nota no está dentro del rango posible")
                else:
                    note_flag_sociales = False
            except ValueError as error:
                print(f"El dato ingresado no es correcto, debido a: {error}")
        while note_flag_ciencias:
            try:
                self.ciencias = int(input("Ingrese la nota de ciencias: "))
                if self.ciencias < 0 or self.ciencias > 100:
                    raise ValueError("Nota no está dentro del rango posible")
                else:
                    note_flag_ciencias = False
            except ValueError as error:
                print(f"El dato ingresado no es correcto, debido a: {error}")
        lista_estudiantes.append(Estudiante(self.nombre, self.seccion, self.espanol, self.ingles, self.sociales, self.ciencias))
        print(f"Estudiante agregado: {self.nombre}")


def calcular_promedio():
    promedio = 0
    global lista_promedios
    lista_promedios = []
    global lista_estudiantes
    for estudiante in lista_estudiantes:
        promedio = (estudiante.espanol + estudiante.ingles + estudiante.sociales + estudiante.ciencias) / 4
        dict_promedio = {
            'Estudiante': estudiante.nombre,
            'Promedio': promedio
            }
        lista_promedios.append(dict_promedio)
    

def calcular_top3():
    
    top1 = {'Promedio': 0}
    top2 = {'Promedio': 0}
    top3 = {'Promedio': 0}
    global lista_promedios
    global lista_top3
    lista_top3 = []
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