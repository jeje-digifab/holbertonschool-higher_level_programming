#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
# from 7-base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class for geometric calculations.

    This script defines a `Rectangle` class that is used for geometric
    calculations related to rectangles. It initializes
    with `width` and `height` attributes after validating them as integers
    using the `integer_validator` method inherited from the `BaseGeometry`
    class in the `7-base_geometry` module.
    """

    def __init__(self, width, height):
        """
        Initialize the Rectangle with width and height.

        This method initializes a Rectangle object with the provided `width`
        and `height` attributes after validating them using the
        `integer_validator` method.
        """

        self.__width = width
        self.__height = height

        super().__init__()
