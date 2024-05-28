#!/usr/bin/python3
"""Module compiled with python3"""

import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

"""
Try to load the content of the JSON file "add_item.json".
If the file doesn't exist, initialize an empty list.
"""
try:
    items = load_from_json_file("add_item.json")
except FileNotFoundError:
    items = []

"""
Add the command-line arguments to the list, ignoring the first argument.
"""
items.extend(sys.argv[1:])

"""
Save the updated list to the file "add_item.json".
"""
save_to_json_file(items, "add_item.json")
