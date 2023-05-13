#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx >= 0 and idx <= len(my_list):
        list_copy = my_list.copy()
        list_copy[idx] = element
        return list_copy
    else:
        return my_list
