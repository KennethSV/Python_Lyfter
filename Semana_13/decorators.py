""" class User:
    role: str

    def __init__(self, role):
        self.role = role


def admin_only(func):
    def wrapper(user, *args):
        if user.role != "Admin":
            raise ValueError(
                "You are not allowed to run this function. You are not an admin"
            )
        func(user, args)

    return wrapper


@admin_only
def create_product(user, product_name):
    # (lógica para crear producto...)
    print(f"Product {product_name} created!")


@admin_only
def create_product_category(user, product_category_name):
    # (lógica para crear categoria...)
    print(f"Product Category {product_category_name} created!")


@admin_only
def modify_order(user, order_id):
    # (lógica para modificar pedido...)
    print(f"Order {order_id} modified!")

user = User("Admin")
create_product(user, "Hoja de papel") """

""" from datetime import date


class User:
    date_of_birth: date

    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        # Debemos calcular la edad cada vez que la usemos
        # ya que va a variar dependiendo de la fecha actual
        today = date.today()
        return (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )


my_user = User(date(1997, 10, 20))
print(f"Age: {my_user.age}") """

from datetime import datetime

class Person:
   def __init__(self, first_name, last_name):
      self.first_name = first_name
      self.last_name = last_name

class User:
   def __init__(self, email, password, person):
      self.email = email
      self.password = password
      self.person = person

   @classmethod
   def create_user(cls, first_name, last_name, email, password):
      person = Person(first_name, last_name)
      return User(email, password, person)

my_user = User.create_user("Sarah", "Connor", "sconor@gmail.com", "321")
print("User: ", vars(my_user))
print("Person: ", vars(my_user.person))