#!/usr/bin/python3

class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        """Initialize square

        Args:
            size (int): Private instance attribute

        """
        self.__size = size
        if type(size) is not int:
            print("size must be an integer")
            raise TypeError
        if size < 0:
            print("size must be >= 0")
            raise ValueError

    def area(self):
        """Public instance method that returns square area."""
        return (self.__size ** 2)
