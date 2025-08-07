#!/usr/bin/python3
"""Rectangle class with area and custom string representation"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class with area method and printable format"""

    def __init__(self, width, height):
        """Initialize width and height using integer_validator"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return string representation: [Rectangle] width/height"""
        return f"[Rectangle] {self.__width}/{self.__height}"
