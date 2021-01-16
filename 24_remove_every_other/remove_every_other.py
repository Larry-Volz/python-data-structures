def remove_every_other(lst):
    """Return a new list of every other item.
    This should return a list, not mutate the original:
    """
    return [ea for ea in lst if lst.index(ea) % 2 == 0 ]

#OTHER SOLUTIONS FROM TEACHERS
#return lst[::2]

# Okay way
# return [val for i, val in enumerate(lst) if i % 2 == 0]


#TESTS
lst = [1, 2, 3, 4, 5]

print("[1, 3, 5] = ", remove_every_other(lst))
print("[1, 2, 3, 4, 5] = ", lst)
