#!/usr/bin/python3
"""Module compiled with python3"""

import json


def save_to_json_file(my_obj, filename):
    """
    Save the given Python object as JSON to a file.

    Args:
        my_obj (any): The Python object to be saved as JSON.
        filename (str): The name of the file to save the JSON data to.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file, ensure_ascii=False)


if __name__ == "__main__":
    main()
