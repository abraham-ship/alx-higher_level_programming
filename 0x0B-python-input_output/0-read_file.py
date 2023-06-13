#!/usr/bin/python3

""" read text file"""


def read_file(filename=""):
    """
    a function that reads a text file (UTF8) and prints it to stdout:
        Args:
            filename: file to be read
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read())
