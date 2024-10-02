#!/usr/bin/python3
"""
A module for defining a Square class with a private size attribute.

This module defines a Square class where the size attribute is private,
which means it cannot be accessed or modified directly from outside the class.
"""

class Square:
    """Class that defines a square with private instance attribute 'size'."""
    
    def __init__(self, size):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
