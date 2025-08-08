#!/usr/bin/python3
"""
This contains code to manipulate shapes
"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    represent a shape
    """

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass


class Circle(Shape):
    """
    represent a circle
    """

    def __init__(self, radius) -> None:
        self.radius = abs(radius)

    def area(self) -> float:
        return pi * self.radius**2

    def perimeter(self) -> float:
        return 2 * pi * self.radius


class Rectangle(Shape):
    """
    represent a rectangle
    """

    def __init__(self, width, height) -> None:
        self.__width = width
        self.__height = height

    def area(self) -> float:
        return self.__width * self.__height

    def perimeter(self) -> float:
        return 2 * self.__height + 2 * self.__width


def shape_info(obj) -> None:
    """
    print shape obj info
    """
    print(f"Area: {obj.area()}")
    print(f"Perimeter: {obj.perimeter()}")
