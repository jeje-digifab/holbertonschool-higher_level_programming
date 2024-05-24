#!/usr/bin/python3
"""Module compiled with python3"""


def is_same_class(obj, a_class):
    """
    This function checks if the object is exactly an instance
    of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare.

    Returns:
        True if the object is exactly an instance of the specified
        class, otherwise False.
    """
    return type(obj) is a_class


if __name__ == "__main__":
    main()
