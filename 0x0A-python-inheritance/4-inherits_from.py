#!/usr/bin/python3

"""
This module provides utility functions to interact with and explore Python objects. 
Currently, it includes a function to check wether an object is an instance of the specified class or not.
"""

def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
