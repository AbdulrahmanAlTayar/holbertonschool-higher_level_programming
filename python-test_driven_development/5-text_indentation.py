#!/usr/bin/python3
"""
This module defines a function that prints text with indentation.
"""


def text_indentation(text):
    """Print text with 2 new lines after ., ? and :.

    Args:
        text (str): input string

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        ch = text[i]
        print(ch, end="")
        if ch in ".?:":
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
