#!/usr/bin/python3

"""Module divides elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Divide elements of a matrix

    Parameters:

        matrix: matrix
        div: a number

    Returns: a new matrix with divided by div, rounded to 2 decimal places
    """


    new = []
    final = []

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(matrix[0]) != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for val in row:
            if not isinstance(val, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new.append(round(val / div, 2))
        final.append(new)
        new = []
    return final
