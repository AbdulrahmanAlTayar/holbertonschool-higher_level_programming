#!/usr/bin/env python3
"""Abstract Animal class with sound method and its subclasses"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for all animals"""

    @abstractmethod
    def sound(self):
        """Abstract method to be implemented by subclasses"""
        pass


class Dog(Animal):
    """Dog class that implements sound method"""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat class that implements sound method"""

    def sound(self):
        return "Meow"
