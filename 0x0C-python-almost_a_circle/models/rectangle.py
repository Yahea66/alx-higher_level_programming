#!/usr/bin/python3

"""
This module provides the Rectangle class which extends functionality from the Base class.
It defines a rectangle with properties for width, height, x-coordinate, and y-coordinate,
optionally managing a unique ID for each instance.
"""

from models.base import Base

class Rectangle(Base):
    """
    Represents a rectangle with properties for width, height, and position coordinates (x, y).
    Inherits from Base class to optionally manage a unique ID for each rectangle instance.
    
    Attributes:
        width (int): Width of the rectangle, must be a positive integer.
        height (int): Height of the rectangle, must be a positive integer.
        x (int): X-coordinate of the rectangle, must be a non-negative integer.
        y (int): Y-coordinate of the rectangle, must be a non-negative integer.
        id (int): An optional unique identifier managed by the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance with specified width, height, and optional position and ID.
        
        Parameters:
            width (int): The width of the rectangle, must be a positive integer.
            height (int): The height of the rectangle, must be a positive integer.
            x (int, optional): The x-coordinate of the rectangle, defaults to 0.
            y (int, optional): The y-coordinate of the rectangle, defaults to 0.
            id (int, optional): An optional identifier that uniquely identifies the rectangle instance.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        for _ in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """
        Return the string representation of the Rectangle instance.
        
        This method provides a quick, formatted summary of the rectangle's state, including its unique identifier,
        position coordinates, and size dimensions. It is especially useful for debugging and logging purposes.
        
        Returns:
            str: A string in the format "[Rectangle] (id) x/y - width/height".
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
