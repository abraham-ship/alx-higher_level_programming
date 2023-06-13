#!/usr/bin/python3

"""Load, add, save"""
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


def add_arguments_to_list(arguments):
    """
    Add all arguments to a Python list.
    Args:
        arguments (list): The arguments to be added.
    Returns:
        list: The updated list.
    """
    try:
        existing_list = load_from_json_file('add_item.json')
    except FileNotFoundError:
        existing_list = []

    updated_list = existing_list + arguments
    save_to_json_file(updated_list, 'add_item.json')
    return updated_list


if __name__ == '__main__':
    arguments = sys.argv[1:]
    add_arguments_to_list(arguments)
