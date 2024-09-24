'''
3. Cree una clase de `User` que:
    - Tenga un atributo de `date_of_birth`.
    - Tenga un property de `age`.
    
    Luego cree un decorador para funciones que acepten un `User` 
    como parámetro que se encargue de revisar si el `User` es mayor de edad
      y arroje una excepción de no ser así.
'''

from datetime import date


class User:
    date_of_birth: date
    
    def __init__(self, date_of_birth, age):
        self.date_of_birth = date_of_birth
        self.age = age


    def verify_legal_age(func):
        def wrapper(self, *args):
            if self.age < 18:
                raise ValueError("no es mayor de edad")
            return func(self, *args)
        return wrapper
    
    
    @verify_legal_age
    def drinking(self):
        return "Si estás tomando es por que eres mayor de edad"


tere = User(date(1997, 10, 20), 27)

try:
    print(tere.drinking())
except ValueError as error:
    print(f"Error tere {error}")
    
juan = User(date(2020, 8, 10), 4)

try:
    print(juan.drinking())
except ValueError as error:
    print(f"Error juan {error}")