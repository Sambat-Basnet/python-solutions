# Write a Python program to get the smallest number from a list.

def smallest(a):
    smallNum = a[0]
    for i in a:
        if i < smallNum:
            smallNum = i
        else:
            smallNum = smallNum
    return smallNum


print(smallest([1, 3, 2, 12]))
