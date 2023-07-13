#!/usr/bin/python3
"""Defining a class-checking function"""


def is_same_class(obj, a_class):
    """Check in case an object is exactly instance of a given class

    Args:
        obj (any): Object to check.
        a_class (type): lass to match the type of obj to.
    Returns:
        In case obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
