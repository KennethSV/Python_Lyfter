'''
Cree un programa que me permita ingresar información de n cantidad de videojuegos y los guarde en un archivo csv.
Debe incluir:
Nombre
Género
Desarrollador
Clasificación ESRB

Ejemplo de archivo final:
nombre,genero,desarrollador,clasificacion
Grand Theft Auto IV,Accion,Rockstar Games,M
The Elder Scrolls IV: Oblivion,RPG,Bethesda,M
Tony Hawk's Pro Skater 2,Deportes,Activision,T
'''

import csv

new_file = 'videojuegos.csv'

def generar_lista_videojuegos():
    lista_de_videojuegos = []
    nuevo_videojuegos = {}
    keys = ['Nombre', 'Género', 'Desarrollador', 'Clasificación ESRB']
    return lista_de_videojuegos, keys
    

def escribir_archivo_csv(file_path, data, headers):
  with open(file_path, 'w', encoding='utf-8') as file:
    writer = csv.DictWriter(file, headers)
    writer.writeheader()
    writer.writerows(data)


def desplegar_menu():
   menu = 0
   try:
        menu = int(input("Ingrese la opción que desea realizar:\n1. Ingresar datos de videojuegos\n2. Salir e imprimir datos guardados\n"))
        if menu > 2 or menu < 1:
            raise ValueError("Numero ingresado no pertenece a la lista del menu")
   except ValueError as error:
      print(f"El valor ingresado es erroneo ver siguiente codigo de error: {error}")
   if menu == 1:
      generar_lista_videojuegos()
   else:
      escribir_archivo_csv('videojuegos.csv', generar_lista_videojuegos(), generar_lista_videojuegos())


if __name__ == '__main__':
	desplegar_menu()