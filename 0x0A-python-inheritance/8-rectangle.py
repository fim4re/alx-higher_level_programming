#!/usr/bin/python3
'''Rectangle class.'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''representing a rectangle.'''
    def __init__(self, width, height):
        '''new rectangle.'''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
