'''
💪🏽 **Ejercicios**

Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
1. Suma
2. Resta
3. Multiplicación
4. División
5. Borrar resultado
Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.
Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.
</aside>
'''

num_ini = 0

def sumar():
    global num_ini
    num_sumar = 0
    try:
        num_sumar = float(input(f"Digite un número a agregar: "))
    except ValueError as error:
        print(f"El numero digitado no es un número")
    num_ini = num_ini + num_sumar
    return num_ini


def restar():
    global num_ini
    num_restar = 0
    try:
        num_restar = float(input(f"Digite un número a restar: "))
    except ValueError as error:
        print(f"El numero digitado no es un número")
    num_ini = num_ini - num_restar
    return num_ini


def multiplicar():
    global num_ini
    num_mult = 0
    try:
        num_mult = float(input(f"Digite un número para mulplicar por: "))
    except ValueError as error:
        print(f"El numero digitado no es un número")
    num_ini = num_ini * num_mult
    return num_ini


def dividir():
    global num_ini
    num_div = 0
    try:
        num_div = float(input(f"Digite un número para dividir entre: "))
        num_ini = num_ini / num_div
    except ZeroDivisionError as error:
        print(f"No se puede dividir entre 0, intente de nuevo")
    except ValueError as error:
        print(f"El numero digitado no es un número {error}")
    return num_ini


def desplegar_menu():
    global num_ini
    menu = 0
    try:
        menu = int(input(f"Bienvenido a la calculadora de Python v1.1\nDigite uno de los siguientes valores según su preferencia:\n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Borrar Resultado\nEl valor actual es de: {num_ini}\n"))
        if menu < 1 or menu > 5:
            raise ValueError("Numero no está dentro de la lista")
    except ValueError as error:
        print(f"El dato ingresado no corresponde a un número dentro del menú, debido a: {error}")
    if menu == 1:
        sumar()
        print(f"El número actual es: {num_ini}\n")
        desplegar_menu()
    elif menu == 2:
        restar()
        print(f"El número actual es: {num_ini}\n")
        desplegar_menu()
    elif menu == 3:
        multiplicar()
        print(f"El número actual es: {num_ini}\n")
        desplegar_menu()
    elif menu == 4:
        dividir()
        print(f"El número actual es: {num_ini}\n")
        desplegar_menu()
    else:
        num_ini = 0
        desplegar_menu()                


if __name__ == '__main__':
	desplegar_menu()