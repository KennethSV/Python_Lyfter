import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area =  math.pi * (self.radius ** 2)
        return area


radius = float(input("Digite el valor del radio para calcular el area del circulo: \n>> "))
circle = Circle(radius)
print(circle.get_area())