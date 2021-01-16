def sum_floats(nums):
    """Return sum of floating point numbers in nums.

    """

    # hint: to find out if something is a float, you should use the
    # "isinstance" function --- research how to use this to find out
    # if something is a float!
    sum = 0
    for num in nums:
        if isinstance(num, float):
            sum+=num
    return sum

#TEACHER'S SOLUTION
#return sum([num for num in nums if isinstance(num, float)])

print("3.9 = ", sum_floats([1.5, 2.4, 'awesome', [], 1]))
print("0 = ", sum_floats([1, 2, 3]))
