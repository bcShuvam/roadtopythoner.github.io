from abc import ABCMeta , abstractmethod

class Shape(metaclass=ABCMeta):
    @abstractmethod
    def PrintArea(self):
        return 0

class Rectangle:
    type = "Ractangle"
    side = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7

    def PrintArea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.PrintArea())