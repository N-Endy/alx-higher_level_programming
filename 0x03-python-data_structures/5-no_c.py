#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for s in my_string:
        if not (s == 'c' or s == 'C'):
            new_string += s
    return new_string
