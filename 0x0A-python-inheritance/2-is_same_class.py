#!/usr/bin/python3

"""
This module provides utility functions to interact with and explore Python objects. 
Currently, it includes a function to check wether an object is an instance of the specified class or not.
"""

def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class; otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False 
