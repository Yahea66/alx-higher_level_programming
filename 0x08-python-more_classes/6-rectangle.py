#!/usr/bin/python3
"""Module 0-rectangle

This module defines a class Rectangle that serves as a template
to define a rectangle. This class can be expanded later with properties
and methods that describe the characteristics and behaviors of a rectangle.
"""

class Rectangle:
    """Class that defines a rectangle."""

    number_of_instances = 0  # Class variable to track the number of instances

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
        Rectangle.number_of_instances += 1 

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
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Visual representation of the rectangle using '#' characters."""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join("#" * self.width for _ in range(self.height))

    def __repr__(self):
        """Official string representation of the Rectangle."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Destructor to decrement instance count and print a message."""
        Rectangle.number_of_instances -= 1  
        print("Bye rectangle...")
