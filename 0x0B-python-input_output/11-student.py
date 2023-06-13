#!/usr/bin/python3

"""class student"""


class Student:
    """define a student"""
    def __init__(self, first_name, last_name, age):
        """initialize class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for attr, value in json.items():
            setattr(self, attr, value)
