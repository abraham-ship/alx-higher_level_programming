#!/usr/bin/python3

"""Define class rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle inheriting from BaseGeometry"""
    def __init__(self, width, height):
        """Initialize class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """return area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """return representation of rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
