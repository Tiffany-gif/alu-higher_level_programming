#!/usr/bin/python3
"""Base class for all future classes"""

class Base:
    """Base of all other classes in this project"""

    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        """Constructor for Base

        Args:
            id (int, optional): ID of the instance. If None, auto-increments.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
