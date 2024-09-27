#!/usr/bin/python3
"""
This script demonstrates the use of abstract base classes and
duck typing in Python.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """Class representing a circle."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return (abs(math.pi * (self.radius ** 2)))

    def perimeter(self):
        """Calculate the perimeter (circumference) of the circle."""
        return (2 * math.pi * self.radius)


class Rectangle(Shape):
    """Class representing a rectangle."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return (self.width * self.height)

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * ((self.width + self.height))


def shape_info(shape):
    """Print the area and perimeter of the given shape."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
