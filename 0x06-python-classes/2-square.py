#!/usr/bin/python3
"""Class: Square"""

class Square:
    """Class: square body"""
    def __init__(self, size=0):
        """Square defined:
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """Function defined."""
        return (self.__size * self.__size)
