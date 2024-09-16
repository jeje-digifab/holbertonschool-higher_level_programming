#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""


class Square:
    """
    A class representing a square.

    This class defines a square by its side length and provides methods
    to calculate the area and perimeter of the square.
    """

    def __init__(self, size=0):
        """
        Initialize a new square with a specified side length.

        Args:
            size (float): The length of each side of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
