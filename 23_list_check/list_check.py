def list_check(lst):
    """Are all items in lst a list?
        
    """
    return all([isinstance(ea, list) for ea in lst])

#MINE IS BETTER THAN TEACHERS THIS TIME!
#   all() returns true if ALL items are true

#HERE IS THEIRS:
    # for item in lst:
    #     if not isinstance(item, list):
    #         return False
    # return True

print("True = ", list_check([[1], [2, 3]]))
print("False = ", list_check([[1], "nope"]))
print("False = ", list_check(["nope", [1]]))