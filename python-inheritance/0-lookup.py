#!/usr/bin/python3
"""Function to return list of attributes and methods of an object"""


def lookup(obj):
    """Returns list of attributes and methods available in an object"""
    return dir(obj)
