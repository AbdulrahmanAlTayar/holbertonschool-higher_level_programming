#!/usr/bin/python3
"""
This contains CountedIterator class that wraps an iterable and counts iterations
"""


class CountedIterator:
    """
    Iterator that counts how many times it was iterated
    """

    def __init__(self, iterable) -> None:
        self.__iterator = iter(iterable)
        self.__count = 0

    def __next__(self):
        value = next(self.__iterator)
        self.__count += 1
        return value

    def get_count(self) -> int:
        return self.__count

    def __iter__(self):
        return self
