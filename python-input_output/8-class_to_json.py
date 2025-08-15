#!/usr/bin/python3
"""
This module contains a function that returns the dictionary
description for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure.
    """
    return obj.__dict__
