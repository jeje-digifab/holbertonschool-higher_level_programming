#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""


class Student:
    """
    A class to represent a student with first name, last name,
    and age attributes.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.

    Methods:
        to_json():
            Returns a dictionary representation of the student's attributes.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance with the provided first name,
        last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the student's attributes
        for JSON serialization.
        If a list of attribute names is provided, only those attributes
        will be included.

        Args:
            attrs (list, optional): A list of attribute names to include
            in the output.
            If None, all attributes are included.

        Returns:
            dict: A dictionary containing the specified attributes
            of the student.
        """

        if attrs is None:
            return self.__dict__

        filtered_dict = {}

        if isinstance(attrs, list):
            for attr in attrs:
                if attr in self.__dict__:
                    filtered_dict[attr] = self.__dict__[attr]

        return filtered_dict

    def reload_from_json(self, json):
        pass



