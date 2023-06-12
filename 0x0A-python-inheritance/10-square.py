#!/usr/bin/python3

"""Defining a class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class inherites from rectangle"""
    def __init__(self, size):
        """Initialize square"""
        super().__init__(size, size)
