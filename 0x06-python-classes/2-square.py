#!/usr/bin/python3
"""Class square."""


class Square:
    """Defines square."""
    def ___init__(self, size=0):
        """New square.
        Args:
        size: size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
