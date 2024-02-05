#!/usr/bin/python3
'''Rectangle class.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''representing a rectangle.'''
    def __init__(self, size):
        '''new rectangle.'''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        '''Return string of this square.'''
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
