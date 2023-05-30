#!/usr/bin/python3

"""Define a square"""


class Square:
    """Class that defines a square."""

    def __init__(self, size=0):
        """Initialize square"""
        self.size = size

    @property
    def size(self):
        """Get/set size square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Public instance method that returns square area."""
        return (self.__size ** 2)

    def my_print(self):
        """Print '#' square"""
        for i in range(self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print("")
