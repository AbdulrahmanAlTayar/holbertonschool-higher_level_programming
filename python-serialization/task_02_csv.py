#!/usr/bin/env python3
"""
task_02_csv
Convert CSV data to JSON (written to data.json).
"""

import csv
import json
from typing import List, Dict


def convert_csv_to_json(csv_filename: str) -> bool:
    """
    Convert a CSV file to JSON written to 'data.json'.

    Args:
        csv_filename: path to the CSV file.

    Returns:
        True if conversion succeeded, False otherwise (e.g., file not found).
    """
    try:
        rows: List[Dict[str, str]] = []
        with open(csv_filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Keep values as strings to match the sample output
                rows.append(dict(row))

        with open("data.json", "w", encoding="utf-8") as out:
            json.dump(rows, out, indent=4)
        return True
    except FileNotFoundError:
        return False
    except Exception:
        # Any other error -> False as per instruction spirit
        return False
