#!/usr/bin/python3
"""class Student."""


class Student:
    """Represent of student."""
    def __init__(self, first_name, last_name, age):
        """new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary of student."""

        if (type(attrs) == list and
                all(type(at) == str for at in attrs)):
            return {rs: getattr(self, rs) for rs in attrs if hasattr(self, rs)}
        return self.__dict__
