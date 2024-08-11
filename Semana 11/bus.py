import sys

class Bus:
    def __init__(self, max_passengers, num_passengers):
        self.max_passengers = max_passengers
        self.num_passengers = num_passengers
    
    def add_passenger(self):
        if self.max_passengers <= self.num_passengers:
            print("El bus está lleno")
        else:
            self.num_passengers += 1

    def remove_passenger(self):
        if self.num_passengers <= 0:
            print("The bus is already empty")
        else:
            self.num_passengers -= 1

bus = Bus(20, 19)

def show_menu():
    try:
        menu = int(input("Welcome to the bus, what do you want to do?\n1. Add Passenger\n2. Remove Passenger\n3. Show the number of passengers\n4. Exit Program\n>> "))
        if menu < 1 or menu > 4:
            raise ValueError("\nNumber does not belong to any option of the list")
        elif menu == 1:
            Bus.add_passenger(bus)
            show_menu()
        elif menu == 2:
            Bus.remove_passenger(bus)
            show_menu()
        elif menu == 3:
            print(f"\nThere are {bus.num_passengers} passengers inside the bus\n")
            show_menu()
        elif menu == 4:
            sys.exit()
    except ValueError as error:
        print(f"\nThe value used is not part of the menu, please see the following error code for more information: {error}")
        show_menu()


if __name__ == '__main__':
	show_menu()