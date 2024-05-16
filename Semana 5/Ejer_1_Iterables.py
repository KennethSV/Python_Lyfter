'''
1. Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.
    1. Ejemplos:
    2. `first_list = [’Hay’, ‘en’, ‘que’, ‘iteracion’, ‘indices’, ‘muy’]`
    `second_list = [’casos’, 'los’, ‘la’, ‘por’, ‘es’, ‘util’]` ->
    Hay casos
    en los
    que la
    iteracion por
    indice es
    muy util
'''

import itertools

first_list = [
    'Hay',
    'en',
    'que',
    'iteracion',
    'indices',
    'muy',    
]

second_list = [
    'casos',
    'los',
    'la',
    'por',
    'es',
    'util',    
]

for (first_record, second_record) in zip(first_list, second_list):
        print(f"{first_record} {second_record}")