#!/usr/bin/python3
"""
This module provides arithmetic utility functions. The primary function, add_integer,
adds two numbers, ensuring they are integers or floats, and converts them to integers.
.......................................................................
"""

def add_integer(a, b=98):
    """
    a function that adds 2 integers.
     """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b) 
