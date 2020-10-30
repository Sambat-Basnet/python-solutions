# Write a Python function that takes two lists and returns True if they have at least one common member.

def commonMember(firstList, secList):
    for i in firstList:
        if i in secList:
            return True
        else:
            return False
