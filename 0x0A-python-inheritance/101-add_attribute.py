#!/usr/bin/python3
"""adds attributes to objects."""


def add_attribute(obj, att, value):
    '''new attribute to an object.'''
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
