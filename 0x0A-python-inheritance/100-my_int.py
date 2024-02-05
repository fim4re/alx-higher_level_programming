#!/usr/bin/python3
"""MyInt that inherits from int."""


class MyInt(int):
    """operators == and !=."""

    def __eq__(self, val):
        """change == opeartor with !=."""
        return self.real != val

    def __ne__(self, val):
        """change != operator with ==."""
        return self.real == val
