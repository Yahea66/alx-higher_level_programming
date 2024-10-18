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
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance with width, height, and optional position and ID.

        Parameters:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle. Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle. Defaults to 0.
            id (int, optional): An optional unique identifier.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Gets the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.
        """
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.
        """
        self.__height = value

    @property
    def x(self):
        """
        Gets the x-coordinate of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the x-coordinate of the rectangle.
        """
        self.__x = value

    @property
    def y(self):
        """
        Gets the y-coordinate of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the y-coordinate of the rectangle.
        """
        self.__y = value
