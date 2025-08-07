#!/usr/bin/python3
"""Function to check if object is instance of class or its subclass"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is instance of a_class or subclass"""
    return isinstance(obj, a_class)
