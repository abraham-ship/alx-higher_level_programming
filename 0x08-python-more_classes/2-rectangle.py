#!/usr/bin/python3

"""A class that defines a Rectangle."""


class Rectangle:
    """A class that defines a Rectangle
    Args:
        width (int): width of rectangle
        height (int): height of rectangle
    """
    def __init__(self, width=0, height=0):
        """Initialize a rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/setter for width in rectagle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/setter for height in rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """return rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__height * 2) + (self.__width * 2))
