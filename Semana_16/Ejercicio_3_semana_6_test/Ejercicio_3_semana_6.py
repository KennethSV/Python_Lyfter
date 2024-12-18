'''
3. Cree una función que retorne la suma de todos los números de una lista.
    1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
    2. [4, 6, 2, 29] → 41
'''

#Primer intento utilizando for

def sumador_de_listas(listas):
    if not isinstance(listas, list):
        raise TypeError
    if not all(isinstance(x, int) for x in listas):
        raise ValueError
    total = 0
    for suma in listas:
        total += suma
    return total

#Segundo intento descubriendo funciones predefinidas
'''
lista=[4, 6, 2, 29]

def sumador_de_listas(listas):
    return sum(lista)


print(sumador_de_listas(lista))
'''