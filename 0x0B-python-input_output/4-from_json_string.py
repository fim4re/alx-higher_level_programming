#!/usr/bin/python3
"""JSON-to-object function."""
import json


def from_json_string(my_str):
    """Return the Python object JSON string."""
    return json.loads(my_str)
