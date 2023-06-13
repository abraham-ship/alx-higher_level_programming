#!/usr/bin/python3

"""create obj form JSON file"""
import json


def load_from_json_file(filename):
    """
    Create an object from a JSON file.
    Args:
        filename: The name of the JSON file.
    Returns:
        object: The object created from the JSON file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
