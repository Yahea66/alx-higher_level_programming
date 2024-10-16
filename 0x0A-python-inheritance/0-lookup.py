#!/usr/bin/python3

"""
This module provides utility functions to interact with and explore Python objects.
Currently, it includes a function to list attributes and methods of any Python object.
"""

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object as per the dir() function.

    Parameters:
    obj (object): The object whose attributes and methods are to be listed.

    Returns:
    list: A list containing the names of the attributes and methods of the object.
    """
    return dir(obj)
