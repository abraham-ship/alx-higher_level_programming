#!/usr/bin/python3

"""append content to file"""


def append_write(filename="", text=""):
    """
    append to file
    Args:
        filename: file to append content
        text: content to be appended
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
