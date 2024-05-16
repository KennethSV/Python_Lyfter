'''
Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero
'''
import random

number = int(input('Adivine el numero secreto\n'))
random_number = random.randint(1,10)

while(number != random_number):
    int(input('Error\nDigite un nuevo numero\n'))

print('Lo adivinaste!')