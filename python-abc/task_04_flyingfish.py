#!/usr/bin/python3
"""
This contains a FlyingFish class using multiple inheritance
"""


class Fish:
    """
    Represents a fish
    """

    def swim(self) -> None:
        print("The fish is swimming")

    def habitat(self) -> None:
        print("The fish lives in water")


class Bird:
    """
    Represents a bird
    """

    def fly(self) -> None:
        print("The bird is flying")

    def habitat(self) -> None:
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A FlyingFish that can both swim and fly
    """

    def swim(self) -> None:
        print("The flying fish is swimming!")

    def fly(self) -> None:
        print("The flying fish is soaring!")

    def habitat(self) -> None:
        print("The flying fish lives both in water and the sky!")
