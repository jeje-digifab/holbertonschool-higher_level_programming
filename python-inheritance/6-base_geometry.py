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


if __name__ == "__main__":
    main()
