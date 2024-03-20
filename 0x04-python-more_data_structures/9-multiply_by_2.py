#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dicti = a_dictionary.copy()
    lis = list(dicti.keys())
    for i in lis:
        dicti[i] *= 2
    return (dicti)
