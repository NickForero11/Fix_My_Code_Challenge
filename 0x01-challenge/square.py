#!/usr/bin/python3
"""Module with a basic Square Class
"""


class Square:
    """Square class with Width and Height.

    Keyword arguments:
    width(int): X size.
    height(int): Y size.
    """
    width = 0
    height = 0

    def __init__(self, width, height):
        """Initialize an empty or specific Square"""
        self.width = 0
        self.height = 0

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        self.__height = value

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """Compute the perimeter of a Square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Returns an human readable representation of a Square"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
