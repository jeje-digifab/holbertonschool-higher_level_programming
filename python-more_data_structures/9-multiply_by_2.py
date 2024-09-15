#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""


def multiply_by_2(a_dictionary):
    """Multiply all values in a dictionary by 2.

    Args:
        a_dictionary (dict): A dictionary with numeric values.

    Returns:
        dict: A new dictionary with the same keys, but with each value
        multiplied by 2.
    """

    new_dictionary = a_dictionary.copy()

    for key in a_dictionary:
        new_dictionary[key] *= 2

    return (new_dictionary)
