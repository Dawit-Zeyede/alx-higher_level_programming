#!/usr/bin/python3

"""Return instance of a specific class."""


def is_same_class(obj, a_class):
    """Check if an object is an instance of a given class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to compare the type of obj to.
    Returns:
        True: if it is an instance of a_class.
        False: otherwise
    """
    if type(obj) == a_class:
        return True
    return False
