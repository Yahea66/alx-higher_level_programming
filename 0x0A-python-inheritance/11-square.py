#!/usr/bin/python3

"""
This module provides a Rectangle class that inherits from BaseGeometry
"""

Rectangle = __import__("9-rectangle").Rectangle

class Square(Rectangle):
    """
    Instantiation with size: def __init__(self, size)::

size must be private. No getter or setter

size must be a positive integer, validated by integer_validator
    """

    def __init__(self, size):
        """
        args:
            size(int): the dimension of the Square 
        """
        
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        utility method to culculate the area of the Square
        """

        return self.__size ** 2

    def __str__(self):
        """
        represents the rectangle dimensions 
        """

        return f"[Square] {self.__size}/{self.__size}"
