from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculatePerimeter(self):
        pass

    @abstractmethod
    def calculateArea(self):
        pass


class Circle(Shape):
    def calculatePerimeter(self, radio):
        perimeter = 2 * math.pi * radio
        return perimeter


    def calculateArea(self, radio):
        area = math.pi * (radio ** 2)
        return area


class Square(Shape):
    def calculatePerimeter(self, side):
        perimeter = side * 4
        return perimeter


    def calculateArea(self, side):
        area = side * side
        return area
    

class Rectangle(Shape):
    def calculatePerimeter(self, lenght, width):
        perimeter = (lenght * 2) + (width * 2)
        return perimeter
    

    def calculateArea(self, lenght, width):
        area = lenght * width
        return area
    

circle = Circle()
print(f"El area de un circulo con un radio de 20 es de: {circle.calculateArea(20)}")
print(f"El perimetro de un circulo con un radio de 20 es de: {circle.calculatePerimeter(20)}")

square = Square()
print(f"El area de un cuadrado con un lado de 20 es de: {square.calculateArea(20)}")
print(f"El perimetro de un cuadrado con un lado de 20 es de: {square.calculatePerimeter(20)}")

rectangle = Rectangle()
print(f"El area de un rectangulo con un largo de 20 y un ancho de 30 es de: {rectangle.calculateArea(20, 30)}")
print(f"El perimetro de un rectangulo con un largo de 20 y un ancho de 30 es de: {rectangle.calculatePerimeter(20, 30)}")