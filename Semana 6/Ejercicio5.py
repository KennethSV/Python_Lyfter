'''
5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
    1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”
'''

ejemplo = "I love Nación Sushi"

def calcular_mayusculas_y_minusculas(texto):
    mayusculas = 0
    minusculas = 0
    for index, letra in enumerate(texto):
        if letra.isupper():
            mayusculas += 1
        elif letra.islower():
            minusculas += 1
    return (mayusculas, minusculas)


mayusculas, minusculas = calcular_mayusculas_y_minusculas(ejemplo)
print(f"El numero de mayusculas es de: ", mayusculas, " y el numero de minusculas es de: ", minusculas)