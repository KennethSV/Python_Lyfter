'''5. Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.
    1. Ejemplos:
    2. 86, 54, 23, 54, 67, 21, 2, 65, 10, 32 → [54, 86, 23, 54, 67, 21, 2, 65, 10, 32]. El más alto fue 86.'''

my_list = [
]
greater = 0
i = 0

while i < 10:
    num = int(input('Digite un numero\n'))
    if num > greater:
        greater = num
    my_list.insert(i, num)
    i += 1
print(f'Usted ingresó los siguientes números: {my_list}. El más alto fue {greater}')