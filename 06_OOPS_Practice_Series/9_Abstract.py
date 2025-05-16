from abc import ABC, abstractmethod

# Abstract Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Rectangle class inheriting Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Creating an object of Rectangle
rect = Rectangle(5, 3)
print(f"The area of the rectangle is: {rect.area()}")
