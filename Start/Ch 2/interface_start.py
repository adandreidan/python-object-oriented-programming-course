# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to implement interfaces

from abc import ABC, abstractmethod


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass

class JSONify(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def toJSN(self):
        pass

class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)
    
    def toJSN(self):
        return f"{{'Circle': {str (self.calcArea())}}}"


c = Circle(10)
# print(Circle.__mro__)
print(c.calcArea())
print(c.toJSN)