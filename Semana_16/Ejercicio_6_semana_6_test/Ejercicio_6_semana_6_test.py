'''
6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
    1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
    2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”
'''

ejemplo = "python-variable-funcion-computadora-monitor"

def ordenar_texto_por_item(texto):
    lista = sorted(texto.split('-'))
    lista_ordenada = "-".join(str(palabra) for palabra in lista)
    return lista_ordenada
        

print(ordenar_texto_por_item(ejemplo))