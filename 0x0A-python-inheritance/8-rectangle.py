#!/usr/bin/python3

"""
This module provides a Rectangle class that inherits from BaseGeometry
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """
    Instantiation with width and height: def __init__(self, width, height):
width and height must be private. No getter or setter
width and height must be positive integers, validated by integer_validator
    """

    def __init__(self, width, height):
        """
        args:
            width(int): the width of the rectangle
            height(int): the height of the rectangle
        """
        
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height) 
        self.__height = height 
