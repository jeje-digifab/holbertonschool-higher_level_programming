#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Saves a Python object as a JSON file.

    Args:
        my_obj (any): The Python object to save in JSON format.
        filename (str): The name of the file where the JSON data will be saved.

    Returns:
        None
    """
    with open(filename, "w", encoding="utf-8") as f:
        return (json.dump(my_obj, f, ensure_ascii=False, indent=4))
