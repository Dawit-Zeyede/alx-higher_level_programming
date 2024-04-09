#!/usr/bin/python3
"""Class: Rectangle"""


class Rectangle:
    """Class: Rectangle body"""

    def __init__(self, width=0, height=0):
        """Intializes a rectangle instance."""
        self.width = width
        self.height = height

    def __str__(self):
        """Returns string representation of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ''
        new_str = ''
        for i in range(self.__height):
            for j in range(self.__widht):
                new_str += '#'
            new_str += '\n'
        return new_str[:-1]

    def __repr__(self):
        """String representaion of a rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes a rectangle instance."""
        print("Bye rectangle...")

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
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
        """Set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area fo rectangele instance"""
        return self.__width * self.__height

    def perimeter(self):
        """Perimeter of rectangle instance"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
