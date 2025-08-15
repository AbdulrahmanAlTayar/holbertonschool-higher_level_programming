#!/usr/bin/python3
"""
This module contains a function to generate Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal’s triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for _ in range(1, n):
        prev = triangle[-1]
        row = [1] + [prev[i] + prev[i + 1] for i in range(len(prev) - 1)] + [1]
        triangle.append(row)
    return triangle
