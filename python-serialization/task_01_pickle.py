#!/usr/bin/python3
"""
This script contains a class `CustomObject` that demonstrates the use of
serialization and deserialization with the `pickle` module. The class also
includes a method to display object details.
"""
import pickle


class CustomObject:
    """
    A class to represent a custom object with attributes name, age,
    and student status.
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}\n"
              f"Age: {self.age}\n"
              f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current object and saves it to a binary
        file using pickle.

        Args:
            filename (str): The name of the file where the object
            will be saved.

        Returns:
            None: If an error occurs during serialization.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (FileNotFoundError, IOError, pickle.PicklingError, SyntaxError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes a CustomObject from a binary file using pickle.

        Args:
            filename (str): The name of the file from which to load the object.

        Returns:
            CustomObject: The deserialized object from the file, or None
            if an error occurs.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, IOError, pickle.UnpicklingError, SyntaxError):
            return None
