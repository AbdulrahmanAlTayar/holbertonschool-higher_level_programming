#!/usr/bin/python3
"""
This module contains a function to save an object to a file in JSON format.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
