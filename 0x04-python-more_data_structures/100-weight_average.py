#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        return (sum(i * b for i, b in my_list) / sum(b for i, b in my_list))
