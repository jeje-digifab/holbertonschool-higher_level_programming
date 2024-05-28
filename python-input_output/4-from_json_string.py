#!/usr/bin/python3
"""Module compiled with python3"""

import json


def from_json_string(my_str):
    """
    Converts a JSON-formatted string to a Python object.

    Args:
        my_str (str): A JSON-formatted string.

    Returns:
        object: A Python object representing the JSON data.

    Raises:
        JSONDecodeError: If the input string is not valid JSON.
    """
    return json.loads(my_str)


if __name__ == "__main__":
    main()
