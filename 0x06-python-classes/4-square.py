#!/usr/bin/python3
""" Class: square declared """
class Square:
    """ Class: Square defined """
    def __init__(self, size=0):
        """ Intialized.
        Args:
            size (int): The size of the new square.
        """
        self.size = size
    
    @property
    def size(self):
        """ Function defined """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        " Funtion defined """
        return (self.__size * self.__size)
