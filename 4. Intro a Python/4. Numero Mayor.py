'''
Cree un programa que le pida tres números al usuario y muestre el mayor.
'''
num_1 = int(input('Digite un numero\n'))
num_2 = int(input('Digite un numero\n'))
num_3 = int(input('Digite un numero\n'))

if num_1 > num_2 & num_1 > num_3:
    print(f'El numero mayor es {num_1}')
elif num_2 > num_1 & num_2 > num_3:
    print(f'El numero mayor es {num_2}')
else:
    print(f'El numero mayor es {num_3}')