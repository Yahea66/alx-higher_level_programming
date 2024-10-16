#!/usr/bin/python3

"""
This module provides a set of functions to manage I/O operations 
"""

def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8) and returns the number of characters written
    """

    with open(filename, 'w', encoding = 'utf-8') as file:
        file.write(text)
    return len(text)
