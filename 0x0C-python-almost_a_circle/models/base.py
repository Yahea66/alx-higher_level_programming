#!/usr/bin/python3

"""
This module defines the Base class, which is designed to manage unique identifiers (IDs) for its instances.
The IDs can either be provided by the user at the time of instantiation or automatically generated to ensure uniqueness.
The automatic generation is handled through a class-level counter that increments with each new instance without a provided ID.
"""

import json

class Base:
    """
    A class to manage IDs for instances, supporting either user-provided or automatically incremental IDs.

    Attributes:
        __nb_objects (int): A class-level attribute that tracks how many instances have been created
                           when no specific ID is provided, ensuring unique IDs.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        If an ID is provided at instantiation, this ID is assigned to the instance.
        If no ID is provided, an incremental unique ID is generated and assigned.

        Parameters:
            id (int, optional): The unique identifier for the instance. Defaults to None, which triggers automatic ID assignment.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries into a JSON-formatted string. If the list is empty or not a list,
        it returns an empty JSON array string "[]".

        Parameters:
            list_dictionaries (list): A list of dictionaries that should be converted into a JSON string.

        Returns:
            str: A JSON string representing the list of dictionaries. Returns "[]" if input is invalid or empty.
        """
        if not list_dictionaries or not isinstance(list_dictionaries, list):
            return "[]"
        return json.dumps(list_dictionaries)
       
    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if not json_string or len(json_string) == 0:
            return []
        return json.loads(json_string)
