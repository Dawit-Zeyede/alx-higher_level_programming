#!/usr/bin/python3
"""Instance of a specific class."""


def is_same_class(obj, a_class):
    """Check if an object is an instance of a givn class.
    Args:
        obj (any): to be checked.
        a_class (type): class to be compared.
    Returns:
        Boolean of an instance of a_class.
    """
    if type(obj) == a_class:
        return True
    return False
