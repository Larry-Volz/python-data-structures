def find_factors(num):
    """Find factors of num, in increasing order.
    """
    return [ea for ea in range(1, num+1) if num%ea == 0]
    # mine's more elegant than teachers :)

print("[1, 2, 5, 10] =", find_factors(10))
print("[1, 11] = ", find_factors(11))
print("[1, 3, 37, 111] = ", find_factors(111))
print("[1, 293, 1097, 321421] = ", find_factors(321421))

