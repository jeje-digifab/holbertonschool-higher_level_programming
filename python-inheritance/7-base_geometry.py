#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""


class BaseGeometry:
    """
    This script defines a BaseGeometry class that serves as a base class for
    basic geometric operations. It currently does not have any attributes or
    methods defined.
    """

    def area(self):
        """
        This method is used to calculate the area of a geometric shape.
        It is expected to be implemented in subclasses that inherit of
        the BaseGeometry class. If called directly of BaseGeometry,
        it will raise an Exception indicating that the method is
        not implemented.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This method validates whether a given value is an integer and
        greater than 0. It takes name as the name of the value being
        validated and value as the actual value. If the value is not
        an integer, it raises a TypeError with a message indicating the
        requirement for an integer type. If the value is less than or equal
        to 0, it raises a ValueError with a message indicating the
        requirement for a value greater than 0.
        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
