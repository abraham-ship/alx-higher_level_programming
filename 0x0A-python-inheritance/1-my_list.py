#!/usr/bin/python3

"""inherit class list"""


class MyList(list):
    """parent class"""
    def print_sorted(self):
        """print list sorted in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)
