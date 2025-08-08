#!/usr/bin/python3
"""
This contains VerboseList class that extends list with notifications
"""


class VerboseList(list):
    """
    Extends list with verbose feedback on mutations
    """

    def append(self, item) -> None:
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable) -> None:
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item) -> None:
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index: int = -1):
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
