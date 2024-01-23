#!/usr/bin/python3

"""class square."""


class Square:
    """define square."""

    def __init__(self, size=0):
        """new square.

        Args:
        size: size of the new square.
        """

    @property
    def size(self):
        """set/get the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """square with # character."""
        for i in range(0, self.__size):
            for j in range(self.__size):
                [print("#", end="")]
                print("")
        if self.__size == 0:
            print("")
