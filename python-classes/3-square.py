#!/usr/bin/python3
"""Module that defines a Square class with size validation and area method"""


class Square:
    """Square class with private size and method to compute area"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square"""
        return self.__size * self.__size
