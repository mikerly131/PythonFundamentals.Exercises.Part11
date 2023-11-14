class Rectangle:
    """
    Represents a rectangle
    """

    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width

    def get_area(self) -> int:
        area = self.length * self.width
        return area

    def get_perimeter(self) -> int:
        perim = (2*self.length) + (2*self.width)
        return perim

class Square(Rectangle):
    """
    Represents a square, a special type of rectangle
    """
    def __init__(self, side_length=0):
        self.length = side_length
        self.width = side_length


