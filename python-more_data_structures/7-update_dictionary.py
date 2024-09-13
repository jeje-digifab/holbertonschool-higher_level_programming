#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""


def update_dictionary(a_dictionary, key, value):
    """
    Creates a new dictionary by copying the original dictionary and updating
    it with the provided key and value.

    Args:
        a_dictionary (dict): The original dictionary to be copied.
        key: The key to be added or updated in the new dictionary.
        value: The value to be associated with the key in the new dictionary.

    Returns:
        dict: A new dictionary with the updated key-value pair.
    """
    a_dictionary_new = a_dictionary.copy()

    a_dictionary_new.update({key: value})

    return (a_dictionary_new)
