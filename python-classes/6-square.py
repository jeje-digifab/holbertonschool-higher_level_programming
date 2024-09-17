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

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new square with a specified side length.

        Args:
            size (float): The length of each side of the square.
        """

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Get the side length of the square.

        Returns:
            int: The length of each side of the square.
        """
        return self.__size

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

        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square, which is the square
            of the side length.
        """

        return (self.__size ** 2)

    def my_print(self):
        """
        Print the square using the '#' character.

        If the size of the square is 0, this method will print an empty line.
        Otherwise, it will print the square using the '#' character.
        """
        if self.size == 0:
                print("")
        else:
            for _ in range(self.position[1]):
                print("")

            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)

