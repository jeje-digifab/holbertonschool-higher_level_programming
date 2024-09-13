#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""


def update_dictionary(a_dictionary, key, value):
    """Replace or add key/value in a dictionary.

    Args:
        a_dictionary (dict): The dictionary to be updated.
        key (str): The key to be updated or added.
        value: The value associated with the key.

    Returns:
        dict: The updated dictionary.
    """
    a_dictionary.update({key: value})

    return (a_dictionary)
