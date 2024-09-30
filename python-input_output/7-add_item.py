#!/usr/bin/python3
"""
This script saves command-line arguments to a JSON file.

It checks if the file 'add_item.json' exists:
- If it does, it loads the existing items into a list.
- If it doesn't, it creates a new file and initializes an empty list.

The script then appends any additional command-line arguments
to the list and saves the updated list back to the JSON file.

Usage:
    python script_name.py item1 item2 item3 ...

Where item1, item2, and item3 are the items to be added to the JSON file.
"""

import os
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


args = sys.argv
filename = "add_item.json"


if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    open(filename, "x")
    my_list = []


my_list.extend(args[1:])
save_to_json_file(my_list, filename)
