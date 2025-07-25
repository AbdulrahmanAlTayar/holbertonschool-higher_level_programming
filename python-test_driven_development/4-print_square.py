#!/usr/bin/python3
"""
This module defines a function that prints a square with #.
"""


def print_square(size):
    """Print a square with the character #.

    Args:
        size (int): the size of the square (length of a side)

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
