#!/usr/bin/python3
"""BaseGeometry class with area method that raises exception"""


class BaseGeometry:
    """Class with unimplemented area method"""

    def area(self):
        """Raises an exception since area is not implemented"""
        raise Exception("area() is not implemented")
