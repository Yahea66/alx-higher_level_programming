#!/usr/bin/python3
"""
A module for defining a Square class with a private size attribute,
including getter and setter, and a method to calculate area.
"""

class Square:
    """Class that defines a square with a private instance attribute 'size'
    and includes a property and setter for size management."""

    def __init__(self, size=0):
        """
        Initialize a new Square instance with optional size validation.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.size = size  

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints in stdout the square with the character #
        """

        if self.__size == 0:
            print() 
            return 
        for i in range(self.__size):
            for i in range(self.__size):
                print("#", end = " ")
            print() 
