#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""


def inherits_from(obj, a_class):
    """
    Return True if obj is an instance of a subclass of a_class,
    but not a direct instance of a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a subclass of a_class,
        but not a direct instance of a_class.
    """

    return isinstance(obj, a_class) and type(obj) is not a_class
