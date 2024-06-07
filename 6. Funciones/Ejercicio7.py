'''
7. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
    1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
    2. Tip 1: Investigue la logica matematica para averiguar si un numero es primo, y conviertala a codigo. No busque el codigo, eso no ayudaria.
    3. *Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). Así que lo mejor es agregar **otra función** para revisar si el numero es primo o no.*
'''

ejemplo_lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def es_primo(numero):
    factores = 0
    primo = False
    if numero == 2:
        primo = True
    elif numero == 3:
        primo = True
    elif numero > 3:
        for index in range(1, numero + 1):
            if numero % index == 0:
                factores += 1
        if factores == 2:
            primo = True
        else:
            primo = False
    return primo


def sacar_primos_en_lista(lista):
    lista_primos = []
    for index, valor in enumerate(lista):
        if es_primo(valor):
            lista_primos.append(valor)
    return lista_primos


print(sacar_primos_en_lista(ejemplo_lista))