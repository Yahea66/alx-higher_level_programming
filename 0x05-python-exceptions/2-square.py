#!/usr/bin/python3
"""
A module for defining a Square class with a private size attribute that
includes validation for both type and value.
"""

class Square:
    """Class that defines a square with a private instance attribute 'size'."""
    
    def __init__(self, size=0):
        """
        Initialize a new Square instance with optional size validation.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
