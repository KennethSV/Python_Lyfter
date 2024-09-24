'''
Cree un decorador que se encargue de revisar si todos los parámetros de la función 
que decore son números, y arroje una excepción de no ser así.
'''

def num_checker(func):
    def wrapper(*args):
        print(f"Los parametros de la funcion: ", func.__name__, "son los siguientes: ", args)
        try:
            for x in args:
                if not isinstance(x, (int, float)):
                    raise ValueError("El parametro ", x, "no es un número")
        except ValueError as error:
            print(error)
    return wrapper


@num_checker
def sumar(num1, num2):
    total = num1 + num2
    return total


@num_checker
def multiplicar(num1, num2, num3):
    total = num1 * num2 * num3
    return total


sumar(1, 3)
multiplicar(5,"a",7)