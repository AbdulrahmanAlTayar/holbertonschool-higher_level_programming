#!/usr/bin/env python3
"""
task_01_pickle
Serialize and deserialize a custom class using pickle.
"""

import pickle
from typing import Optional


class CustomObject:
    """
    A simple custom object to demonstrate pickling.
    Attributes:
        name (str)
        age (int)
        is_student (bool)
    """

    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self) -> None:
        """Print object attributes in the required format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename: str):
        """
        Serialize the current instance to `filename` using pickle.

        Returns:
            True on success, None on failure (per spec requirement to return None if error).
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
            return True
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename: str) -> Optional["CustomObject"]:
        """
        Deserialize an instance of CustomObject from `filename`.

        Returns:
            CustomObject instance on success, None on failure.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            # Ensure the loaded object is an instance of CustomObject
            if isinstance(obj, cls):
                return obj
            return None
        except Exception:
            return None
