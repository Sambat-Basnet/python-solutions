# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

def countNumInAList(a):
    x = []
    for i in a:
        if len(i) >= 2 and i[0] == i[-1]:
            x.append(i)
    return len(x)
