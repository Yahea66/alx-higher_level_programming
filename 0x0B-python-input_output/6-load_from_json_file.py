#!/usr/bin/python3

"""
This module provides a set of functions to manage I/O operations 
"""

import json
def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”
    """

    with open(filename, 'r', encoding = 'utf-8') as file:
        content = file.read()
        return json.loads(content)
