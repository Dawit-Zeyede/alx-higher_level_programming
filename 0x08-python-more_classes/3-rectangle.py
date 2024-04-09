#!/usr/bin/python3
"""
Class: rectangle
"""


class Rectangle:
    """Class: Rectangle body. """

    def __init__(self, width=0, height=0):
        """Initializes a rectangle"""
        self.width = width
        self.height = height

    def __str__(self):
        """Returns an informal string reprsentation
        """
        if self.__height == 0 or self.__width == 0:
            return ''
        new_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                new_str += '#'
            new_str += '\n'
        return new_str[:-1]

    @property
    def width(self):
        """Get width"""
        return self__width

    @width.setter
    def width(self, value):
        """Set the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height"""
        return self__height

    @height.setter
    def height(self, value):
        """Set the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a Rectangle instance
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and return  the perimeter of a Rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
