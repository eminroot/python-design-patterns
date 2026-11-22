#Without the factory pattern

###
# I decided to write this using the factory pattern because of some factors:
#1. If you want to add let's say triangle, you would need to write if/else blocks to carry out your intentions
#but if we use the factory design, you could add additional functionality without changing the existing code
#A class, program should be open for extension but closed for modification(Open/Closed principle of SOLID)
#There are some other reasosn but the aforementioned factor is one of the most primrary ones.


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


#Printing the results for demonstrational purposes.
circle = Circle(5)
print(circle.area())

rectangle = Rectangle(2,5)
print(rectangle.area())

triangle = Triangle(6,8,10)
print(triangle.area())





#With factory pattern



#############################







import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self): 
        pass
    
    @abstractmethod
    def perimeter(self): 
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self): 
        return math.pi * self.radius ** 2
    def perimeter(self): 
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self): 
        return self.length * self.width
    def perimeter(self): 
        return 2 * (self.length + self.width)

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type, *args):
        shapes = {
            "circle": Circle,
            "rectangle": Rectangle
        }
        shape_class = shapes.get(shape_type.lower())
        if shape_class:
            return shape_class(*args)
        raise ValueError(f"Unknown shape type: {shape_type}")

class ShapeCalculator:
    def print_shape_info(self, shape: Shape):
        print(f"--- {type(shape).__name__} ---")
        print(f"Area: {shape.area():.2f}")
        print(f"Perimeter: {shape.perimeter():.2f}")

#Printing the results for demonstrational purposes.
calc = ShapeCalculator()
factory = ShapeFactory()

circle = factory.create_shape("circle", 25)
rectangle = factory.create_shape("rectangle", 5, 7)

calc.print_shape_info(circle)
calc.print_shape_info(rectangle)