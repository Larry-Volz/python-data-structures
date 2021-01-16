def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    lt_to_rb = 0
    rt_to_lb = 0
    vert_idx = 0
    for l in range(len(matrix)):
        lt_to_rb += matrix[l][l]
    for r in range(len(matrix)-1,-1,-1):
        # print(f"matrix[{vert_idx}][{r}] = {matrix[vert_idx][r]}")
        rt_to_lb += matrix[vert_idx][r]
        vert_idx += 1
    return lt_to_rb + rt_to_lb

    # TEACHERS - REVIEW THIS
    # total = 0

    # for i in range(len(matrix)):
    #     total += matrix[i][i]
    #     total += matrix[i][-1 - i]

    # return total

    # # or, probably too tersely:
    # #
    # # return sum([matrix[i][i] + matrix[i][-1 - i] for i in range(len(matrix))])
