#!/usr/bin/python3
"""
A module for defining a Square class with a private 'size' attribute,
getter and setter for the attribute, an area calculation method,
and a method to print the square using standard output.
"""

class Square:
    """Class that defines a square with a private instance attribute 'size' 
    and includes a property and setter for size management, along with methods
    for calculating area and printing the square graphically."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance with optional size validation.

        Args:
            size (int, optional): The size of the square, defaults to 0.

            position(tuple, optional): The position of the square, defaults to (0,0)
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
        Retrieve the position of the square 

        Returns: 
            Tuple: the position of the square 
        """

        return self.__position 

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
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
        Print the square with the character '#' or an empty line if size is 0.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size) 
           
