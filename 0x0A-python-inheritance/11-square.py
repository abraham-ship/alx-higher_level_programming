#!/usr/bin/python3

"""Defining class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square inheriting from rectangle"""
    def __init__(self, size):
        """initialize class"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """return area of square"""
        return self.__size * self.__size

    def __str__(self):
        """return representation of square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
