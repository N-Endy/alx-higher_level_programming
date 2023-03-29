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

    @property
    def position(self):
        """Get/set the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square represented with # sign"""
        if self.size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(0, self.__size):
                for k in range(self.__position[0]):
                    print(" ", end='')
                for j in range(self.__size):
                    print("#", end='')
                print()
