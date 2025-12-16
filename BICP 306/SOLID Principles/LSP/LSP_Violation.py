class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height
    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    def set_width(self, width):
        self.width = width
        self.height = width
    def set_height(self, height):
        self.width = height
        self.height = height

def calculate_area(rectangle: Rectangle):
    rectangle.set_width(5)
    rectangle.set_height(9)
    return rectangle.area()

if __name__ == "__main__":
    rect = Rectangle(2, 3)
    sq = Square(4)

    print("Rectangle area:", calculate_area(rect))  
    print("Square area:", calculate_area(sq))       
