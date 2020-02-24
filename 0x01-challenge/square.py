#!/usr/bin/python3
"""Module with a basic Square Class
"""


class Square:
    """Square class with Width and Height.

    Keyword arguments:
    width(int): X size.
    height(int): Y size.
    """

    def __init__(self, *args, **kwargs):
        """Initialize an empty or specific Square"""
        self.width = 0
        self.height = 0
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
        if args:
            (self.width, self.height) = args

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
