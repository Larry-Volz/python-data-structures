def partition(lst, fn):
    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

    TEACHER'S SOLUTION (only runs functions on ea once)
    true_list = []
    false_list = []

    for val in lst:
        if fn(val):
            true_list.append(val)
        else:
            false_list.append(val)

    return [true_list, false_list]

    """
    return [[ea for ea in lst if fn(ea)], [ea for ea in lst if fn(ea)==False]]

def is_even(num):
    return num % 2 == 0
    
def is_string(el):
    return isinstance(el, str)

print("[[2, 4], [1, 3]] = ", partition([1, 2, 3, 4], is_even))
    
print("[['hi', 'bye'], [None, 6]] = ", partition(["hi", None, 6, "bye"], is_string))
    