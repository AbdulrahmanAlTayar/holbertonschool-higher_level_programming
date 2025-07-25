#!/usr/bin/python3
"""
This module defines a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div, rounded to 2 decimals."""
    if (not isinstance(matrix, list) or
            any(not isinstance(row, list) for row in matrix) or
            any(not all(isinstance(x, (int, float)) for x in row)
                for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
