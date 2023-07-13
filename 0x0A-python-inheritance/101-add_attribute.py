#!/usr/bin/python3
"""Defining a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object ? possible.

    Args:
        obj (any): Oject to add an attribute to.
        att (str): Name of the attribute to add to obj.
        value (any): Value of att.
    Raises:
        TypeError: In case the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
