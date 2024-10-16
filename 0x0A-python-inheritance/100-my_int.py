#!/usr/bin/python3

"""
invert comparison operators 
"""

class MyInt(int):
    """
    MyInt is a rebel. MyInt has == and != operators inverted
    """

    def __eq__(self, other):
        """
        args:
            other(int): the number being compared 
        """
        return super().__eq__ (other) == False

    def __ne__(self, other):
        """
        invert the (!=) operator
        """

        return super().__ne__(other) == False
