#!/usr/bin/python3
"""
This module provides a set of functions to manage I/O operations.

functions:
    load_from_json_file: creates an Object from a “JSON file”
    save_to_json_file: writes an Object to a text file, using a JSON representation
"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'
items = load_from_json_file(filename)
items.extend(sys.argv[1:])
save_to_json_file(items, filename)
