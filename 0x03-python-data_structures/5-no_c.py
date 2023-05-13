#!/usr/bin/python3
def no_c(my_string):
    replace = ['c', 'C']

    for char in my_string:
        if char in replace:
            my_string = my_string.replace(char, '')
    return my_string
