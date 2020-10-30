# Write a Python program to get the largest number from a list.

def largest(a):
    largeNum = 0
    for i in a:
        if i > largeNum:
            largeNum = i
        else:
            largeNum = largeNum
    return largeNum
