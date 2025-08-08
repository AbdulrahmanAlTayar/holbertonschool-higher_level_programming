#!/usr/bin/python3
"""
This contains mixin-based Dragon class that can swim and fly
"""


class SwimMixin:
    """
    Adds swimming ability
    """

    def swim(self) -> None:
        print("The creature swims!")


class FlyMixin:
    """
    Adds flying ability
    """

    def fly(self) -> None:
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A dragon that can swim, fly, and roar
    """

    def roar(self) -> None:
        print("The dragon roars!")
