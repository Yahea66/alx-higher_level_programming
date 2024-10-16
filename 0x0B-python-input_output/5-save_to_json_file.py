#!/usr/bin/python3

"""
This module provides a set of functions to manage I/O operations 
"""

import json
def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation
    """

    with open(filename, 'w', encoding = 'utf-8') as file:
        file.write(json.dumps(my_obj))
