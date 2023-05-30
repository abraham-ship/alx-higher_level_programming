#!/usr/bin/python3

"""Define a square."""


class Square:
    """A class defining a square."""
    def __init__(self, size=0):
        """Initialize square.

        Args:
            size (int): Private instance attribute
        """
        self.__size = size

    @property
    def size(self):
        """get/set size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Public instance method, that returns the current square area"""
        return (self.__size ** 2)
