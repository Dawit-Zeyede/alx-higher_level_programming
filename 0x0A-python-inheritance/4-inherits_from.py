#!/usr/bin/python3
"""Inherited class-checking methon."""


def inherits_from(obj, a_class):
    """check for inherited instance
    Args:
        obj (any): checked object
        a_class (type): compare for class.
    Returns:
        A boolean of inheritance.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
