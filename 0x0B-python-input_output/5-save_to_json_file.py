#!/usr/bin/python3

"""save obj to file"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using JSON representation.
    Args:
        my_obj: The object to be written.
        filename: The name of the file.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
