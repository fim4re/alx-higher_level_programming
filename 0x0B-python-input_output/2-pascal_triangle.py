#!/usr/bin/python3
"""Pascal's Triangle function."""


def pascal_triangle(n):
    """Pascal's Triangle of size n."""
    if n <= 0:
        return []

    trgls = [[1]]
    while len(trgls) != n:
        tr = trgls[-1]
        cp_t = [1]
        for j in range(len(tr) - 1):
            cp_t.append(tr[j] + tr[j + 1])
        cp_t.append(1)
        trgls.append(cp_t)
    return (trgls)
