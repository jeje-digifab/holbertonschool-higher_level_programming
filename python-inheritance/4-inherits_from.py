#!/usr/bin/python3
"""Module compiled with python3"""


def inherits_from(obj, a_class):
    """
    Check if an object inherits from a given class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if the object inherits from the class, False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class


if __name__ == "__main__":
    main()
