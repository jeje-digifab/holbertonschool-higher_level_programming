#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""


def common_elements(set_1, set_2):
    """
    Return the intersection of two sets.

    The intersection is the set of elements that are present in both
    sets. It returns the common elements between set_1 and set_2.

    Parameters:
    set_1 (set): The first set.
    set_2 (set): The second set.

    Returns:
    set: The intersection of set_1 and set_2.
    """

    return (set_1.intersection(set_2))
