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

    def to_json(self):
        """
        Returns the dictionary representation of the student's attributes.

        Returns:
            dict: A dictionary containing the first name, last name,
            and age of the student.
        """
        return self.__dict__
