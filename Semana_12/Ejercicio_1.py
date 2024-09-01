import sys

class BankAccount:
    balance = 50

    def sacarDinero(self, monto):
        self.balance -= monto    
        print(f"El balance actual es de {self.balance}")


    def ingresarDinero(self, monto): 
        self.balance += monto
        print(f"El balance actual es de {self.balance}")


class SavingsAccount(BankAccount):
    min_balance = 0
        
def main():
    my_bank_account = SavingsAccount()
    menu = 0
    try:
        menu = int(input(f"Bienvenido a mi cuenta de banco, digite la opción que desea realizar:\n1. Retirar Dinero\n2. Ingresar Dinero\n3. Salir\n>>"))
        if menu < 1 or menu > 3:
            raise ValueError("Numero no está dentro de la lista")
    except ValueError as error:
        print(f"El dato ingresado no corresponde a un número dentro del menú, debido a: {error}")
        main()
    if menu == 1:
        try:
            dinero = float(input("Digite el valor a retirar: "))
        except ValueError as error:
            print(f"El numero digitado no es un número")
        if dinero > my_bank_account.balance:
             print("El valor digitado es mayor al actual en su cuenta, favor intente de nuevo.")
             main()
        else:
            my_bank_account.sacarDinero(dinero)
    elif menu == 2:
        try:
            dinero = float(input("Digite el valor a depositar: "))
        except ValueError as error:
            print(f"El numero digitado no es un número")
        my_bank_account.ingresarDinero(dinero)
    elif menu == 3:
        sys.exit()


if __name__ == '__main__':
	main()