"""2. Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.
    1. Ejemplos:
    2. `list_a = [’first_name’, ‘last_name’, ‘role’]`
    `list_b = [’Alek’, ‘Castillo’, ‘Software Engineer’]`
    → `{’first_name’: ‘Alek’, ‘last_name’: ‘Castillo’, ‘role’: ‘Software Engineer’}`"""


import itertools

list_a = [
    'firstname',
    'last_name',
    'role'
]

list_b = [
    'Alex',
    'Castillo',
    'Software Engineer'
]

dictionary = {
}

for index_a, index_b in zip(list_a, list_b):
    dictionary[index_a] = index_b

print(dictionary)