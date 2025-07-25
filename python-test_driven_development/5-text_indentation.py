#!/usr/bin/python3
"""
This module contains functions to indent strings
"""


def text_indentation(text):
    """This function add two lines after eache ?, :, . in text"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.strip()
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print()
            print()
            while i + 1 < len(text) and text[i + 1] in " \t":
                i += 1
        i += 1
