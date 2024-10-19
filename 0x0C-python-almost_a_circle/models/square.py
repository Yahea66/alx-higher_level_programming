#!/usr/bin/python3
"""
This module defines the Square class which inherits from the Rectangle class.
The Square class models a square shape where the width and height are equal.
It extends the Rectangle's functionality by ensuring that both dimensions are always
the same and are represented by a single attribute, 'size'.

The Square class is part of a larger geometrical shapes management system and
ensures that all operations valid for a rectangle are equally applicable to a square,
with the added constraint that its width and height remain equal.
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Represents a square geometric shape with equal width and height,
    and maintains position with x and y coordinates.
    Inherits all attributes and methods from the Rectangle class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square instance with specified size and optional position and ID.
        
        Parameters:
            size (int): The size of the square's sides, used for both width and height.
            x (int, optional): The x-coordinate of the square. Defaults to 0.
            y (int, optional): The y-coordinate of the square. Defaults to 0.
            id (int, optional): An optional identifier for the square. Defaults to None.
        """
        super().__init__(width=size, height=size, x=x, y=y, id=id)
    
    @property 
    def size(self):
        """
        Gets the size of the square. The size is defined as the length of any one side
        of the square, which is equivalent to either the width or the height (since both
        are the same for a square).
        
        Returns:
            int: The size of the square.
        """
        return self.width
        
    @size.setter
    def size(self, value):
        """
        Sets the size of the square. This method ensures that both the width and height
        are updated together, maintaining the integrity of the square's shape.
        
        Parameters:
            value (int): The new size for the sides of the square.
        """
        self.width = value
        self.height = value 
       
    def __str__(self):
        """
        Return the string representation of the Square instance.
        Format: [Square] (<id>) <x>/<y> - <size>
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
