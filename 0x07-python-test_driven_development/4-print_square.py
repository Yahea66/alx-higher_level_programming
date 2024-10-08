#!/usr/bin/python3
"""
This module provides a function to prints a square with the character #.
"""

def print_square(size):
    """
    prints a square with the character #.

    Args:
    size (int): The size of the square 

    Raises:
    TypeError: If size is not an integer. 
    ValueError: if size is negative. 
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0") 

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for row in range(size):
        for i in range(size):
            print("#", end = "")
        print() 
