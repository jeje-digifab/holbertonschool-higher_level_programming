#!/usr/bin/python3
"""Module compiled with python3"""


class Student:
    """
    Defines a class Student that represents a student with attributes first
    name, last_name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with the provided first name, last name,
        and age.

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
        Converts the Student instance to a JSON representation.

        Args:
            attrs (list of str, optional): A list of attributes to include in
                the JSON representation. If None, all attributes are included.

        Returns:
            dict: A dictionary representing the Student instance in JSON
            format.
        """
        if attrs is None:
            return vars(self)
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(
                self, attr)}


if __name__ == "__main__":
    main()
