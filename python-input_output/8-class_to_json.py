#!/usr/bin/python3
"""Module compiled with python3"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object
    """
    return vars(obj)


if __name__ == "__main__":
    main()
