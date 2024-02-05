#!/usr/bin/python3
'''Rectangle class.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''representing a rectangle.'''
    def __init__(self, size):
        '''new rectangle.'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
