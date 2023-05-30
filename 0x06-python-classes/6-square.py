#!/usr/bin/python3

""" Define a square """


class Square:
    """Class that defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize square."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set size of square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set size of square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (type(value) is not tuple or len(value) != 2 or
                not all([type(i) == int for i in value]) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ return current square area."""
        return (self.__size ** 2)

    def my_print(self):
        """Print '#' square."""
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
        for i in range(self.__position[1]):
            print("")
        if self.__size == 0:
            print("")
