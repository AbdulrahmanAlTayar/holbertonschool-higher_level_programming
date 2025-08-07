#!/usr/bin/python3
"""Square class that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class with size validation and area method"""

    def __init__(self, size):
        """Initialize square with size using parent's constructor"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns area of the square"""
        return self.__size ** 2
