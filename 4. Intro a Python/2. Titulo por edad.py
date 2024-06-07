'''
Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.
'''

edad = int(input('Se desplegará en pantalla su titulo de acuerdo a la edad ingresada\nDigite cúal es su edad?\n'))
if edad >= 65:
    print('Eres un Adulto mayor')
elif edad >= 30:
    print('Eres un Adulto')
elif edad >= 18:
    print('Eres un Adulto Joven')
elif edad >= 13:
    print('Eres un Adolescente')
elif edad >= 11:
    print('Eres un Preadolescente')
elif edad >= 3:
    print('Eres un Niño')
else:
    print('Eres un Bebé')