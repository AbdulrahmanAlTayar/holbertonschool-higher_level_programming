#!/usr/bin/python3
"""Module that defines a Rectangle class with a square classmethod"""


class Rectangle:
    """
    Rectangle class with width/height, area, perimeter,
    str/repr, delete message, instance counter, print symbol,
    static method for comparison and class method for squares
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the rectangle width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the rectangle height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with bigger area (rect_1 if equal)"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle with width == height == size"""
        return cls(size, size)

    def __str__(self):
        """Return string representation using print_symbol"""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(str(self.print_symbol) * self.width
                         for _ in range(self.height))

    def __repr__(self):
        """Return a string that recreates this rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Message when a rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
