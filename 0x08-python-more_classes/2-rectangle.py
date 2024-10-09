#!/usr/bin/python3
"""Module 0-rectangle

This module defines a class Rectangle that serves as a template
to define a rectangle. This class can be expanded later with properties
and methods that describe the characteristics and behaviors of a rectangle.
"""

class Rectangle:
    """Class that defines a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle with optional width and height.

        Args:
            width (int): The width of the rectangle, defaults to 0.
            height (int): The height of the rectangle, defaults to 0.

        Raises:
            TypeError: If either width or height is not an integer.
            ValueError: If either width or height is less than 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle, or 0 if either dimension is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
