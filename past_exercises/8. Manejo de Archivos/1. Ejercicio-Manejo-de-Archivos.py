'''
1. Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente.
2. Lea sobre el resto de métodos de la clase File de Python [aquí](https://www.w3schools.com/python/python_ref_file.asp) y cree una tabla donde explique qué hace cada uno.
    1. Siga el siguiente formato:
'''

location = "canciones"
new_location = "canciones_ordenado.txt"

def ordenar_archivo(path):
    with open(path, "r") as file:
        ini_lines = file.readlines()
        sorted_list = sorted(ini_lines)
        string_songs = ''.join([str(song) for song in sorted_list])
        return string_songs

def generar_archivo_ordenado():
    with open("canciones_ordenado.txt", 'x') as file:
        file.write(ordenar_archivo(location))
        

generar_archivo_ordenado()