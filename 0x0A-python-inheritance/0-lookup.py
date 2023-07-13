#!/usr/bin/python3
"""Defining object attribute lookup function"""


def lookup(obj):
    """Returingn a list of an object available attributes"""
    return (dir(obj))
