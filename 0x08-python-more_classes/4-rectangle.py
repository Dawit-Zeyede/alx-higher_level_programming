#!/usr/bin/python3
"""Class: Rectange"""


class Rectangle:
    """Class: REctangle body"""

    def __init__(self, width=0, height=0):
        """Intializes a method"""
        self.width = width
        self.height = height

    def __str__(self):
        """Informal stirng representaiton"""
        if self.__height == 0 or self.__width == 0:
            return ''
        new_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                new_str += '#'
            new_str += '\n'
        return new_str[:-1]

    def __repr__(self):
        """internal string representaiton"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter ofrectangle"""
        if self__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
