#!/usr/bin/python3
"""Module compiled with python3"""


class BaseGeometry:
    """
    This class represents a base for geometry. Currently, it doesn't
    contain any specific methods or attributes, but it can be used as
    a parent class for other geometry classes to share common functionalities.
    """

    def area(self):
        """
        Check if the current instance belongs to the same class as the method
        and raise an exception if area() is not implemented.
        """
        if isinstance(self, self.__class__):
            raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if the value is an integer and greater than 0.

        Args:
            name (str): The name of the variable.
            value (int): The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    def integer_validator(self, name, value):
        """
        Validate that value is a positive integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """
        Initialize a rectangle with width and height.
        Values must be positive integers validated by integer_validator.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return the rectangle description: [Rectangle] <width>/<height>.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


if __name__ == "__main__":
    main()
