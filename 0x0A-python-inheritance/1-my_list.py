#!/usr/bin/python3
"""inherits from the list class"""


class MyList(list):
    """inherits form list"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))