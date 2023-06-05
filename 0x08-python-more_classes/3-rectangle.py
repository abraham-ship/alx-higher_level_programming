#!/usr/bin/python3

"""A class that defines a rectangle"""


class Rectangle:
    """A class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """a class that defines a rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set width of rectangle"""
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
        """Get/setter height of rectangle"""
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
        """return perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """return string format of rectangle"""
        if not self.__height or not self.__width:
            return ""
        s = ''
        for i in range(self.__height):
            s += '#' * self.__width + '\n'
        return s[:-1]
