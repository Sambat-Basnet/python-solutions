# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.

def keyOrder(n):
    return n[-1]


def sortatuple(a):
    return sorted(a, key=keyOrder)
