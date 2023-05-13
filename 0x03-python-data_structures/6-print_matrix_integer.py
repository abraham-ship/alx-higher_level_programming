#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for val in row:
            if val == row[len(row) - 1]:
                print("{}".format(val), end='')
            else:
                print("{} ".format(val), end='')
        print()
