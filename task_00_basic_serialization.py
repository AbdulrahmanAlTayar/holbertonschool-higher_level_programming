#!/usr/bin/env python3
"""
task_00_basic_serialization
Basic JSON serialization/deserialization helpers.
"""

import json
from typing import Dict, Any


def serialize_and_save_to_file(data: Dict[str, Any], filename: str) -> None:
    """
    Serialize a Python dictionary to JSON and save it to `filename`.
    If the output file exists, it will be replaced.

    Args:
        data: Python dict to serialize.
        filename: Target JSON filename.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename: str) -> Dict[str, Any]:
    """
    Load JSON content from `filename` and deserialize it to a Python dict.

    Args:
        filename: Source JSON filename.

    Returns:
        Dict[str, Any]: deserialized dictionary.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
