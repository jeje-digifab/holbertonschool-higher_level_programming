#!/usr/bin/python3
"""Module compiled with python3"""


class Square:
    """"Class defining a Square, for now printing empty stuff"""
    def __init__(self, size=0):
        """
        Initializes a Square object.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size


if __name__ == "__main__":
    main()
