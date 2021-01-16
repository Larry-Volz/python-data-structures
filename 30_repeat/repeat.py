def repeat(phrase, num):
    #JUST DISCOVERED DOCTEST!!!
    #ALL THIS TIME i'VE BEEN MANUALLY CUTTING AND PASTING THE DOCTESTS TO MANUALLY
    #TEST THEM WHEN I COULD HAVE JUST BEEN RUNNING THEM!
    #GAAAAAHHHH!!!

    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
    if isinstance(num, (int, float)) and num >= 0:
        return phrase * num
    else:
        return None

