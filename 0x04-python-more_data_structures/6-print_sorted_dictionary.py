#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return
    lis = list(a_dictionary.keys())
    lis.sort()
    for i in lis:
        print("{}: {}".format(i, a_dictionary.get(i)))
