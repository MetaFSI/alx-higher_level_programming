#!/usr/bin/python3
# 4-print_square.py
"""Defining a square-printing function."""


def print_square(size):
    """Printing square with # character.

    Args:
        size (int): height/width of square
    Raises:
        TypeError: In case size is not an integer
        ValueError: In case size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
