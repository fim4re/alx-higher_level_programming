#!/usr/bin/python3
"""Def Rectangle class."""


class Rectangle:
    """Represent a rectangle (fm)."""

    def __init__(self, width=0, height=0):
        """new Rectangle.

        Args:
            width: width of a new rectangle.
            height: height of a new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set width of the rectangle (fm)."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set height of the rectangle (fm)."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
