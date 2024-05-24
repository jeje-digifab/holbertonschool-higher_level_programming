#!/usr/bin/python3
"""Module compiled with python3"""


def lookup(obj):
    """
    This function returns a list of attributes and methods of an object.

    Parameters:
    obj (object) : The object for which we want to retrieve the attributes and methods.

    Returns:
    list (object) : A list of attributes and methods of the object 'obj'.
    """
    return dir(obj)


if __name__ == "__main__":
    main()
