#!/usr/bin/python3
'''inherits_from method.'''


def inherits_from(obj, a_class):
        '''if an object is a true subclass.'''
        return isinstance(type(obj), a_class) and type(obj) != a_class
