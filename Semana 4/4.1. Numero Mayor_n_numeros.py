'''
Cree un programa que le pida n números al usuario y muestre el mayor.
'''

counter = int(input('Cuantos números desea comparar?\n'))
num = int(input('Digite un numero\n'))
greater = 0

while counter > 0:
    if num.isdigit():
        if num > greater:
            greater = num
        else:
            num = int(input('Digite un numero\n'))
        print(counter)
        counter -= 1
    else:
        break
print(f'El número mayor es {greater}')