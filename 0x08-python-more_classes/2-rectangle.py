#!/usr/bin/python3
"""
Defines a class Rectangle
"""

class Rectangle:
    """Representation of a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.width = width
        self.height = height

        @property
        def height(self):
            """getter for the private instance attribute height"""
            return self.__height

        @height.setter
        def height(self, value):
            """setter for the private instance attribute height"""
            if type(value) is not int:
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value

            def area(self):
                """returns the area of the rectangle"""
                if self.__width == 0 or self.__height == 0:
                    return 0
                return (self.__width * 2) + (self.__height * 2)
