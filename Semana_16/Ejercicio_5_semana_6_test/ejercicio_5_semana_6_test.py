def calcular_mayusculas_y_minusculas(texto):
    if not isinstance(texto, str):
        raise TypeError
    mayusculas = 0
    minusculas = 0
    for index, letra in enumerate(texto):
        if letra.isupper():
            mayusculas += 1
        elif letra.islower():
            minusculas += 1
    return (mayusculas, minusculas)