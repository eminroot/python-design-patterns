#Without pattern
import math
from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi *  self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def perimeter(self):
        return 2*(self.width+self.length)

    def area(self):
        return self.width*self.length

class Triangle(Shape):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        self.p = (self.a+self.b+self.c)/2

        return (self.p*(self.p-self.a)*(self.p-self.b)*(self.p-self.c))**0.5

    def perimeter(self):
        return self.a+self.b+self.c

circle = Circle(5)
print(circle.area())

rectangle = Rectangle(2,5)
print(rectangle.area())

triangle = Triangle(6,8,10)
print(triangle.area())