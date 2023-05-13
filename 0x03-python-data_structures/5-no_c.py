#!/usr/bin/python3
def no_c(my_string):
    replace = ['c', 'C']
    new_str = list(my_string)
    new = ''
    for i in range(len(my_string)):
        if new_str[i] in replace:
            new_str[i] = new
    return ''.join(new_str)
