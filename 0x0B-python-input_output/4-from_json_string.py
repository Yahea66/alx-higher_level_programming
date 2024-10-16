#!/usr/bin/python3

"""
This module provides a set of functions to manage I/O operations 
"""

import json
def from_json_string(my_str):
    """
    returns the JSON representation of an object (string)
    """

    return json.loads(my_str)
