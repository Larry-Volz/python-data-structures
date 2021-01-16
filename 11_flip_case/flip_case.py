def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

        FROM TEACHER'S SOLUTION
        Turns out there is a function .swapcase()
        wasn't in the notes.  Good to know going forward...

    """
    phrase2=""
    for ltr in phrase:
        if ltr.lower() == to_swap.lower() and ltr.islower():
            phrase2 += ltr.upper()
        elif ltr.lower() == to_swap.lower() and ltr.isupper():
            phrase2 += ltr.lower()
        else:
            phrase2 += ltr
    return phrase2

print('aAAAhhh=', flip_case('Aaaahhh', 'a'))
print('aAAAhhh = ',flip_case('Aaaahhh', 'A'))
print('AaaaHHH', flip_case('Aaaahhh', 'h'))