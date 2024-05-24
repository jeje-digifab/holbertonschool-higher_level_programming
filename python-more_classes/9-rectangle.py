#!/usr/bin/python3
"""Module compiled with python3"""


class Rectangle:
    """Class that represents a rectangle with a width and height"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle object with the given width and height.
        If no values are provided, the rectangle will have a width and height
        of 0.
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Set the height of the rectangle.
        The value must be an integer and greater than or equal to 0.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.
        The value must be an integer and greater than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """
        Return the perimeter of the rectangle.
        If the width or height is 0, the perimeter is also 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def my_print(self):
        """
        Print the rectangle with the character(s) stored in print_symbol.
        If the width or height is equal to 0, an empty string is returned.
        """
        if self.width == 0 or self.height == 0:
            return ""

        rectangle_str = ""
        for i in range(self.height):
            for j in range(self.width):
                rectangle_str += str(self.print_symbol)
            rectangle_str += "\n"
        return rectangle_str.rstrip()

    def __str__(self):
        """Returns a string representing the rectangle."""
        return self.my_print()

    def __repr__(self):
        """
        Return a string representation of the rectangle that can be used to
        recreate a new instance with the same attributes.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print a message when the instance is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.width * rect_1.height
        area_2 = rect_2.width * rect_2.height

        if area_1 == area_2:
            return rect_1

        if area_1 < area_2:
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """
        Create a new square instance of the class with the given size.
        The size value must be a positive integer.
        If no size is provided, a square with a size of 0 is created.
        """
        if not isinstance(size, int):
            raise ValueError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be >= 0")
        return cls(size, size)


if __name__ == "__main__":
    main()
