#!/usr/bin/python3
"""Module compiled with python3"""

import xml.etree.ElementTree as ET

class serialize:
    def serialize_to_xml(self, dictionary, filename):
        """
        Function to serialize a dictionary to an XML file.

        :param dictionary: The dictionary to be serialized.
        :param filename: The path to the XML file to be created.
        """

        root = ET.Element('data')

        for key, value in dictionary.items():
            item = ET.Element(key)
            item.text = str(value)
            root.append(item)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)

    def deserialize_from_xml(self, filename):
        """
        Function to deserialize an XML file to a dictionary.

        :param filename: The path to the XML file to be read.
        :return: The deserialized dictionary.
        """
        tree = ET.parse(filename)
        root = tree.getroot()

        dictionary = {}
        for child in root:
            dictionary[child.tag] = child.text

        return dictionary


"""
if __name__ == "__main__":
    main()
"""

