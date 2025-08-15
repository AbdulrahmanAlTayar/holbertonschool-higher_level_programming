#!/usr/bin/env python3
"""
task_03_xml
Serialize a dictionary to XML and deserialize it back.
"""

import xml.etree.ElementTree as ET
from typing import Dict


def serialize_to_xml(dictionary: Dict[str, str], filename: str) -> None:
    """
    Serialize a dictionary (string values) into XML and save to filename.

    Args:
        dictionary: dict with string keys and values.
        filename: target XML file.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        # store as text; keep strings as-is, no type casting
        child.text = str(value) if value is not None else ""

    tree = ET.ElementTree(root)
    # No XML declaration needed to match sample; UTF-8 encoding.
    tree.write(filename, encoding="utf-8", xml_declaration=False)


def deserialize_from_xml(filename: str) -> Dict[str, str]:
    """
    Deserialize XML from filename back into a dictionary of strings.

    Args:
        filename: source XML file.

    Returns:
        dict[str, str]: reconstructed dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    result: Dict[str, str] = {}
    for child in root:
        # child.tag -> key, child.text -> value (string)
        result[child.tag] = "" if child.text is None else child.text
    return result
