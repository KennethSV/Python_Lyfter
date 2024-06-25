'''
1. Investigue cómo leer y escribir archivos `JSON` en Python [aquí](https://www.w3schools.com/python/python_json.asp).
2. Cree un programa que permita agregar un Pokémon nuevo al archivo de arriba.
    1. Debe leer el archivo para importar los Pokémones existentes.
    2. Luego debe pedir la información del Pokémon a agregar.
    3. Finalmente debe guardar el nuevo Pokémon en el archivo.
'''

import json

file_location = 'pokedex.json'

def leer_archivo(path):
    with open(path, "r") as file:
        archivo_json = json.load(file)
    return archivo_json


def crear_nuevo_pokemon(data):
    name_english = input("Enter the English name of the Pokémon: ")
    types = input("Enter the type(s) of the Pokémon (comma separated): ").split(',')
    hp = int(input("Enter the HP value: "))
    attack = int(input("Enter the Attack value: "))
    defense = int(input("Enter the Defense value: "))
    sp_attack = int(input("Enter the Sp. Attack value: "))
    sp_defense = int(input("Enter the Sp. Defense value: "))
    speed = int(input("Enter the Speed value: "))
    new_pokemon = {
        "name": {
            "english": name_english
            },
        "type": types,
        "base": {
            "HP": hp,
            "Attack": attack,
            "Defense": defense,
            "Sp. Attack": sp_attack,
            "Sp. Defense": sp_defense,
            "Speed": speed
            }
    }
    data.append(new_pokemon)
    print(f"Pokemon agregado a la pokedex satisfactoriamente: {new_pokemon}")


def imprimir_nuevo_archivo(path, data):
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)
    

def desplegar_menu():
    menu = 0
    pokedex = leer_archivo(file_location)
    try:
        menu = int(input("Ingrese la opción que desea realizar:\n1. Crear Pokemon\n2. Mostrar lista de Pokemons\n3. Salir e imprimir datos guardados\n"))
        if menu > 3 or menu < 1:
            raise ValueError("Numero ingresado no pertenece a la lista del menu")
    except ValueError as error:
        print(f"El valor ingresado es erroneo ver siguiente codigo de error: {error}")
    if menu == 1:
        crear_nuevo_pokemon(pokedex)
        imprimir_nuevo_archivo(file_location, pokedex)
        desplegar_menu()
    elif menu == 2:
        print(leer_archivo(file_location))
        desplegar_menu()
    elif menu == 3:
        print(f"Lista guardada en: {file_location}")  


if __name__ == '__main__':
	desplegar_menu()