#!/usr/bin/python3
"""Defining an inherited class-checking function"""


def inherits_from(obj, a_class):
    """Checks in case an object is an inherited instance of a class

    Args:
        obj (any): Object to check
        a_class (type): The class to match the type of obj to
    Returns:
        In case obj is an inherited instance of a_class - True
        Otherwise - False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
