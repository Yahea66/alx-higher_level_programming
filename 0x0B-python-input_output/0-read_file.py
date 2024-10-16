#!/usr/bin/python3

"""
This module provides a set of functions to manage I/O operations 
"""

def read_file(filename=""):
    """
    reads a text file (UTF8) and prints it to stdout
    """

    with open(filename, 'r') as file:
        content = file.read()
    print(content)
