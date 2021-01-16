def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.       
    """
    if not isinstance(collection, (dict, set)):
        if start is None:
            start = 0
        for ea in range(start, len(collection)):
            if sought == collection[ea]:
                return True
        return False
    elif isinstance(collection, set):
        return sought in collection
    else:
        return sought in collection.values()

print("True = ", includes([1, 2, 3], 1))
print("False = ", includes([1, 2, 3], 1, 2))
print("True = ", includes("hello", "o"))
print("True = ", includes(('Elmo', 5, 'red'), 'red', 1))
print("True = ", includes({1, 2, 3}, 1))
print("True = ", includes({1, 2, 3}, 1, 3))  # "start" ignored for sets!
print("True = ", includes({"apple": "red", "berry": "blue"}, "blue"))