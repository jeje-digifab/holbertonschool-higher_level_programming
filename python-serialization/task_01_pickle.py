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

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        is_student (bool): Indicates if the person is a student.

    Methods:
        display():
            Prints the attributes of the object to the console.

        serialize(filename):
            Serializes the object to a binary file using pickle.

        deserialize(filename):
            Class method that deserializes an object from
            a binary file using pickle.
    """

    def __init__(self, name, age, is_student):
        """
        Initializes a new CustomObject instance with name, age,
        and student status.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints the object's attributes: name, age, and student status.
        """
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
            None
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (FileNotFoundError, IOError, pickle.PicklingError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes a CustomObject from a binary file using pickle.

        Args:
            filename (str): The name of the file from which to load the object.

        Returns:
            CustomObject: The deserialized object from the file.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, IOError, pickle.UnpicklingError):
            return None
