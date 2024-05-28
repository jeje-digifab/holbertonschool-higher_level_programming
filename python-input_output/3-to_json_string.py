#!/usr/bin/python3
"""Module compiled with python3"""

import json


def to_json_string(my_obj):
    """
    Convert an object to a JSON string.

    Args:
    my_obj -- the Python object to convert

    Returns:
    A JSON string representing the object
    """
    return json.dumps(my_obj)


if __name__ == "__main__":
    main()
