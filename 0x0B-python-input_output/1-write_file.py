#!/usr/bin/python3
"""function to write a text to given filename"""


def write_file(filename="", text=""):
    """Write 'text' to a 'filename'
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        return my_file.write(text)
