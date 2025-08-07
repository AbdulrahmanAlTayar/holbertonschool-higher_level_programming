#!/usr/bin/python3
"""Function to check if object is instance of subclass of a class"""


def inherits_from(obj, a_class):
    """Return True if obj is instance of subclass (not the class itself)"""
    return isinstance(obj, a_class) and type(obj) is not a_class
