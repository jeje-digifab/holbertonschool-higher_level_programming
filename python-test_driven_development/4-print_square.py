#!/usr/bin/python3
"""
This script contains a function to print a square with a given size.
"""


def print_square(size):
    """
    Prints a square made of '#' characters with the given size.

    Args:
        size (int): The size (width and height) of the square to print.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
