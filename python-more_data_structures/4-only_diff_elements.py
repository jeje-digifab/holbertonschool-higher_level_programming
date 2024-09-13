#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""


def only_diff_elements(set_1, set_2):
    """
    Return the symmetric difference of two sets.

    The symmetric difference is the set of elements that are in either
    of the sets, but not in their intersection. In other words, it returns
    elements that are unique to each set.

    Parameters:
    set_1 (set): The first set.
    set_2 (set): The second set.

    Returns:
    set: The symmetric difference of set_1 and set_2.
    """

    return set_1.symmetric_difference(set_2)
