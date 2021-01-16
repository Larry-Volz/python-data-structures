def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    **REVIEW THIS!

    """
    visited = set()
    for ea in nums:
        diff = goal-ea
        if diff in visited:
            return (diff, ea)
        visited.add(ea)
    return ()

print("(2, 2) = ", sum_pairs([1, 2, 2, 10], 4))

# (4, 2) sum to 6, and come before (5, 1):
print("(4, 2) = ", sum_pairs([4, 2, 10, 5, 1], 6))

#(4, 3) sum to 7, and finish before (5, 2):
print("(4,3) = ", sum_pairs([5, 1, 4, 8, 3, 2], 7))

# No pairs sum to 100, so return empty tuple:
print("() = ", sum_pairs([11, 20, 4, 2, 1, 5], 100))

