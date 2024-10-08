#!/usr/bin/python3
"""
This module provides arithmetic utility functions. The primary function, matrix_divided,
divides all the items by a number , ensuring they are integers or floats, and rounded all values to 2 decimal places. 
.......................................................................
"""

def matrix_divided(matrix, div):
    """
    a function that divide a matrix by div.
     """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number") 

    if div == 0:
        raise ZeroDivisionError("division by zero") 

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats") 
    
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        if len(matrix[0]) != len(row):
            raise TypeError("Each row of the matrix must have the same size")
 
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    new_matrix = [] 
    for row in matrix:
        new_list = []  
        for i in row:
            new_list.append(round((i / div), 2)) 
        new_matrix.append(new_list)
    return new_matrix
