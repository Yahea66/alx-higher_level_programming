#!/usr/bin/python3

"""
This module defines the Base class, which is designed to manage unique identifiers (IDs) for its instances.
The IDs can either be provided by the user at the time of instantiation or automatically generated to ensure uniqueness.
The automatic generation is handled through a class-level counter that increments with each new instance without a provided ID.
"""

import json
import os

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
        
    @classmethod 
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances that are inherited from Base.

        The filename is derived from the class name of the objects in list_objs and has the format <Class name>.json.
        If list_objs is None or empty, an empty list is saved.
        """
        file_name = f"{cls.__name__}.json"
        if list_objs is None or list_objs == []:
            json_string = "[]"
        else:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(list_dicts)
        with open(file_name, 'w') as file:
            file.write(json_string)
       
    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if not json_string or len(json_string) == 0:
            return []
        return json.loads(json_string)
   
    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance with attributes set according to the dictionary provided.

        Args:
            **dictionary: Arbitrary keyword arguments representing attributes and their values.

        Returns:
            An instance of cls with attributes set according to the dictionary.
        """
        if cls.__name__ == 'Rectangle':
            dummy_ins = cls(1,1)
        elif cls.__name__ == 'Square':
            dummy_ins = cls(1)
        else:
            return None
        dummy_ins.update(**dictionary)
        return dummy_ins
    
    @classmethod 
    def load_from_file(cls):
        """
        returns a list of instances
        The filename must be: <Class name>.json - example: Rectangle.json
        If the file doesn’t exist, return an empty list
        Otherwise, return a list of instances - the type of these instances depends on cls (current class using this method)
        You must use the from_json_string and create methods (implemented previously)
        """
        file_name = f"{cls.__name__}.json"
        list_objs = []
        if not os.path.exists(file_name):
            return []
        with open(file_name, 'r') as file:
            json_string = file.read()
        list_dicts = cls.from_json_string(json_string)
        return [cls.create(**dic) for dic in list_dicts]
