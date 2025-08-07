#!/usr/bin/python3
"""Square class with custom string representation"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle with custom __str__"""

    def __init__(self, size):
        """Initialize square and validate size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Return string representation: [Square] size/size"""
        return f"[Square] {self.__size}/{self.__size}"
