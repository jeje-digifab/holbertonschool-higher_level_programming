#!/usr/bin/python3
"""Module compiled with python3"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of the specified class or an instance
    of a class that inherits from the specified class.

    Args:
    obj: The object to check.
    a_class: The class to test against.

    Returns:
    True if the object is an instance of the specified class or a subclass
    of that class, otherwise False.
    """
    return isinstance(obj, a_class)


if __name__ == "__main__":
    main()
