def is_odd_string(word):
    
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:
    
        >>> is_odd_string('a')
        True

        >>> is_odd_string('A')
        True

    These sum to 4, which is not odd:
    
        >>> is_odd_string('aaaa')
        False

        >>> is_odd_string('AAaa')
        False

    Longer example:
    
        >>> is_odd_string('amazing')
        True
    """
    translator = '_abcdefghijklmnopqrstuvwxyz'
    return sum([translator.index(ltr) for ltr in word.lower()]) % 2 != 0

    # Hint: you may find the ord() function useful here
    #char.ord() gives the unicode so just need to subtract a-1 from it to get offset

    # TEACHERS SOLUTION:
    # DIFF = ord("a") - 1
    # total = sum((ord(c) - DIFF) for c in word.lower())
    # return total % 2 == 1