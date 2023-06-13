#!/usr/bin/python3

"""write to file"""


def write_file(filename="", text=""):
    """
    a function to write content to a file
    Args:
        filename: file to write to
        text: content to be written
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(text)
        return len(text)
