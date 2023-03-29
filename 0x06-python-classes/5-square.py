#!/usr/bin/python3

"""Define a Square class"""


class Square:
    """Blueprint for a square"""

    def __init__(self, size=0):
        """Initialize a new square

        Args:
            size (int): The length of the new square
        """
        self.__size = size

    @property
    def size(self):
        """Get the size/length of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square represented with #"""
        for i in range(self.__size):
            print("#" * self.__size))
            print("")
        if self.__size == 0:
            print("")
