#!/usr/bin/python3
"""Module compiled with python3"""

import json


def load_from_json_file(filename):
    """
    Load data from a JSON file.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        dict: A dictionary containing the data loaded from the JSON file.
    """

    with open(filename, 'r') as file:
        data = json.load(file)
    return data


if __name__ == "__main__":
    main()
