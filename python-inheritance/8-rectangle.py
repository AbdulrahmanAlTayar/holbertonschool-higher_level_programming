#!/usr/bin/python3
"""Rectangle class inheriting from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class with validated private width and height"""

    def __init__(self, width, height):
        """Initialize width and height using integer_validator"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
