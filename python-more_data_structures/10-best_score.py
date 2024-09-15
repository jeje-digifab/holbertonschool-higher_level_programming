#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""


def best_score(a_dictionary):
    """
    Given a dictionary, returns the key with the highest value.

    Args:
        a_dictionary: A dictionary containing key-value pairs.

    Returns:
        The key with the highest value, or None if the dictionary is empty.
    """

    if not a_dictionary:
        return None

    max_key = next(iter(a_dictionary))

    for key in a_dictionary:

        if a_dictionary[key] > a_dictionary[max_key]:
            max_key = key

    return (max_key)
