#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats and returns their sum.

    If either argument is a float, it is first cast to an integer before
    performing the addition. The default value for `b` is 98.

    Args:
        a (int, float): The first number to add. Must be an integer or float.
        b (int, float, optional): The second number to add. Must be an integer
                                  or float. Defaults to 98.

    Returns:
        int: The sum of `a` and `b`, cast to an integer.

    Raises:
        TypeError: If either `a` or `b` is not an integer or float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
