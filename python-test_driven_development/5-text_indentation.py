#!/usr/bin/python3
"""
This module defines a function that prints text with indentation.
"""


def text_indentation(text):
    """
    Print text with 2 new lines after ., ? and :.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if text == "":
        print()
        return

    i = 0
    while i < len(text):
        ch = text[i]
        if ch in ".?:":
            print(ch)
            print()
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        else:
            print(ch, end="")

