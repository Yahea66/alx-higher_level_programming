#!/usr/bin/python3
"""
This module provides a function that prints a text with 2 new lines after each of these characters: ., ? and :
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to be processed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    break_chars = ['.', '?', ':']
    output = []
    start = 0
    
    for i, char in enumerate(text):
        if char in break_chars:
            output.append(text[start:i+1].strip())
            output.append("\n\n")
            start = i + 1

    if start < len(text):
        output.append(text[start:].strip())
    
    for part in output:
        print(part, end="")
