#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return
    lis = my_list[:]
    for i, c in enumerate(lis):
        if c == search:
            lis[i] = replace
    return (lis)
