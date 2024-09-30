#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""

import json


def to_json_string(my_obj):
    """
    Converts a Python object to a JSON string.

    Args:
        my_obj (any): The Python object to convert to JSON.

    Returns:
        str: The JSON string representation of the Python object.
    """
    return json.dumps(my_obj)
