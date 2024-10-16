#!/usr/bin/python3

"""
This module extends built-in Python data structures to add additional functionality.
Currently, it includes a subclass of the built-in list called MyList, which extends
the functionality of the standard list by adding a method to print the elements in
sorted order without altering the original list.

Classes:
    MyList: A subclass of the built-in list with an added method to print sorted elements.
"""

class MyList(list):
    """
    MyList extends the built-in Python list by adding a method to print the list
    elements in sorted order without modifying the original list.
    
    Attributes:
        Inherits all attributes of the built-in Python list.
    
    Methods:
        print_sorted(): Prints the elements of the list in ascending order.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in sorted order.
        
        This method does not alter the original list; instead, it prints a new list
        that is sorted. The sorting is done in ascending order.
        
        Examples:
            >>> my_list = MyList([3, 1, 2])
            >>> my_list.print_sorted()
            [1, 2, 3]
        """
        print(sorted(self))
