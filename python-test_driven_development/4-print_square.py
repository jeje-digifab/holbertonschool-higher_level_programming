#!/usr/bin/python3
"""Module compiled with python3"""


def print_square(size):
    """
    Prints a square of a given size using the '#' character.

    Args:
        size (int): The size of the square to print.

    Raises:
        TypeError: If the size is not an integer.
        ValueError: If the size is less than 0.

    Examples:
        >>> print_square(4)
        #####
        #####
        #####
        #####
        >>> print_square(0)

        >>> print_square(-1)
        Traceback (most recent call last):
          ...
        ValueError: size must be >= 0
        >>> print_square('a')
        Traceback (most recent call last):
          ...
        TypeError: size must be an integer
        >>> print_square(4.1)
        Traceback (most recent call last):
          ...
        TypeError: size must be an integer
        >>> print_square(-4.1)
        Traceback (most recent call last):
          ...
        TypeError: size must be an integer
        """
    if size == 0:
        print()

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if isinstance(size, float):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    else:
        for i in range(size):
            print("{:s}".format("#" * size))


if __name__ == "__main__":
    main()
