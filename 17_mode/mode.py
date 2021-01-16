def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

    SEE TEACHER'S SOLUTION
    He uses a dictionary, {}.get(num, 0)+1 to ad them up then max()...
    convoluted but clever - worth seeing a different way to do it

    """
    mode = 0
    for ea in nums:
        if nums.count(ea) > nums.count(mode):
            mode = ea
    return mode


print("1 = ",mode([1, 2, 1]))
print("2 = ",mode([2, 2, 3, 3, 2]))

#Teacher's solution (worth reviewing):
# for num in nums:
#         counts[num] = counts.get(num, 0) + 1 #0 is default - adds one if none exist
#     # returns {2:3, 3:2}
#     # find the highest value (the most frequent number)

#     max_value = max(counts.values())

#     # now we need to see at which index the highest value is at

#     for (num, freq) in counts.items():
#         if freq == max_value:
#             return num
