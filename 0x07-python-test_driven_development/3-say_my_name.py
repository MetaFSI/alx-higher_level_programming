#!/usr/bin/python3
# 3-say_my_name.py
"""Defining name-printing function"""


def say_my_name(first_name, last_name=""):
    """Printing name

    Args:
        first_name (str): printing first name
        last_name (str): Printing last name
    Raises:
        TypeError: In case either of first_name || last_name are !strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
