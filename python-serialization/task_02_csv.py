#!/usr/bin/python3
"""Module compiled with python3"""

import csv
import json


def convert_csv_to_json(csv_file):
    """
    Function to convert CSV to JSON format.

    :param csv_file: The path to the CSV file to be converted.
    :return: True if conversion is successful, False otherwise.
    """
    try:
        with open(csv_file, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)
            with open('data.json', 'w', encoding='utf-8') as jsonfile:
                jsonfile.write("[\n")
                for i, row in enumerate(rows):
                    jsonfile.write("    ")
                    json.dump(row, jsonfile, separators=(',', ':'))
                    if i < len(rows) - 1:
                        jsonfile.write(",\n")
                    else:
                        jsonfile.write("\n")
                jsonfile.write("]\n")
        return True

    except FileNotFoundError:
        return False

    except Exception:
        return False


if __name__ == "__main__":
    csv_file = "data.csv"
    convert_csv_to_json(csv_file)
    print(f"Data from {csv_file} has been converted to data.json")
