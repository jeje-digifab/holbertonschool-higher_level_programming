#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry
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

        super().__init__()

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
        int: The area of the rectangle.
        """

        return (self.__width * self.__height)

    def __str__(self):
        """
        Return a string representation of the rectangle.

        The string is formatted as [Rectangle] <width>/<height>,
        where <width> and <height> are the width and height of the rectangle.

        Returns:
        str: A string in the format [Rectangle] <width>/<height>.
        """

        return (f"[Rectangle] {self.__width}/{self.__height}")


class Square(Rectangle):
    """
    Square class for geometric calculations.

    This class represents a square, which is a special type of rectangle where
    the width and height are equal. It inherits from the Rectangle class,
    utilizing its methods and properties while ensuring that the size of the
    square is validated as a positive integer.

    Attributes:
        __size (int): The size of the square, which is both the width
        and height.

    Methods:
        __init__(self, size):
            Initializes a Square object with the given size.
            Validates that size is a positive integer.

        area(self):
            Calculates and returns the area of the square.

        __str__(self):
            Returns a string representation of the square in the format
            "[Rectangle] <size>/<size>", since a square is a special case of
            a rectangle.
    """

    def __init__(self, size):
        """
        Initialize the Square with size.

        This method initializes a Square object with the provided `size`
        attribute after validating it using the integer_validator method.
        """

        super().__init__(size, size)

        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
        int: The area of the square.
        """

        return (self.__size ** 2)

    def __str__(self):
        """
        Return a string representation of the square.

        This calls the string representation of the Rectangle.

        Returns:
        str: A string in the format [Rectangle] <size>/<size>.
        """

        return f"[Square] {self.__size}/{self.__size}"
