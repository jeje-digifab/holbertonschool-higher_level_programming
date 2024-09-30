#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""

import json


def load_from_json_file(filename):
    """
    Loads a Python object from a JSON file.

    Args:
        filename (str): The name of the file to read the JSON data from.

    Returns:
        any: The Python object represented by the JSON data in the file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
