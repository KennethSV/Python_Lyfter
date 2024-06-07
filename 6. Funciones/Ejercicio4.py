'''
4. Cree una función que le de la vuelta a un string y lo retorne.
    1. Esto ya lo hicimos en iterables.
    2. “Hola mundo” → “odnum aloH”
'''

ejemplo = "Hola Mundo"

def invertir_texto(texto):
    palabra_invertida = ""
    for letra in range(len(texto)-1,-1,-1):
        palabra_invertida = palabra_invertida + texto[letra]
    return palabra_invertida        
        

print(invertir_texto(ejemplo))