#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes the given data to JSON format and saves it to a file.

    Args:
        data (any): The data to serialize and save (must be JSON serializable).
        filename (str): The name of the file where the JSON data will be saved.

    Returns:
        None
    """
    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(data, f)


def load_and_deserialize(filename):
    """
    Loads JSON data from a file and deserializes it into a Python object.

    Args:
        filename (str): The name of the file to read the JSON data from.

    Returns:
        any: The deserialized Python object from the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
