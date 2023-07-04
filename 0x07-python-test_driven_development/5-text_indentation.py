#!/usr/bin/python3
# 5-text_indentation.py
"""Defining a text-indentation function"""


def text_indentation(text):
    """Printing text with 2 new lines after each '.', '?', && ':'

    Args:
        text (string): printing text
    Raises:
        TypeError: In case text is !string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
