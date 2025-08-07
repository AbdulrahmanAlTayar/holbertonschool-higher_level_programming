#!/usr/bin/python3
"""Class MyList that extends the built-in list with a print_sorted method"""


class MyList(list):
    """Custom list with ability to print itself sorted"""

    def print_sorted(self):
        """Prints the list in ascending sorted order"""
        print(sorted(self))
