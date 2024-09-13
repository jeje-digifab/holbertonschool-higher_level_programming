#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""


def print_sorted_dictionary(a_dictionary):
    """
    Return a new dictionary sorted by keys.

    :param a_dictionary: The dictionary to be sorted.
    :return: A new dictionary sorted by keys.
    """

    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
