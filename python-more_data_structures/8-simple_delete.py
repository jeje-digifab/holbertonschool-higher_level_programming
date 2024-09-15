#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""


def simple_delete(a_dictionary, key=""):
    """
    Removes a key-value pair from a dictionary.

    Args:
        a_dictionary (dict): The dictionary to remove the key-value pair from.
        key (str): The key to be removed from the dictionary.

    Returns:
        dict: The modified dictionary with the specified
        key-value pair removed.
    """

    if key in a_dictionary:
        del a_dictionary[key]

    return (a_dictionary)
