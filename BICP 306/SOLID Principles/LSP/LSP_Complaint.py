from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side

def print_area(shape: Shape):
    return shape.area()

if __name__ == "__main__":
    rect = Rectangle(5, 10)
    sq = Square(5)
    print("Rectangle area:", print_area(rect))
    print("Square area:", print_area(sq))  
