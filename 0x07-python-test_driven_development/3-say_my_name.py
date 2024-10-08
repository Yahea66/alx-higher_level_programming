#!/usr/bin/python3
"""
This module provides a function to print a person's name.
"""

def say_my_name(first_name, last_name=""):
    """
    Prints the full name in the format: "My name is <first name> <last name>".

    Args:
    first_name (str): The first name.
    last_name (str): The last name, optional.

    Raises:
    TypeError: If either first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {0} {1}".format(first_name, last_name).strip())
