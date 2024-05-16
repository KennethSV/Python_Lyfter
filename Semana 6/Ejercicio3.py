'''
3. Cree una función que retorne la suma de todos los números de una lista.
    1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
    2. [4, 6, 2, 29] → 41
'''

#Primer intento utilizando for


lista = [4, 6, 2, 29]
lista2 = [4, 6, 2, 30]

def sumador_de_listas(listas):
    total = 0
    for suma in listas:
        total = suma + total
    return total


print(sumador_de_listas(lista2))


#Segundo intento descubriendo funciones predefinidas
'''
lista=[4, 6, 2, 29]

def sumador_de_listas(listas):
    return sum(lista)


print(sumador_de_listas(lista))
'''