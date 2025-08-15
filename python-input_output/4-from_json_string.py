#!/usr/bin/python3
"""
This module contains a function to convert JSON string to Python object.
"""
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) from  JSON string.
    """
    return json.loads(my_str)
