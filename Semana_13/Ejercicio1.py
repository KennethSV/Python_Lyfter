'''
Cree un decorador que haga print de los parámetros y 
retorno de la función que decore.
'''
def imprimirfuncion(func):
    def wrapper(*args):
        print(f"Los parametros de la funcion: ", func.__name__, "son los siguientes: ", args)
        result = func(*args)
        print(f"El resultado es de: ", result)
        return result
    return wrapper


@imprimirfuncion
def sumar(num1, num2):
    total = num1 + num2
    return total


@imprimirfuncion
def multiplicar(num1, num2, num3):
    total = num1 * num2 * num3
    return total


sumar(1, 3)
multiplicar(5,6,7)