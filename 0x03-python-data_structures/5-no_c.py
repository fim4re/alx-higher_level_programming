#!/usr/bin/python3
def no_c(my_string):
    t = ""
    for y in range(len(my_string)):
        if (my_string[y] != 'c' and my_string[y] != 'C'):
            t += my_string[y]
    return t
