#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""


def class_to_json(obj):
    """
    Returns the dictionary representation of an object's attributes
    for JSON serialization.

    Args:
        obj (any): An instance of a class.

    Returns:
        dict: The dictionary containing the object's attributes.
    """

    return (obj.__dict__)
