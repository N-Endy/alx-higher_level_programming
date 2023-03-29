#!/usr/bin/python3

"""Define a Square class"""


class Square:
    """Blueprint for a square"""

    def __init__(self, size=0):
        """Initialize a new square

        Args:
            size (int): The length of the new square
        """
        self.size = size

    @property
    def size(self):
        """Get the size/length of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not instance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2
