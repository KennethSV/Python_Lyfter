'''
Lea sobre el resto de métodos del módulo csv aqui y cree una version alternativa del ejercicio de arriba que guarde el archivo separado por tabulaciones en vez de por comas.
Ejemplo de archivo final:
nombre	genero	desarrollador	clasificacion
Grand Theft Auto IV	Accion	Rockstar Games	M
The Elder Scrolls IV: Oblivion	RPG	Bethesda	M
Tony Hawk's Pro Skater 2	Deportes	Activision	T
'''

import csv

new_file = 'videojuegos.csv'
keys = ['Nombre', 'Género', 'Desarollador', 'Clasificación ESRB']
lista_de_videojuegos = []

def generar_videojuego():
    global lista_de_videojuegos
    nombre = input("Ingrese el nombre del videojuego: ")
    genero = input("Ingrese el género del videojuego: ")
    desarrollador = input("Ingrese el desarrollador del videojuego: ")
    esrb = input("Ingrese la clasificación ESRB del videojuego: ")
    nuevo_videojuego = {
        'Nombre': nombre,
        'Género': genero,
        'Desarollador': desarrollador,
        'Clasificación ESRB': esrb
    }
    lista_de_videojuegos.append(nuevo_videojuego)
    print(f"Videojuego agregado: {nuevo_videojuego}")

def escribir_archivo_csv():
  global keys
  with open(new_file, 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=keys, delimiter='\t')
    writer.writeheader()
    writer.writerows(lista_de_videojuegos)


def desplegar_menu():
   menu = 0
   global new_file
   try:
        menu = int(input("Ingrese la opción que desea realizar:\n1. Ingresar datos de videojuegos\n2. Mostrar lista de videojuegos\n3. Salir e imprimir datos guardados\n"))
        if menu > 3 or menu < 1:
            raise ValueError("Numero ingresado no pertenece a la lista del menu")
   except ValueError as error:
      print(f"El valor ingresado es erroneo ver siguiente codigo de error: {error}")
   if menu == 1:
      generar_videojuego()
      desplegar_menu()
   elif menu == 2:
      for juego in lista_de_videojuegos:
          print(juego)
      desplegar_menu()
   elif menu == 3:
       escribir_archivo_csv()
       print(f"Lista guardada en: {new_file}")  


if __name__ == '__main__':
	desplegar_menu()