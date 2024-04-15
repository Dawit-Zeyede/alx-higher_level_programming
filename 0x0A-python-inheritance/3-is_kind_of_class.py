#!/usr/bin/python3
"""A class and inherited class-cheking funcion."""


def is_kind_of_class(obj, a_class):
    """check for instacne of class:
    Args:
        obj (any): To be chekceed.
        a_class (type): to be compared.
    Returns:
        Boolean of an instance.
    """
    if isinstance(obj, a_class):
        return True
    return False
