#!/usr/bin/python3
"""Function to read file"""


def read_file(filename=""):
    """
    read_file function
    It reads a text file of format UTF8 and prints it to standard output.
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        print(f.read(), end='')
