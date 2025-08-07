#!/usr/bin/python3
"""BaseGeometry class with area method and integer validation"""


class BaseGeometry:
    """Class with methods for area and integer validation"""

    def area(self):
        """Raises exception since area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
