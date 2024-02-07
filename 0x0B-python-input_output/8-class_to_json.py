#!/usr/bin/python3
"""class-to-JSON function."""


def class_to_json(obj):
    """Return dictionary of a simple data structure."""
    return obj.__dict__
