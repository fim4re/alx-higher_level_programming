#!/usr/bin/python3
'''Module for Square class.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''class square.'''

    def __init__(self, size, x=0, y=0, id=None):
        '''new square.'''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''set and get Size of this square.'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def _update_(self, id=None, size=None, x=None, y=None):
        '''updates method.'''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Updates this square.'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''Returns dictionary of this class.'''
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}

    def __str__(self):
        '''Returns info this square.'''
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)
