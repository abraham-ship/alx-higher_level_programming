#!/usr/bin/python3
import json

"""to JSON string"""


def to_json_string(my_obj):
    """
    a function that returns JSON representation of string object
    Args:
        my_obj: string to be represented
    """
    return json.dumps(my_obj)
