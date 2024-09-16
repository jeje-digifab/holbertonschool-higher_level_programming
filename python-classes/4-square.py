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
        """

        self._size = size

    @property
    def size(self):
        """
        Get the side length of the square.

        Returns:
            int: The length of each side of the square.
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        Set the side length of the square.

        Args:
            value (int): The new side length of the square.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is negative.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self._size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square, which is the square of the side length.
        """

        return (self._size ** 2)
