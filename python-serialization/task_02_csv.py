#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""

import csv
import json


def convert_csv_to_json(filename):
    """
    Converts a CSV file to a JSON file.

    Args:
        filename (str): The name of the CSV file to convert.

    Returns:
        bool: True if conversion was successful, False otherwise.
    """

    data = []

    try:
        with open(filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for rows in reader:
                data.append(rows)

        with open("data.json", "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4)

        return True
    except FileNotFoundError:
        print(f"file not found")
        return False
