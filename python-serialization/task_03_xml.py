#!/usr/bin/python3
"""
This script provides utility functions for serializing and deserializing
data to and from XML format using the xml.etree.ElementTree module.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize into XML.
        filename (str): The name of the file where the XML data will be saved.

    Returns:
        None
    """
    data = ET.Element("data")

    for key, value in dictionary.items():
        ET.SubElement(data, key).text = str(value)

    ET.ElementTree(data).write(filename)


def deserialize_from_xml(filename):
    """
    Deserializes data from an XML file into a dictionary.

    Args:
        filename (str): The name of the XML file to read from.

    Returns:
        dict: A dictionary containing the data loaded from the XML file.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}

    for child in root:
        dictionary[child.tag] = child.text

    return dictionary
