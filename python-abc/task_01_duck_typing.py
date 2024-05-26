#!/usr/bin/python3
"""Module compiled with python3"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract class representing a geometric shape.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Class representing a circle.
    """

    def __init__(self, radius):
        """
        Initializes a circle with a given radius.
        """
        self.radius = radius

    def area(self):
        """
        Computes and returns the area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Computes and returns the perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Class representing a rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a rectangle with given width and height.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Computes and returns the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Computes and returns the perimeter of the rectangle.
        """
        return (self.width + self.height) * 2


def shape_info(shape):
    """
    Displays the area and perimeter of a shape.
    """
    print("Area: {:}".format(shape.area()))
    print("Perimeter: {:}".format(shape.perimeter()))


if __name__ == "__main__":
    main()
