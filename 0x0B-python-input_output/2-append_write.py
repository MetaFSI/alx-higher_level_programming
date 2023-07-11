#!/usr/bin/python3
"""Defining a file-appending fn"""


def append_write(filename="", text=""):
    """Appending a string to end of a UTF8 text file

    Args:
        filename (str): Name of file to append to
        text (str): Appended string to the file.
    Returns:
        Characters number appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
