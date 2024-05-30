'''
1. Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente.
2. Lea sobre el resto de métodos de la clase File de Python [aquí](https://www.w3schools.com/python/python_ref_file.asp) y cree una tabla donde explique qué hace cada uno.
    1. Siga el siguiente formato:
'''

def ordenar_archivo(path):
    with open(path, "r") as file1:
        ini_lines = file1.readlines()
        sorted_list = sorted(ini_lines)
        return sorted_list


def crear_archivo_ordenado():
    print(ordenar_archivo("canciones"))


crear_archivo_ordenado()