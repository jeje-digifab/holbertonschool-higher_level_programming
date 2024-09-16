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

    def __init__(self, size):
        """
        Initialize a new square with a specified side length.

        Args:
            size (float): The length of each side of the square.

        Raises:
            ValueError: If size is not a positive number.
        """
        self.__size = size
