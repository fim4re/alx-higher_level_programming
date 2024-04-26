#!/usr/bin/python3
""" peak-finding algorithm."""


def find_peak(list_of_integers):
    """ Finds the peak in a list of ints """
    if list_of_integers is None or list_of_integers == []:
        return None

    le = len(list_of_integers)
    mid = int(le / 2)
    lo = list_of_integers

    if mid - 1 < 0 and mid + 1 >= le:
        return lo[mid]
    elif mid - 1 < 0:
        return lo[mid] if lo[mid] > lo[mid + 1] else lo[mid + 1]
    elif mid + 1 >= le:
        return lo[mid] if lo[mid] > lo[mid - 1] else lo[mid - 1]

    if lo[mid - 1] < lo[mid] > lo[mid + 1]:
        return lo[mid]

    if lo[mid + 1] > lo[mid - 1]:
        return find_peak(lo[mid:])
    return find_peak(lo[:mid])
