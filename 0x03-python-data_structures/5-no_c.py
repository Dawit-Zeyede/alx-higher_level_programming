#!/usr/bin/python3
def no_c(my_string):
    str_Cc = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            str_Cc += char
    return (str_Cc)
