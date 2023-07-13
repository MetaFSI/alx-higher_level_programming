#!/usr/bin/python3
"""Defines a class MyInt that inherits from int"""


class MyInt(int):
    """Invert int operators equal and !=."""

    def __eq__(self, value):
        """Override equal opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override isnot operator with == behavior."""
        return self.real == value
