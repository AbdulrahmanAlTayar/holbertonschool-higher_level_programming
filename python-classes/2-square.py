#!/usr/bin/python3
"""Module that defines a Square class with basic size validation"""


class Square:
    """Square with a private size that validates type and value"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
