#!/usr/bin/python3
"""
A module for defining a Square class with private 'size' and 'position' attributes,
including getters and setters for these attributes, and methods to calculate area
and print the square to standard output.
"""

class Square:
    """Class that defines a square with private instance attributes 'size' and 'position'
    and includes properties and setters for size and position management."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance with optional size and position.

        Args:
            size (int, optional): The size of the square, defaults to 0.
            position (tuple, optional): The position of the square, defaults to (0, 0).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieve the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square with validation.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) and num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with the character '#' to stdout, considering position.

        The position is used to offset the square with leading spaces and newlines.
        """
        if self.__size == 0:
            print()
            return

        print("\n" * self.__position[1], end="")

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
