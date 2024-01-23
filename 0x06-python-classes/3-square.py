#!/usr/bin/python3
"""class Square."""


class Square:
    """Defines square."""
    def __init__(self, size=0):
        """new square.
        Args:
        size: size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """return the area of square."""
        return (self.__size * self.__size)
