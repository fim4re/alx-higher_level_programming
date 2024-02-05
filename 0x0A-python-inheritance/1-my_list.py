#!/usr/bin/python3
"""list class MyList."""


class MyList(list):
        """built-in list class."""

        def print_sorted(self):
            """Print a sorted list."""
            print(sorted(self))
