def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    if parens.index(")") !=0:
        return parens.count("(") == parens.count(")")
    return False

    # fast fail: ) is first (index = 0) 
    # or unequal amount
    #my solution is more elegant that teachers - she manually 
    # adds one for ( and subtracts one  for ) and checks for = 0