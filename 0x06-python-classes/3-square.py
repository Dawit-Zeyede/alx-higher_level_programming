#!/usr/bin/python3
"""Class: Square"""


class Square:
    """Calss: Square body"""

    def __init__(self, size=0):
        """Initialzie a new square.
        Args:
            size (int): The size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            """ Function defination """
            return (self.__size * self.__size)
