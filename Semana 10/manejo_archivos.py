import re

seccion_flag = True
seccion_pat = re.compile(r'^[0-9]{2}[A-Fa-f]$')

while seccion_flag:
    try:
        seccion = input("Ingrese la seccion del estudiante: ")
        if re.fullmatch(seccion_pat, seccion) == None:
            raise ValueError("Seccion no Existe")
        else: 
                seccion_flag = False
                print('Correcto')
    except ValueError as error:
            print(f"El dato ingresado no es correcto, debido a: {error}")