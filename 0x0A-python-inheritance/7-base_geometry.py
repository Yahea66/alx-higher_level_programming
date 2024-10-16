#!/usr/bin/python3

"""
This module provides a class that defines and Characterize different geometric structures 
"""

class BaseGeometry:
    """
    BaseGeometry defines the structure of a geometry utilize functions and attribute
    """
   
    def area(self):
        """
        Public instance method: def area(self): that raises an Exception with the message area() is not implemented
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method: def integer_validator(self, name, value): that validates value
        
        raises:
            TypeError: if value is not an integer 
            ValueError: if value is less or equal to 0
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if not value > 0:
            raise ValueError(f"{name} must be greater than 0") 
