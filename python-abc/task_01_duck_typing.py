#!/usr/bin/env python3
"""Abstract Shape class and its implementations using duck typing"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class defining a shape"""

    @abstractmethod
    def area(self):
        """Return area of shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Return perimeter of shape"""
        pass


class Circle(Shape):
    """Circle class with radius"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class with width and height"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints area and perimeter using duck typing"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
