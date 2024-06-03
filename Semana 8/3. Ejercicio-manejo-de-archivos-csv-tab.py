menu = 0

try:
    menu = int(input("Ingrese la opción que desea realizar:\n1. Ingresar datos de videojuegos\n2. Salir"))
    if menu > 2 or menu < 1:
        raise ValueError("Numero ingresado no pertenece a la lista del menu")
    if menu == 1:
        print("Yes")
    else:
        print("No")

except ValueError as error:
    print(f"El valor ingresado es erroneo ver siguiente codigo de error: {error}")