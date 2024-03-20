#!/usr/bin/python3
def uniq_add(my_list=[]):
    lis = set(my_list)
    num = 0
    for i in lis:
        num += i
    return (num)
