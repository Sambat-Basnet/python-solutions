#  Write a Python program to remove duplicates from a list.

def removeDupli(a):
    x = []
    for i in a:
        if i not in x:
            x.append(i)
    return x
