#!/usr/bin/python3
"""Defines a lock"""


class LockedClass:
    """
    Prevent user from instantiating new LockedCls attributes
    for anything but attributes named as 'first_name'.
    """

    __slots__ = ["first_name"]
